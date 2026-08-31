# AI/ML Engineering Journey

A hands-on repository for learning, experimenting with, and building modern Artificial Intelligence systems — from Machine Learning and Deep Learning to Generative AI, Large Language Models, RAG, Vector Databases, AI Agents, and Agentic AI.

---

## About This Repository

This repository represents my journey into **AI/ML Engineering**.

The focus is on building a strong foundation in Artificial Intelligence while progressing toward modern AI application development. Concepts are studied from both theoretical and practical perspectives and reinforced through implementations, experiments, and real-world projects.

The repository covers the complete progression from traditional Machine Learning to modern **LLM-powered and agentic applications**.

The primary goal is to understand:

* What a technology or concept is
* Why it is needed
* How it works internally
* How to implement it
* Where it is useful
* What its limitations are
* How it can be used in real-world systems

---

## AI/ML Learning Path

```text
Python & Data Science
        │
        ▼
Mathematics for ML
        │
        ▼
Machine Learning
        │
        ▼
Deep Learning
        │
        ▼
Neural Networks & Transformers
        │
        ▼
Generative AI
        │
        ▼
Large Language Models
        │
        ▼
Embeddings & Semantic Search
        │
        ▼
RAG Systems
        │
        ▼
Vector Databases
        │
        ▼
AI Agents
        │
        ▼
Agentic AI
        │
        ▼
Production AI Systems
```

---

## Areas Covered

### Machine Learning

Core concepts and algorithms for building predictive and analytical systems.

Topics include:

* Supervised Learning
* Unsupervised Learning
* Regression
* Classification
* Clustering
* Dimensionality Reduction
* Feature Engineering
* Feature Selection
* Model Training
* Cross Validation
* Hyperparameter Optimization
* Model Evaluation
* Ensemble Learning
* Bias and Variance
* Overfitting and Underfitting

Algorithms explored include:

* Linear Regression
* Logistic Regression
* K-Nearest Neighbors
* Decision Trees
* Random Forest
* Support Vector Machines
* Naive Bayes
* K-Means
* DBSCAN
* PCA
* Gradient Boosting

---

### Deep Learning

Understanding neural networks and modern deep learning architectures.

Topics include:

* Artificial Neural Networks
* Perceptrons
* Activation Functions
* Forward Propagation
* Backpropagation
* Loss Functions
* Gradient Descent
* Optimizers
* Regularization
* Dropout
* Batch Normalization
* Convolutional Neural Networks
* Recurrent Neural Networks
* LSTM
* GRU
* Attention Mechanism
* Transformers

Frameworks include:

* PyTorch
* TensorFlow
* Keras

---

### Generative AI

Exploring how modern AI systems generate text, code, images, and other forms of content.

Topics include:

* Generative AI fundamentals
* Large Language Models
* Transformer Architecture
* Tokenization
* Attention
* Context Windows
* Prompt Engineering
* Structured Outputs
* Function Calling
* Tool Calling
* Embeddings
* Fine-Tuning
* Parameter-Efficient Fine-Tuning
* LLM Evaluation
* LLM Application Development

---

### Large Language Models

Understanding LLMs beyond simply calling an API.

Topics include:

* Transformer architecture
* Self-Attention
* Multi-Head Attention
* Positional Encoding
* Tokenization
* Embeddings
* Pre-training
* Fine-tuning
* Instruction tuning
* Inference
* Context windows
* Temperature
* Sampling
* Hallucination
* Model evaluation
* LLM limitations

---

### Retrieval-Augmented Generation

Building systems that combine information retrieval with Large Language Models.

```text
             ┌─────────────────┐
             │    Documents    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Document Loader │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │     Chunking    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Embeddings    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Vector Store   │
             └────────┬────────┘
                      │
                User Query
                      │
                      ▼
             ┌─────────────────┐
             │    Retrieval    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │      LLM        │
             └────────┬────────┘
                      │
                      ▼
                 Final Answer
```

Topics include:

* Document ingestion
* Document loaders
* Text splitting
* Chunking strategies
* Embedding models
* Vector search
* Similarity search
* Metadata filtering
* Hybrid search
* Re-ranking
* Query transformation
* Context optimization
* Conversational RAG
* Advanced RAG
* RAG evaluation

---

### Vector Databases

Understanding how vector representations are stored, indexed, and searched.

Technologies and concepts include:

* Vector embeddings
* Dense vectors
* Similarity search
* Cosine similarity
* Euclidean distance
* Approximate Nearest Neighbor Search
* Indexing
* Metadata filtering
* Vector retrieval

Tools explored include:

* FAISS
* ChromaDB
* Pinecone
* Weaviate

---

### AI Agents

Exploring AI systems that can reason about tasks, use tools, maintain state, and perform actions.

Topics include:

* AI Agent fundamentals
* LLM + Tools
* Function Calling
* Tool Calling
* Agent Loops
* Planning
* Reasoning
* ReAct
* Memory
* Reflection
* Human-in-the-loop
* Agent Workflows
* Multi-Agent Systems
* Agent Evaluation

---

### Agentic AI

