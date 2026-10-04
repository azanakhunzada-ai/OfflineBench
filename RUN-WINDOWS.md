# Windows Run Guide

## Backend (PowerShell 1)
```powershell
cd "C:\Users\hamda\OneDrive\Documents\nechmark\OfflineAI-Benchmark-Lab-Elite\backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
If activation is blocked:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
```
Test: http://localhost:8000/health

## Frontend (PowerShell 2)
```powershell
cd "C:\Users\hamda\OneDrive\Documents\nechmark\OfflineAI-Benchmark-Lab-Elite\frontend"
npm install
npm run dev
```
Open: http://localhost:3000

## Ollama
```powershell
ollama list
```
Make sure Ollama is running and at least one local model is installed.

## First test
Select the model in the dashboard and ask: `Explain RAG in simple words.` Then click `Run benchmark`.
