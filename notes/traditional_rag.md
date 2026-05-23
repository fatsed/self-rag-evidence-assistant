# Traditional RAG

## What Is Traditional RAG?

Traditional RAG stands for **Retrieval-Augmented Generation**.

It is a method that combines a language model with a retrieval system. Instead of answering only from the model's internal knowledge, the system first retrieves relevant information from external documents and then uses that information to generate an answer.

# Traditional RAG

## What Is Traditional RAG?

Traditional RAG stands for **Retrieval-Augmented Generation**.

It is a method that combines a language model with a retrieval system. Instead of answering only from the model's internal knowledge, the system first retrieves relevant information from external documents and then uses that information to generate an answer.

## Traditional RAG Pipeline

A simple RAG system usually follows this process:

```text
User question
↓
Retrieve relevant documents
↓
Pass retrieved documents to the language model
↓
Generate final answer
```
## Main Limitation of Traditional RAG

Traditional RAG usually retrieves documents in a fixed way.

This means retrieval often happens every time, even when the question may not need external information.

Another limitation is that the retrieved documents may not always be relevant. If irrelevant or weak evidence is given to the language model, the final answer may become less useful or less accurate.

## Traditional RAG vs. Self-RAG

The main difference is that traditional RAG mainly focuses on retrieving documents and generating an answer.

Self-RAG adds more control and reflection. It can check whether retrieval is needed, whether the retrieved evidence is useful, and whether the generated answer is supported.

In simple words:

```text
Traditional RAG = Retrieve + Generate

Self-RAG = Retrieve + Generate + Critique
```

## How This Project Uses RAG

This project uses the basic RAG idea by retrieving relevant chunks from uploaded documents before generating an answer.

The retrieved chunks are used as evidence for the answer.

However, the project also adds a Self-RAG-inspired critique step to check whether the answer is supported by the retrieved evidence.