# My Little Gatherer

A personal AI knowledge assistant.

This project is a siblings' journey into modern LLM engineering, starting from a simple document assistant and gradually evolving into a more capable AI knowledge system.

The goal is to learn and apply modern AI engineering practices including RAG, embeddings, vector databases, LLM orchestration, evaluation, deployment, and agentic workflows.

## Run locally

The application has three local processes: llama.cpp, the Python API, and the Next.js UI.

1. Start llama.cpp using `scripts/start_model.bat`, or follow [the llama.cpp setup guide](docs/setup_llamacpp.md). The model server listens on `http://127.0.0.1:8080`.
2. From the repository root, install the Python package and start FastAPI:

    ```powershell
    uv sync
    uv run uvicorn gatherer.api.main:app --reload --port 8000
    ```

3. In a second terminal, install and start the Next.js UI:

    ```powershell
    cd ui
    npm install
    npm run dev
    ```

4. Open `http://localhost:3000`.

Next.js sends browser requests to its same-origin `/api/ask` route. That server route forwards them to FastAPI at `http://127.0.0.1:8000`. To use another API address, set the server-only `FASTAPI_URL` environment variable before starting Next.js.

Useful checks from `ui/`:

```powershell
npm run lint
npm run typecheck
npm run build
```

---

# Roadmap

## Phase 0 — Foundation & Setup

- [x] Create project repository
- [x] Set up Python virtual environment
- [x] Create clean project structure
- [x] Configure Git workflow
- [x] Write initial README
- [x] Add dependency management (uv)
- [x] Set up environment variables (.env)
- [ ] Add basic logging

---

# Phase 1 — First LLM Application

Goal: Understand how LLM applications work end-to-end.

- [x] Install local LLM runtime (llama.cpp)
- [x] Run first local model successfully
- [ ] Understand model parameters:
    - [ ] Temperature
    - [ ] Context window
    - [ ] Token limits
    - [ ] System prompts
- [x] Build simple Python LLM client
- [x] Create basic chat interface
- [ ] Support conversation history
- [ ] Add streaming responses

---

# Phase 2 — Application Architecture

Goal: Build like a real software system.

- [ ] Create backend API using FastAPI
- [ ] Create frontend using next.js
- [ ] Separate frontend/backend/model logic
- [ ] Add API endpoints
- [ ] Add request validation
- [ ] Add error handling
- [ ] Containerize with Docker
- [ ] Add basic testing

---

# Phase 3 — Document Intelligence

Goal: Make the AI understand files.

Support:

- [ ] PDF ingestion
- [ ] PowerPoint ingestion
- [ ] Word document ingestion
- [ ] Markdown ingestion
- [ ] Code file ingestion

Processing pipeline:

- [ ] Extract text
- [ ] Clean text
- [ ] Split documents into chunks
- [ ] Add metadata
    - filename
    - page number
    - timestamp
    - document type

---

# Phase 4 — Retrieval Augmented Generation (RAG)

Goal: Build a proper knowledge retrieval system.

- [ ] Learn embeddings
- [ ] Generate document embeddings
- [ ] Store embeddings in vector database
- [ ] Implement similarity search
- [ ] Retrieve relevant documents
- [ ] Construct prompts with retrieved context
- [ ] Generate answers grounded in documents
- [ ] Add source citations

Tech exploration:

- [ ] Qdrant
- [ ] Chroma
- [ ] FAISS

---

# Phase 5 — Improve Retrieval Quality

Goal: Move beyond basic tutorials.

- [ ] Experiment with chunk sizes
- [ ] Experiment with overlap
- [ ] Compare embedding models
- [ ] Add metadata filtering
- [ ] Add hybrid search
    - [ ] Keyword search
    - [ ] Semantic search
- [ ] Add reranking model
- [ ] Measure retrieval quality

---

# Phase 6 — Personal Knowledge Assistant

Goal: Make it useful for myself.

Features:

- [ ] Chat with all school notes
- [ ] Search past projects
- [ ] Find forgotten concepts
- [ ] Summarize lectures
- [ ] Generate revision notes
- [ ] Generate flashcards
- [ ] Quiz me on topics
- [ ] Explain concepts at different levels
- [ ] Compare documents

---

# Phase 7 — Multimodal AI

Goal: Understand more than text.

- [ ] OCR scanned documents
- [ ] Process images
- [ ] Understand diagrams
- [ ] Understand lecture slides
- [ ] Process handwritten notes
- [ ] Add vision-language model support

---

# Phase 8 — AI Agents & Tool Use

Goal: Learn modern agentic AI.

- [ ] Understand function calling
- [ ] Build simple tools
- [ ] Allow LLM to call tools
- [ ] Create document search tool
- [ ] Create summarization tool
- [ ] Create file generation tool
- [ ] Create study planner agent

Explore:

- [ ] MCP (Model Context Protocol)
- [ ] Agent frameworks
- [ ] Workflow orchestration

---

# Phase 9 — Production Engineering

Goal: Apply real AI engineering practices.

- [ ] Add automated evaluation
- [ ] Create test questions dataset
- [ ] Measure RAG accuracy
- [ ] Track latency
- [ ] Track token usage
- [ ] Add monitoring
- [ ] Add caching
- [ ] Optimize inference
- [ ] Deploy application
- [ ] Set up CI/CD

---

# Phase 10 — Advanced Exploration

Future ideas:

- [ ] Voice interface
- [ ] Personal knowledge graph
- [ ] Long-term memory
- [ ] Browser integration
- [ ] Email/document ingestion
- [ ] Autonomous research assistant
- [ ] Multi-agent workflows

---

# Technologies To Explore

## LLM
- [ ] Ollama
- [ ] Qwen
- [ ] GLM
- [ ] Llama
- [ ] Hosted APIs

## Backend
- [ ] FastAPI
- [ ] Docker
- [ ] Async processing

## RAG
- [ ] Embeddings
- [ ] Vector databases
- [ ] Reranking
- [ ] Hybrid retrieval

## AI Frameworks
- [ ] LlamaIndex
- [ ] LangChain
- [ ] LangGraph

## Evaluation
- [ ] RAGAS
- [ ] LLM evaluation
- [ ] Custom benchmarks
