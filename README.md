# JustiBot — Generative AI Law Chatbot for Indian Judicial Advice

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-orange.svg)](https://openai.com)
[![IEEE](https://img.shields.io/badge/Published-IEEE%20IATMSI-red.svg)](https://ieee.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Research paper published at **IEEE IATMSI International Conference** — *"Generative vs Intent-Based Chatbot for Judicial Advice"*

---

## Overview

JustiBot is a Generative AI-powered legal chatbot designed to provide context-aware judicial advice based on **Indian Penal Code (IPC)** and constitutional law. It was built as part of a comparative research study exploring two distinct approaches to legal AI:

- **Generative Chatbot** — powered by OpenAI GPT-3.5-Turbo with a RAG pipeline
- **Intent-Based Chatbot** — rule-driven, intent-classification approach

The study compares both approaches across five dimensions: nature of responses, response quality, handling of evolving legal scenarios, training and data requirements, and overall user experience — all in the context of Indian law.

---

## Research Publication

This project was presented at the **IEEE IATMSI International Conference**.

**Paper Title:** *Generative vs Intent-Based Chatbot for Judicial Advice*

**Key Finding:** The generative RAG-based approach outperformed the intent-based chatbot in handling complex, multi-turn legal queries and changing legal scenarios, while the intent-based approach demonstrated advantages in response consistency and lower computational requirements.

---

## Architecture
User Query
│
▼
LangChain Conversation Buffer Memory (session context)
│
▼
RAG Pipeline
├── FAISS Vector Database (10,000+ judicial conversations indexed)
├── Semantic Similarity Search
└── Context Retrieval
│
▼
GPT-3.5-Turbo (16K context window)
├── Custom Prompt Engineering
└── IPC + Constitutional Law grounding
│
▼
Streamlit UI (real-time multi-turn conversation)

---

## Key Features

- **RAG Pipeline** — Retrieval-Augmented Generation using FAISS vector database indexed on 10,000+ Indian judicial conversations
- **Hallucination Reduction** — Custom prompt engineering reduces hallucination rate by ~40% over baseline
- **High Retrieval Accuracy** — Achieves 98.4% Relevance@K on a manually curated 200-query Indian legal domain test set validated against IPC ground-truth answers
- **Multi-turn Conversations** — Full session-level context retention via LangChain Conversation Buffer Memory
- **Indian Law Grounding** — Responses grounded specifically in IPC and Indian constitutional law
- **Cloud-Ready Architecture** — Designed for deployment via Azure OpenAI Service endpoints

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.10+ |
| LLM | OpenAI GPT-3.5-Turbo (16K context window) |
| Framework | LangChain |
| Vector Database | FAISS |
| UI | Streamlit |
| Methodology | RAG, Prompt Engineering |
| Embeddings | Hugging Face Transformers |
| Cloud | Azure OpenAI Service |
| Data Processing | Pandas, NumPy |

---

## Evaluation Results

| Metric | Generative — JustiBot | Intent-Based |
|--------|----------------------|--------------|
| Relevance@K | **98.4%** | 74.2% |
| Hallucination Rate | **~40% lower** than baseline | N/A |
| Multi-turn Handling | Excellent | Limited |
| Changing Scenarios | Adapts dynamically | Rigid |
| Training Data Required | 10,000+ conversations | 500+ intents |
| Response Quality | High, contextual | Consistent, templated |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Sarang-Zanwar/Justibot--Generative-AI-Law-Chatbot-
cd Justibot--Generative-AI-Law-Chatbot-

# Create virtual environment
python -m venv venv
source venv/bin/activate
# On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Running the Application

```bash
streamlit run app.py

```
## Project Structure
JustiBot/
├── app.py                  # Main Streamlit application
├── rag_pipeline.py         # RAG pipeline with FAISS
├── prompt_templates.py     # Custom prompt engineering
├── data/
│   └── judicial_corpus/    # Indian judicial conversations dataset
├── vectorstore/
│   └── faiss_index/        # Pre-built FAISS index
├── requirements.txt
├── .env.example
└── README.md

---

## Comparative Study — Generative vs Intent-Based

The core research question this project addresses:

> *Which approach — generative AI or intent-based classification — is better suited for providing judicial advice to Indian users?*

**Generative Approach excels at:**
- Handling nuanced, multi-part legal queries
- Adapting to new or evolving legal scenarios without retraining
- Providing contextually rich, conversational responses
- Explaining complex IPC sections in plain language

**Intent-Based Approach excels at:**
- Consistent, predictable responses for common queries
- Lower computational cost and latency
- No dependency on external LLM APIs
- Better performance on narrow, well-defined legal question types

---


## Requirements
openai>=1.0.0
langchain>=0.1.0
faiss-cpu>=1.7.4
streamlit>=1.28.0
python-dotenv>=1.0.0
huggingface-hub>=0.19.0
sentence-transformers>=2.2.2
pandas>=2.0.0
numpy>=1.24.0

---


## Author

**Sarang Zanwar**
- GitHub: [@Sarang-Zanwar](https://github.com/Sarang-Zanwar)
- LinkedIn: [sarang-zanwar](https://www.linkedin.com/in/sarang-zanwar)
- Email: sarangzanwar@gmail.com

---
