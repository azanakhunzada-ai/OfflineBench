# Architecture

## 1. User layer
Next.js dashboard provides:
- local assistant
- model selector
- benchmark controls
- result table
- performance chart

## 2. API layer
FastAPI exposes:
- GET /health
- GET /models
- POST /chat
- POST /benchmark/run
- GET /benchmarks
- GET /stats

## 3. Inference layer
Ollama is the local model runtime. The API never sends prompts to OpenAI/Gemini/Anthropic.

## 4. Measurement layer
The benchmark records:
- accuracy percentage
- end-to-end response latency
- approximate tokens/sec
- weighted score

## 5. Storage
SQLite stores benchmark runs so results survive restarts.

## Production upgrade path
- PostgreSQL
- Redis job queue
- WebSocket streaming
- hardware telemetry
- tokenizer-aware token counting
- larger curated benchmark datasets
- signed benchmark reports
