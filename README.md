# Self-RAG Evidence Assistant 🧠📄

A simple document-based assistant inspired by the Self-RAG paper.

The goal of this project is to answer questions using evidence from local documents, then check whether the answer is actually supported by that evidence.

This is not a full implementation of the original Self-RAG model. It is a smaller educational project that tries to simulate the main idea in a simple and practical way.

## Project Idea 💡
Traditional RAG systems usually retrieve documents first and then generate an answer based on those documents.
Self-RAG adds a more reflective step. Instead of always retrieving information, the model can first decide whether retrieval is needed. After generating an answer, it can also check the quality of the evidence and whether the answer is supported.
This project follows that idea in a lightweight way.

## How It Works ⚙️
The assistant follows this pipeline:
```text
User Question
     ↓
Decide if retrieval is needed
     ↓
Retrieve relevant document chunks
     ↓
Generate an answer using the evidence
     ↓
Critique the answer
     ↓
Show the final answer, evidence, and critique result
```
## Demo 🖼️

![Demo](assets/demo.png)

## Main Features ✅
- Load local text documents
- Ask a question about the documents
- Retrieve the most relevant text chunks
- Generate an answer using an LLM API
- Check if the retrieved evidence is relevant
- Check if the answer is supported by the evidence
- Give a simple usefulness score
- Warn the user when the answer is not supported by the evidence


## Self-RAG Inspired Components 🔍
| Self-RAG Concept | Simplified Version in This Project |
|---|---|
| Retrieval | Search local documents for relevant chunks |
| Retrieval Token | Decide whether retrieval is needed |
| Critique Token | Check relevance, support, and usefulness |
| Reflection | Ask the model to review its own answer |
| Evidence-based generation | Generate answers using retrieved text |


## Project Structure 📁
```text
self-rag-evidence-assistant/
│
├── README.md
├── requirements.txt
├── .env.example
├── app.py
│
├── documents/
│   └── self_rag_notes.txt
│
├── src/
│   ├── retriever.py
│   ├── generator.py
│   ├── critic.py
│   └── pipeline.py
│
└── examples/
    └── example_outputs.md
```


## Example Output 🧪
```text
Question:
What is the main idea of Self-RAG?

Answer:
Self-RAG is a retrieval-augmented generation framework that allows a language model to retrieve information only when needed and critique its own generated response.

Evidence:
"SELF-RAG adaptively retrieves passages on-demand and reflects on retrieved passages and its own generations."

Critique:
Retrieval needed: Yes
Evidence relevance: Relevant
Support level: Fully supported
Usefulness: 5/5
```


## Tech Stack 🛠️
- Python
- OpenAI API
- Local text documents
- Simple keyword-based retrieval


## Why I Built This ✨
I built this project to better understand how Self-RAG works and how retrieval, generation, and critique can be combined in one workflow.

Instead of only reading the paper, I wanted to turn the main idea into a small working project.


## Important Note ⚠️
This project is not a reproduction of the full Self-RAG paper.
The original Self-RAG framework trains a language model to generate reflection tokens during generation. This project uses an LLM API to simulate the main steps in a simpler way.


## Reference 📚

Paper: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection  
Official repository: https://github.com/akariasai/self-rag

## Status

Work in progress.
