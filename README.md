# 🚀 LangChain & LangGraph Masterclass

A comprehensive, hands-on repository designed to take you from foundational LLM concepts to architecting production-ready **AI Agents** and **Multi-Agent Systems**.

**Maintained by:** [Dev Savaj](https://github.com/devsavaj) | *Gen AI Engineer intern @ Ascendion*

---

## 📚 Learning Path

This masterclass is structured to provide a deep dive into the modern AI ecosystem:

* **LangChain Fundamentals:** Mastering Chains, Prompts, and Output Parsers.
* **Advanced RAG Systems:** Implementing Retrieval Augmented Generation with complex query expansion and reranking.
* **AI Agents:** Building autonomous entities capable of tool-use and reasoning.
* **LangGraph Workflows:** Orchestrating stateful, multi-actor applications with cyclic graphs.
* **Multi-Agent Systems:** Coordinating specialized agents for collaborative task completion.
* **Production Deployment:** Wrapping models with FastAPI and monitoring performance.

---

## 🛠 Tech Stack

| Category | Tools |
| :--- | :--- |
| **Frameworks** | LangChain, LangGraph |
| **Languages** | Python 3.10+ |
| **Models** | OpenAI (GPT-4o), Anthropic, Open Source (Ollama/Groq) |
| **API & Backend** | FastAPI, Pydantic |
| **Vector Stores** | Pinecone, ChromaDB, FAISS |

---

## 📂 Project Structure

```text
.
├── 01_Fundamentals/       # Basic Chains and Prompt Engineering
├── 02_RAG_Deep_Dive/      # Vector Databases and Document Loaders
├── 03_Agents/             # Tool-calling and ReAct logic
├── 04_LangGraph/          # State management and cyclic graphs
├── 05_Multi_Agent/        # Supervisor and Hierarchical patterns
├── projects/              # Full-scale applications
│   ├── chat_with_pdf/     # PDF ingestion + RAG
│   ├── research_asst/     # Autonomous web-search agent
│   └── multi_agent_team/  # Collaborative coding/writing team
└── requirements.txt       # Environment dependencies
