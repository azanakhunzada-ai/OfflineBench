# 🧠 Offline AI Benchmark Lab — Elite

> **A portfolio-grade, fully local AI assistant and model benchmarking laboratory built for measuring, comparing, and evaluating local LLM performance.**

Offline AI Benchmark Lab — Elite is a local-first AI experimentation platform that connects a modern web dashboard to **Ollama**, allowing you to chat with locally hosted models and run repeatable benchmarks on your own hardware.

The platform measures real performance on your machine rather than relying on generic online benchmarks.

---

## 🚀 What It Does

### 💬 Local AI Chat

* Chat with locally installed Ollama models.
* Switch between available models.
* Stream model responses in real time.
* Works without cloud APIs after models are installed.
* Keeps inference entirely on your machine.

### ⚡ Performance Benchmarking

Measures:

* First-token latency
* Total response latency
* Approximate tokens/second
* Prompt processing performance
* Generation performance
* Response completion time
* Benchmark consistency

### 🧪 Repeatable Benchmark Suite

Run standardized prompts across different models and compare their performance under the same conditions.

Benchmark categories include:

* **General AI**
* **Coding**
* **Healthcare**
* **Banking**
* **Legal**

### 📊 Model Comparison

Compare locally installed models using:

* Speed
* Latency
* Tokens/sec
* Benchmark scores
* Category performance
* Historical runs

### 🖥️ Hardware Profile

The application records the local machine environment used for benchmarking, helping make benchmark results reproducible and meaningful.

### 🗃️ Benchmark History

Results are persisted in SQLite so previous benchmark runs can be reviewed and compared later.

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      Browser         │
                         │   Next.js Dashboard  │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP / Streaming
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         │    Python Backend    │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌─────────────────┐             ┌─────────────────┐
          │     Ollama      │             │ SQLite Database │
          │  Local Models   │             │ Benchmark Data  │
          └────────┬────────┘             └─────────────────┘
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
      Local LLMs       Model Runtime
```

### Data Flow

```text
User
  │
  ▼
Next.js UI
  │
  ▼
FastAPI API
  │
  ├──────────────► Ollama
  │                   │
  │                   ▼
  │              Local LLM
  │                   │
  │                   ▼
  │              Token Stream
  │
  └──────────────► SQLite
                      │
                      ▼
               Benchmark History
```

---

# 🧰 Technology Stack

## Frontend

* Next.js
* React
* TypeScript
* Tailwind-style CSS
* Recharts
* Modern responsive dashboard UI

## Backend

* Python 3.11+
* FastAPI
* Pydantic
* HTTPX
* SQLAlchemy
* SQLite
* Uvicorn

## AI Runtime

* Ollama
* Local open-source LLMs

## Database

* SQLite

---

# 📋 Requirements

Before running the application, install:

### Required

* **Node.js 20.9+**
* **Python 3.11+**
* **Ollama**
* At least one local AI model
* Git

Check your versions:

```powershell
node --version
```

```powershell
python --version
```

```powershell
ollama --version
```

```powershell
git --version
```

---

# 🤖 Ollama Setup

Install Ollama separately.

Verify that Ollama is running:

```powershell
ollama list
```

Pull a model:

```powershell
ollama pull gemma3:4b
```

Verify:

```powershell
ollama list
```

You can install additional models for comparison.

For example:

```powershell
ollama pull llama3.2:3b
```

```powershell
ollama pull qwen2.5:7b
```

```powershell
ollama pull qwen2.5-coder:7b
```

> Model availability depends on your Ollama installation and local hardware.

---

# 📁 Project Structure

```text
OfflineAI-Benchmark-Lab-Elite/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── database/
│   │   └── benchmark/
│   │
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
│
├── benchmarks/
│   ├── general/
│   ├── coding/
│   ├── healthcare/
│   ├── banking/
│   └── legal/
│
├── data/
│   └── benchmark.db
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository:

```powershell
git clone https://github.com/YOUR_USERNAME/OfflineAI-Benchmark-Lab-Elite.git
```

Enter the project:

```powershell
cd OfflineAI-Benchmark-Lab-Elite
```

---

# 🐍 Backend Setup

Enter the backend directory:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Start FastAPI:

```powershell
python -m uvicorn app.main:app --reload --port 8000
```

Backend API:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

---

# 🌐 Frontend Setup

Open another PowerShell terminal.

Enter the frontend directory:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Open:

```text
http://localhost:3000
```

---

# 🔌 Environment Configuration

The application can use a custom Ollama endpoint.

Set:

```text
OLLAMA_BASE_URL
```

Example:

```powershell
$env:OLLAMA_BASE_URL="http://localhost:11434"
```

The default Ollama endpoint is:

```text
http://localhost:11434
```

---

# 📡 API

The backend exposes endpoints for the frontend and benchmarking system.

Typical endpoints include:

