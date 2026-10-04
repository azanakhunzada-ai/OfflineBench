import os, time, httpx
from dotenv import load_dotenv
load_dotenv()
BASE=os.getenv("OLLAMA_BASE_URL","http://127.0.0.1:11434")

async def models():
    async with httpx.AsyncClient(timeout=30) as c:
        r=await c.get(f"{BASE}/api/tags"); r.raise_for_status()
        return r.json().get("models",[])

async def chat(model:str,prompt:str):
    start=time.perf_counter()
    async with httpx.AsyncClient(timeout=180) as c:
        r=await c.post(f"{BASE}/api/chat",json={"model":model,"messages":[{"role":"user","content":prompt}],"stream":False})
        r.raise_for_status()
        data=r.json()
    latency=(time.perf_counter()-start)*1000
    text=data.get("message",{}).get("content","")
    tokens=data.get("eval_count") or max(1,len(text.split()))
    duration=max(0.001,data.get("eval_duration",0)/1e9) if data.get("eval_duration") else max(0.001,latency/1000)
    return {"answer":text,"latency_ms":latency,"tokens_per_sec":tokens/duration}
