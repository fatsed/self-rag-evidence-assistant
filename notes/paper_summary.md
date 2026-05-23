# Self-RAG Paper Summary

## Paper Title

**Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**

## Main Idea

Self-RAG is a framework designed to improve the factuality and quality of language model responses.

Traditional language models usually generate answers using only their internal knowledge. This can lead to hallucination or unsupported answers. Traditional RAG improves this by retrieving external documents before generating an answer.

Self-RAG goes one step further. It allows the model to decide when retrieval is needed, use retrieved passages, generate an answer, and then critique its own output.

## Why Self-RAG Is Important

The main problem Self-RAG tries to solve is that language models can generate confident but incorrect answers.

Traditional RAG helps by adding external information, but it usually retrieves documents in a fixed way. Sometimes retrieval is unnecessary, and sometimes the retrieved passages are not useful.

Self-RAG introduces a more flexible and reflective approach.

## Main Components

Self-RAG combines three main actions:

1. **Retrieval**  
   The model retrieves external information when it is useful.

2. **Generation**  
   The model generates an answer using the retrieved evidence.

3. **Critique**  
   The model checks whether the retrieved evidence is relevant and whether the generated answer is supported.

## Reflection Tokens

A key idea in Self-RAG is the use of reflection tokens.

These tokens help the model decide:

- whether retrieval is needed
- whether the retrieved passage is relevant
- whether the generated answer is supported
- whether the answer is useful

In the original paper, these reflection tokens are learned during training.

## Difference from Traditional RAG

Traditional RAG usually follows this process:

```text
User question
↓
Retrieve documents
↓
Generate answer
```

Self-RAG follows a more reflective process:

```text
User question
↓
Decide if retrieval is needed
↓
Retrieve relevant passages
↓
Generate answer
↓
Critique the evidence and answer
↓
Select or improve the final response
```

## How This Project Uses the Paper Idea

This project is not a full reproduction of the Self-RAG paper.

Instead, it implements a simplified version of the main idea:

- uploaded documents are used as the knowledge source
- embedding-based retrieval finds relevant chunks
- Groq API generates an answer
- structured critique checks evidence relevance, support level, and usefulness

The goal is to understand the main Self-RAG workflow in a practical way.

## Summary

Self-RAG improves traditional retrieval-augmented generation by adding reflection and critique.

Instead of only retrieving documents and generating an answer, Self-RAG also checks whether the retrieved evidence is useful and whether the generated answer is supported.

This makes the model more reliable and reduces unsupported or hallucinated responses.