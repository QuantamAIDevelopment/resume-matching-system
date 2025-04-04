# resume-matching-system

## 📌 Project Description

This project provides an API-first, AI-powered resume matching system designed to automate resume screening and candidate-job relevance scoring using cutting-edge technologies. The system combines microservices architecture, Large Language Models (LLMs), and vector databases to deliver enterprise-ready resume matching for HR teams, staffing agencies, and career platforms.

It uses a modular, agent-based orchestration flow where each component performs a specialized task — from resume parsing, embedding generation, and job description comprehension to final matching and scoring. It supports both local and scalable deployment options including Docker and Azure Kubernetes Service (AKS).

## ✅ Features

- **Resume Upload & Parsing:** Accepts resumes in PDF/DOCX format and extracts structured content using LLMs and traditional NLP.
- **Job Description Ingestion:** Handles job creation with automatic semantic embedding generation.
- **Resume Matching:** Uses cosine similarity with FAISS on vector embeddings for intelligent scoring and ranking.
- **Agent Workflow Engine:** Orchestrates tasks through CrewAI agents.
- **API-First Design:** RESTful APIs using FastAPI with OpenAPI docs.
- **Cloud & DevOps Ready:** Built for containerization, logging, and production-grade monitoring.

---

## 🧰 Tech Stack

### 🚀 Core Backend & Services
| Layer | Technology | Purpose |
|-------|------------|---------|
| Microservices Framework | **FastAPI** | Lightweight, high-performance Python API |
| Agent Orchestration | **CrewAI + LangChain** | Multi-agent coordination and prompt chaining |
| Parsing & NLP | **pdfplumber, python-docx, spaCy, GPT-4** | Extracts structured info from resumes & job descriptions |
| Embedding & Matching | **SentenceTransformers + FAISS** | Semantic embedding & similarity ranking |
| Internal Event System | **Custom Pub/Sub** | Triggers agents across services (can scale to Redis/Kafka) |
| ML Scoring | **Scikit-learn** | Optional ranking models for advanced scoring logic |

### 📦 Infrastructure & DevOps
| Component | Technology |
|----------|------------|
| Containerization | **Docker** |
| Local Orchestration | **Docker Compose** |
| Cloud Deployment (Planned) | **Azure Kubernetes Service (AKS)** |
| Configuration Management | `.env`, `settings.py`, `Makefile` |
| Observability (Planned) | Azure Monitor, ELK stack-ready architecture |

### 🧪 Testing
| Type | Tool |
|------|------|
| Unit Tests | **pytest** |
| API/Integration Tests | **pytest + httpx** |
| End-to-End Tests | Custom workflows with real resumes & JDs |

### 🧠 LLM & AI Integration
| Service | Purpose |
|---------|---------|
| **OpenAI GPT-4** | Contextual understanding of resumes and JDs |
| **LangChain** | Manages prompt flows and agent memory |
| **FAISS** | Vector search & semantic similarity engine |
| **Jinja2** | Dynamic prompt templating for flexible input/output |

### 📚 Documentation & Developer Tools
| Tool | Purpose |
|------|--------|
| **Swagger (via FastAPI)** | Auto-generated REST API docs |
| **Markdown + YAML** | Internal schema and configuration docs |
| **VS Code** | Dev IDE with FastAPI/LLM extensions recommended |
| **Makefile** | Developer automation for setup, testing, linting, etc. |
