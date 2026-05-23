# Self-RAG Evidence Assistant 🧠📄

A Streamlit-based multi-document question-answering assistant inspired by the Self-RAG paper.

This project allows users to upload multiple documents, ask questions, retrieve relevant evidence, generate an answer, and check whether the answer is supported by the retrieved evidence.

It is not a full implementation of the original Self-RAG model. Instead, it is a simplified practical project that applies the main ideas of retrieval, generation, and critique in an evidence-based QA workflow.

## Project Idea 💡

Traditional RAG systems usually retrieve documents and then generate an answer using the retrieved information.

Self-RAG adds a more reflective process. It introduces the idea of checking whether retrieval is needed, whether the retrieved evidence is relevant, and whether the generated answer is supported.

This project follows that idea in a simplified way. The assistant retrieves evidence from uploaded documents, generates an answer using a language model API, and then critiques the answer based on the retrieved evidence.

## How It Works ⚙️

The assistant follows this pipeline:

```text
Upload documents
     ↓
Extract text from PDF / TXT / DOCX files
     ↓
Split documents into chunks
     ↓
Create embeddings for the chunks
     ↓
Retrieve the most relevant evidence
     ↓
Generate an answer using Groq API
     ↓
Critique the answer using structured JSON output
     ↓
Show answer, evidence, support level, warning, and reason
```
## Demo 🖼️

![Demo](assets/demo.png)

## Main Features ✅

- Upload multiple documents
- Support PDF, TXT, and DOCX files
- Extract text from uploaded files
- Split long documents into smaller chunks
- Use embedding-based retrieval to find relevant evidence
- Apply a minimum evidence score threshold
- Generate answers using Groq API
- Critique answers using structured JSON output
- Show evidence relevance, support level, usefulness, warning, and reason
- Download the final result as a TXT file


## Self-RAG Inspired Components 🔍

| Self-RAG Concept | Simplified Version in This Project |
|---|---|
| Retrieval | Finds relevant chunks from uploaded documents |
| Retrieval Token | Simulated through the evidence score threshold |
| Critique Token | Structured critique with relevance, support, and usefulness |
| Reflection | The assistant checks whether the answer is grounded in evidence |
| Evidence-based generation | The answer is generated only from retrieved evidence |

## Study Notes 📝

I also added short notes to explain the main concepts behind this project:

- [Self-RAG Paper Summary](notes/paper_summary.md)
- [Traditional RAG](notes/traditional_rag.md)
- [Self-RAG](notes/self_rag.md)
- [Key Concepts](notes/key_concepts.md)

## Project Structure 📁

```text
self-rag-evidence-assistant/
│
├── README.md
├── requirements.txt
├── .env.example
├── app.py
│
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── file_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── generator.py
│   ├── critic.py
│   └── pipeline.py
│
└── examples/
    └── example_outputs.md
```

## Tech Stack 🛠️

- Python
- Streamlit
- Groq API
- Sentence Transformers
- Scikit-learn
- PyPDF
- python-docx
- NumPy

## Installation 🚀

Clone the repository:

```bash
git clone https://github.com/fatsed/self-rag-evidence-assistant.git
cd self-rag-evidence-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```
## Environment Variables 🔐

This project uses Groq API for answer generation and critique.

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

A sample file is provided as:
Do not upload your real `.env` file to GitHub.
```text
.env.example
```

## How to Run ▶️

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

The app allows you to:

1. Upload one or more PDF, TXT, or DOCX files
2. Ask a question about the uploaded documents
3. Retrieve relevant evidence
4. Generate an answer
5. Check whether the answer is supported by evidence



## Example Output 🧪

```text
Question:
What is critique in Self-RAG?

Answer:
Critique in Self-RAG is the process of evaluating the retrieved evidence and the generated answer. It helps check whether the evidence is relevant and whether the answer is supported by that evidence.

Retrieved Evidence:
Source: self-rag-paper.pdf
Chunk: 2
Score: 0.684

Critique:
Evidence relevance: Relevant
Support level: Fully supported
Usefulness: 5/5
Warning: No warning.
Reason: The answer is directly supported by the retrieved evidence.
```

## Important Note ⚠️

This project is not a full reproduction of the original Self-RAG paper.

The original Self-RAG framework trains a language model to generate reflection tokens during generation. This project is a smaller practical version that simulates the main workflow using document retrieval, answer generation, and structured critique.

The goal of this project is to understand and apply the main Self-RAG ideas in a simple document question-answering application.

## Why I Built This ✨

I built this project to better understand how RAG and Self-RAG work in practice.

Instead of only reading the paper, I wanted to turn the main idea into a working project where users can upload documents, ask questions, retrieve evidence, and check whether the answer is supported.


## Reference 📚

Paper: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection  
Official repository: https://github.com/akariasai/self-rag

## Status

Work in progress.