```text
GET  /api/health
GET  /api/models
POST /api/chat
POST /api/benchmark
GET  /api/benchmarks/history
GET  /api/hardware
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

---

# 🧪 Benchmark System

The benchmark engine executes standardized prompts against selected local models.

Each benchmark records metrics such as:

```text
Model
Category
Prompt
Response
First-token latency
Total latency
Approximate token count
Tokens/sec
Timestamp
Hardware profile
```

Example benchmark flow:

```text
Select Model
      │
      ▼
Select Category
      │
      ▼
Load Standard Prompts
      │
      ▼
Send Prompt → Ollama
      │
      ▼
Measure Latency
      │
      ▼
Estimate Tokens/sec
      │
      ▼
Calculate Benchmark Score
      │
      ▼
Save Result → SQLite
      │
      ▼
Display Dashboard
```

---

# 🧠 Benchmark Categories

## General

Tests:

* Reasoning
* Summarization
* Instruction following
* General knowledge
* Structured responses

## Coding

Tests:

* Code generation
* Debugging
* Algorithm design
* Refactoring
* Explanation of code

## Healthcare

Tests:

* Medical terminology
* Clinical reasoning
* Patient communication
* Safety-aware responses
* Structured medical information

> Healthcare benchmarks are evaluation tasks only and are not intended to provide medical advice.

## Banking

Tests:

* Financial reasoning
* Transaction analysis
* Risk scenarios
* Structured financial data
* Banking terminology

> Banking benchmarks are evaluation tasks only and are not financial advice.

## Legal

Tests:

* Legal terminology
* Document analysis
* Rule interpretation
* Scenario reasoning
* Structured legal responses

> Legal benchmarks are evaluation tasks only and are not legal advice.

---

# 📈 Performance Metrics

## First Token Latency

The approximate time between sending a prompt and receiving the first generated token.

```text
First Token Latency =
Time(first token received) - Time(request started)
```

Lower is generally better.

---

## Total Latency

Total time required to receive the model response.

```text
Total Latency =
Time(response completed) - Time(request started)
```

Lower is generally better for interactive workloads.

---

## Tokens Per Second

Approximate generation throughput:

```text
Tokens/sec =
Estimated output tokens / Generation time
```

Higher is generally better.

Because token counting can differ between models and APIs, these values should be treated as approximate unless an exact tokenizer is used.

---

# 🏆 Benchmark Scoring

The project can combine multiple measurements into an overall benchmark score.

Example:

```text
Overall Score
│
├── Response Quality
├── First Token Latency
├── Total Latency
├── Tokens/sec
└── Category Performance
```

The exact scoring methodology should remain transparent so users can understand how the final score was produced.

---

# 💾 SQLite Database

Benchmark results are stored locally in SQLite.

Example conceptual schema:

```text
benchmark_runs
│
├── id
├── model
├── category
├── prompt
├── response
├── first_token_latency
├── total_latency
├── tokens_per_second
├── score
├── hardware_profile
└── created_at
```

SQLite makes the application easy to run without requiring:

* PostgreSQL
* MySQL
* Cloud databases
* External database servers

---

# 🖥️ Hardware-Aware Benchmarking

Benchmark results depend heavily on local hardware.

Important factors include:

* CPU
* GPU
* RAM
* VRAM
* Operating system
* Model size
* Quantization
* Ollama configuration
* Background workloads

Therefore:

> **Benchmark results from this application represent performance on the machine where the benchmark was executed.**

They should not be interpreted as universal model rankings.

---

# 🔒 Privacy & Offline Design

The application is designed around local execution.

After the required software and models are installed:

```text
Browser
   │
   ▼
Local FastAPI
   │
   ▼
Local Ollama
   │
   ▼
Local Model
```

No cloud AI API is required for inference.

Your prompts and model responses can remain on your machine.

---

# 🌐 Internet Requirements

Internet access is generally required for:

* Installing dependencies
* Downloading Ollama
* Downloading models
* Installing npm packages
* Cloning the repository

After installation and model download, the application is designed to operate locally.

---

# 🧪 Recommended Test

After starting the application:

1. Open the dashboard.
2. Select an installed model.
3. Send a test prompt.
4. Confirm streaming works.
5. Open the benchmark section.
6. Select a category.
7. Run the benchmark.
8. Review latency and tokens/sec.
9. Run the same benchmark again.
10. Compare results.

Example prompt:

```text
Explain the difference between a process and a thread in an operating system.
Give the answer in five concise bullet points.
```

---

# 📊 Example Dashboard

The target dashboard contains:

```text
┌─────────────────────────────────────────────────────────────┐
│             OFFLINE AI BENCHMARK LAB                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Model: [ gemma3:4b ▼ ]       Status: ● Online              │
│                                                             │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌───────────┐ │
│ │ First      │ │ Total      │ │ Tokens/sec │ │ Score     │ │
│ │ Token      │ │ Latency    │ │            │ │           │ │
│ │ 320 ms     │ │ 4.2 sec    │ │ 18.4       │ │ 87.4      │ │
│ └────────────┘ └────────────┘ └────────────┘ └───────────┘ │
│                                                             │
│ Performance                                                │
│                                                             │
│ Tokens/sec ────────────────────────────────╮                │
│                                            │                │
│                                            ╰─────────────── │
│                                                             │
│ Model Comparison                                            │
│                                                             │
│ Model          Speed       Latency       Score              │
│ gemma3:4b      18.4 t/s    4.2s          87.4               │
│ llama3.2:3b    24.1 t/s    3.6s          84.8               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# 🛠️ Development