Moving beyond simple LLM applications toward systems capable of executing multi-step tasks through autonomous or semi-autonomous workflows.

Topics include:

* Agent orchestration
* Planning and execution
* Stateful agents
* Long-term memory
* Tool ecosystems
* Multi-agent architectures
* Autonomous workflows
* Human-in-the-loop systems
* Agent communication
* Agent evaluation
* Guardrails
* MCP
* Production agent architectures

---

## Projects

The repository contains practical implementations ranging from foundational experiments to complete AI applications.

Projects may include:

### Machine Learning

* Regression systems
* Classification systems
* Recommendation systems
* Customer segmentation
* Prediction systems
* NLP classification

### Deep Learning

* Image classification
* Neural network implementations
* CNN projects
* NLP models
* Sequence models

### Generative AI

* LLM applications
* AI assistants
* Summarization systems
* Question-answering systems
* AI-powered developer tools

### RAG

* PDF Question Answering
* Document RAG
* Website RAG
* Knowledge Base Assistant
* Research Assistant
* Conversational RAG

### AI Agents

* Research Agent
* Coding Agent
* Data Analysis Agent
* Web Research Agent
* Tool-using AI Assistant

### Agentic AI

* Multi-Agent Research System
* Autonomous Research Workflow
* AI Development Workflow
* Multi-Agent Collaboration Systems
* End-to-End Agentic Applications

---

## Repository Structure

```text
ai-ml-engineering-journey/
│
├── 01-python-and-data-science/
│
├── 02-mathematics/
│
├── 03-machine-learning/
│   ├── regression/
│   ├── classification/
│   ├── clustering/
│   ├── dimensionality-reduction/
│   └── model-evaluation/
│
├── 04-deep-learning/
│   ├── neural-networks/
│   ├── cnn/
│   ├── rnn/
│   ├── lstm/
│   └── transformers/
│
├── 05-generative-ai/
│   ├── llms/
│   ├── prompt-engineering/
│   ├── embeddings/
│   └── fine-tuning/
│
├── 06-rag/
│   ├── basic-rag/
│   ├── advanced-rag/
│   └── rag-evaluation/
│
├── 07-vector-databases/
│   ├── faiss/
│   ├── chromadb/
│   ├── pinecone/
│   └── similarity-search/
│
├── 08-ai-agents/
│   ├── tool-calling/
│   ├── memory/
│   ├── single-agent/
│   └── multi-agent/
│
├── 09-agentic-ai/
│   ├── workflows/
│   ├── orchestration/
│   ├── mcp/
│   └── production-agents/
│
├── projects/
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── interview-preparation/
│   ├── machine-learning/
│   ├── deep-learning/
│   ├── generative-ai/
│   ├── rag/
│   └── ai-agents/
│
└── README.md
```

---

## Technology Stack

```text
Programming
├── Python
├── SQL
└── JavaScript

Data Science
├── NumPy
├── Pandas
└── Matplotlib

Machine Learning
└── Scikit-learn

Deep Learning
├── PyTorch
├── TensorFlow
└── Keras

Generative AI
├── Hugging Face
├── Transformers
├── LLM APIs
├── LangChain
└── LangGraph

RAG & Vector Search
├── FAISS
├── ChromaDB
├── Pinecone
└── Weaviate

AI Agents
├── LangGraph
├── Tool Calling
├── Function Calling
├── MCP
└── Multi-Agent Systems

Development & Deployment
├── Git
├── GitHub
├── Jupyter
├── VS Code
├── FastAPI
└── Docker
```

---

## Learning Approach

The repository follows a practical learning methodology:

```text
Learn
  ↓
Understand
  ↓
Implement
  ↓
Experiment
  ↓
Build
  ↓
Evaluate
  ↓
Document
```

For important concepts, the focus is on understanding both the **theory and implementation** rather than treating libraries as black boxes.

---

## AI Engineering Principles

While building projects, special attention is given to:

* Clean and maintainable code
* Reproducible experiments
* Model evaluation
* Data quality
* Prompt reliability
* Retrieval quality
* Hallucination reduction
* Security
* Scalability
* Observability
* Cost optimization
* Production readiness

---

## Interview Preparation

This repository also serves as a technical reference for AI/ML interviews.

Important areas include:

* Python
* Data Structures and Algorithms
* SQL
* Machine Learning
* Deep Learning
* Neural Networks
* Transformers
* LLMs
* Embeddings
* RAG
* Vector Databases
* AI Agents
* Agentic AI
* AI System Design

The objective is to develop the ability to explain:

> **What it is → Why it is needed → How it works → How to implement it → When to use it → What trade-offs it has**

---

## Projects Over Theory

The ultimate goal of this repository is not to collect notes.

It is to progressively transform concepts into **working software and real-world AI systems**.

Each project is intended to demonstrate practical understanding through:

* Problem definition
* Architecture
* Implementation
* Evaluation
* Experiments
* Documentation
* Improvements

---

## Disclaimer

This repository is a personal learning and experimentation space. Implementations, experiments, and project architectures may evolve as my understanding of AI/ML engineering develops.

---

⭐ **Learning AI. Building systems. Understanding the technology behind them.**
