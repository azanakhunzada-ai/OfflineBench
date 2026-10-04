from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import select, func
from .db import SessionLocal, BenchmarkRun
from .services.ollama import models, chat
from .services.benchmark import run_suite

app=FastAPI(title="Offline AI Benchmark Lab API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000","http://127.0.0.1:3000"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

class ChatIn(BaseModel):
    model:str
    prompt:str

class BenchmarkIn(BaseModel):
    model:str|None=None
    categories:list[str]=["general","coding","healthcare","banking","legal"]

@app.get("/health")
async def health(): return {"status":"ok","mode":"offline"}

@app.get("/models")
async def get_models():
    try: return {"models":await models()}
    except Exception as e: raise HTTPException(503,f"Ollama unavailable: {e}")

@app.post("/chat")
async def do_chat(x:ChatIn):
    try: return await chat(x.model,x.prompt)
    except Exception as e: raise HTTPException(503,f"Local model error: {e}")

@app.post("/benchmark/run")
async def benchmark(x:BenchmarkIn):
    try:
        ms=await models()
        available=[m["name"] for m in ms]
        model=x.model or (available[0] if available else None)
        if not model: raise HTTPException(400,"No Ollama model installed.")
        results=await run_suite(model,x.categories)
        db=SessionLocal()
        try:
            for r in results: db.add(BenchmarkRun(model=model,**r))
            db.commit()
        finally: db.close()
        return {"model":model,"results":results}
    except HTTPException: raise
    except Exception as e: raise HTTPException(503,f"Benchmark failed: {e}")

@app.get("/benchmarks")
async def benchmarks(limit:int=50):
    db=SessionLocal()
    try:
        rows=db.scalars(select(BenchmarkRun).order_by(BenchmarkRun.created_at.desc()).limit(limit)).all()
        return {"runs":[{"model":r.model,"category":r.category,"accuracy":r.accuracy,"latency_ms":r.latency_ms,"tokens_per_sec":r.tokens_per_sec,"score":r.score,"created_at":r.created_at.isoformat()} for r in rows]}
    finally: db.close()

@app.get("/stats")
async def stats():
    db=SessionLocal()
    try:
        count=db.scalar(select(func.count()).select_from(BenchmarkRun)) or 0
        avg=db.scalar(select(func.avg(BenchmarkRun.latency_ms))) or 0
        best=db.scalars(select(BenchmarkRun).order_by(BenchmarkRun.score.desc()).limit(1)).first()
        try: model_count=len(await models())
        except Exception: model_count=0
        return {"models":model_count,"runs":count,"best_model":best.model if best else "—","avg_latency":float(avg)}
    finally: db.close()