Backend:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --port 8000
```

Frontend:

```powershell
cd frontend
npm run dev
```

---

# 🧹 Production Build

Build the frontend:

```powershell
cd frontend
npm run build
```

Run the production frontend:

```powershell
npm run start
```

For the backend:

```powershell
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 🧪 Quality Checklist

Before considering a release ready:

```text
[ ] Ollama connection works
[ ] Model discovery works
[ ] Chat works
[ ] Streaming works
[ ] Model switching works
[ ] Benchmark execution works
[ ] Latency measurement works
[ ] Token estimation works
[ ] Tokens/sec calculation works
[ ] SQLite persistence works
[ ] Benchmark history works
[ ] Model comparison works
[ ] Hardware information works
[ ] Domain benchmarks work
[ ] Frontend responsive
[ ] API error handling works
[ ] Loading states implemented
[ ] Empty states implemented
[ ] README updated
[ ] .gitignore configured
```

---

# 🗺️ Roadmap

## Phase 1 — Core

* [x] Local Ollama integration
* [x] FastAPI backend
* [x] Next.js frontend
* [x] Local chat
* [x] Model selection

## Phase 2 — Benchmarking

* [x] Benchmark engine
* [x] Latency measurement
* [x] Token throughput
* [x] SQLite persistence
* [x] Benchmark history

## Phase 3 — Analytics

* [ ] Advanced model comparison
* [ ] Performance charts
* [ ] Category scoring
* [ ] Hardware comparison
* [ ] Benchmark export
* [ ] CSV/JSON reports

## Phase 4 — Elite

* [ ] Streaming telemetry
* [ ] Reproducible benchmark profiles
* [ ] Configurable benchmark suites
* [ ] Automated regression detection
* [ ] Model recommendation engine
* [ ] Benchmark run diffing
* [ ] Advanced hardware profiling
* [ ] Dark/light dashboard themes
* [ ] Professional reporting
* [ ] Docker deployment
* [ ] Automated testing
* [ ] CI/CD pipeline

---

# 🧩 Future Architecture

The project is designed to evolve toward:

```text
                     ┌─────────────────────┐
                     │   Next.js Web UI    │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     FastAPI API     │
                     └──────────┬──────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
        Chat Engine       Benchmark Engine    Hardware Profiler
             │                  │                  │
             ▼                  ▼                  ▼
          Ollama             SQLite             System Info
             │
             ▼
        Local Models
```

---

# 🔬 Why This Project?

Most AI applications focus only on generating responses.

This project focuses on **measuring the AI system itself**.

It provides a controlled environment for studying:

* Local LLM performance
* Model latency
* Inference throughput
* Hardware impact
* Model-size tradeoffs
* Domain-specific performance
* Reproducible benchmarking

This makes it useful as both a practical local AI assistant and an AI engineering portfolio project.

---

# ⚠️ Benchmark Disclaimer

Benchmark results are machine-dependent.

Performance can vary based on:

* Hardware
* Drivers
* RAM availability
* VRAM availability
* Model quantization
* Ollama version
* Operating system
* Background processes
* Prompt length
* Output length
* Model configuration

Therefore, benchmark results should be used for **relative comparison on the same system**, not as universal rankings.

---

# 🔐 Security

This project is intended for local development and experimentation.

Do not expose the FastAPI or Ollama endpoints directly to the public internet without implementing appropriate:

* Authentication
* Authorization
* Input validation
* Rate limiting
* Network restrictions
* Secure deployment configuration

---

# 📜 License

Add your preferred license here.

Example:

```text
MIT License
```

---

# 👨‍💻 Author

**Offline AI Benchmark Lab — Elite**

A local-first AI engineering and benchmarking project focused on:

```text
Local AI
+
LLM Evaluation
+
Performance Engineering
+
Benchmarking
+
Full-Stack Development
```

---

# ⭐ Project Goal

The ultimate goal is to provide a professional local laboratory where developers can:

> **Run, measure, compare, and understand local AI models on their own hardware.**

```text
INSTALL
   ↓
RUN
   ↓
CHAT
   ↓
BENCHMARK
   ↓
MEASURE
   ↓
COMPARE
   ↓
ANALYZE
   ↓
IMPROVE
```

**Offline AI Benchmark Lab — Elite**

**Local AI. Real Hardware. Real Measurements.**
