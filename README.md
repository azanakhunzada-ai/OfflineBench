# Offline AI Benchmark Lab — Elite

A portfolio-grade local AI assistant and model benchmarking laboratory.

## What it does
- Runs local models through Ollama.
- Chat UI with model selection.
- Measures first-token latency, total latency, approximate tokens/sec.
- Runs a repeatable benchmark suite.
- Stores benchmark runs in SQLite.
- Shows model comparisons, hardware profile, and benchmark history.
- Includes domain benchmark categories: General, Coding, Healthcare, Banking, Legal.
- Designed to work offline after models are installed.

## Architecture
Browser (Next.js) -> FastAPI -> Ollama -> Local model
                         |
                         -> SQLite benchmark database

## Frontend
Next.js + TypeScript + Tailwind-style CSS + Recharts.

## Backend
FastAPI + Pydantic + httpx + SQLAlchemy/SQLite.

## Requirements
- Node.js 20.9+
- Python 3.11+
- Ollama installed and running
- At least one local model

## Start backend (Windows PowerShell)
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000

## Start frontend
cd frontend
npm install
npm run dev

Open http://localhost:3000

## Ollama
Install Ollama separately, then:
ollama pull gemma3:4b
ollama list

Set OLLAMA_BASE_URL if your Ollama endpoint differs.

## Important
The benchmark numbers shown by this app are measured on your machine. They are not universal model rankings.
