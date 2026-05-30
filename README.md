# Self-RAG Evidence Assistant

A simple Streamlit app inspired by the Self-RAG paper.

In this project, the user can upload documents, ask a question, and get an answer based on the retrieved evidence. The app also checks whether the answer is supported by the evidence.

This is not a full implementation of the original Self-RAG model. I did not train a new language model. Instead, I used the main ideas of Self-RAG in a smaller runtime workflow: retrieval decision, evidence critique, answer critique, answer revision, and reflection.

---

## Project Idea

Traditional RAG systems usually retrieve relevant text and then generate an answer from it.

Self-RAG adds a more reflective process. It does not only generate an answer, but also checks whether retrieval is needed, whether the retrieved evidence is useful, and whether the answer is supported by the evidence.

I used this idea in a simplified way. In this project, the app retrieves relevant chunks from uploaded documents, evaluates the evidence, generates an answer, critiques the answer, and revises the answer if the critique shows that it is not fully supported.

---

## How the App Works

The app follows this process:

```text
Upload documents
↓
Extract text from PDF, TXT, or DOCX files
↓
Split the text into chunks
↓
Create embeddings
↓
Decide whether retrieval is needed
↓
Retrieve the most relevant chunks
↓
Critique each evidence chunk using the language model
↓
Generate an answer using the retrieved evidence
↓
Critique whether the answer is supported
↓
Revise the answer if needed
↓
Critique the final answer again
↓
Show the answer, evidence, critique, and reflection summary
```

---

## Demo

Here is a screenshot of the app after uploading the Self-RAG paper and asking a question.

![Demo screenshot](assets/demo.png)

---

## Features

* Upload PDF, TXT, and DOCX files
* Ask questions about uploaded documents
* Retrieve relevant evidence chunks
* Decide whether retrieval is needed for the question
* Critique each retrieved evidence chunk using the language model
* Label evidence as Relevant, Partially relevant, or Irrelevant
* Generate an answer using Groq API
* Check whether the answer is supported by the retrieved evidence
* Revise the answer if it is not fully supported
* Show critique results and warning messages
* Show a Self-RAG-style reflection summary
* Show evidence quality based on evidence labels
* Download the result as a TXT file

---

## Self-RAG Ideas Used in This Project

| Self-RAG idea | How I used it in this project |
|---|---|
| Retrieval decision | The app decides whether document retrieval is needed |
| Retrieval | The app finds relevant chunks from uploaded documents |
| Evidence critique | Retrieved chunks are evaluated as Relevant, Partially relevant, or Irrelevant |
| Answer generation | The answer is generated using only the retrieved evidence |
| Answer critique | The app checks whether the answer is supported by the evidence |
| Answer revision | If the answer is not fully supported, the app revises it using the evidence |
| Reflection | The app summarizes retrieval decision, evidence quality, support level, and warnings |

---

## Project Structure

```text
self-rag-evidence-assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
│
├── src/
│   ├── file_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── evidence_critic.py
│   ├── generator.py
│   ├── critic.py
│   ├── reviser.py
│   ├── reflection.py
│   └── pipeline.py
│
├── examples/
│   └── example_outputs.md
│
├── notes/
│   ├── paper_summary.md
│   ├── traditional_rag.md
│   ├── self_rag.md
│   └── key_concepts.md
│
└── assets/
    └── demo.png
```

---

## Tech Stack

* Python
* Streamlit
* Groq API
* Sentence Transformers
* Scikit-learn
* PyPDF
* python-docx
* NumPy
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/fatsed/self-rag-evidence-assistant.git
cd self-rag-evidence-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

This project uses Groq API for answer generation, evidence critique, answer critique, and answer revision.

Create a `.env` file in the project folder and add your API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

There is also a sample file:

```text
.env.example
```

---

## How to Run

Run the app with:

```bash
streamlit run app.py
```

Then open the local link shown in the terminal.

---

## Example Output

A sample output is available in:

```text
examples/example_outputs.md
```

It includes a sample question, generated answer, retrieved evidence, critique result, and reflection summary.

---

## Notes

I also added short notes while studying the paper:

* [Self-RAG Paper Summary](notes/paper_summary.md)
* [Traditional RAG](notes/traditional_rag.md)
* [Self-RAG](notes/self_rag.md)
* [Key Concepts](notes/key_concepts.md)

---

## Important Note

This project is not a full reproduction of the Self-RAG paper.

The original Self-RAG method trains a language model to generate reflection tokens during generation. My project does not train a new model. Instead, it simulates the main Self-RAG workflow at runtime using separate steps for retrieval decision, evidence critique, answer critique, answer revision, and reflection.

Because of that, this project should be understood as a Self-RAG-inspired assistant, not an exact implementation of the original paper.

---

## Why I Built This

I built this project because I wanted to understand Self-RAG better by turning the idea into a small working app.

Instead of only reading the paper, I wanted to make something practical where I could upload documents, ask questions, retrieve evidence, check the evidence, and see whether the answer is actually supported.

---

## Reference

Paper: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection  
Official repository: https://github.com/akariasai/self-rag

---

## Status

MVP completed.

The current version includes document upload, retrieval, LLM-based evidence critique, answer generation, answer critique, answer revision, and reflection summary.

Future improvements may include deployment, better retrieval settings, more evaluation options, and a small dataset for testing the evidence critique step.