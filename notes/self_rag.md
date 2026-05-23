# Self-RAG

## What Is Self-RAG?

Self-RAG stands for **Self-Reflective Retrieval-Augmented Generation**.

It is a framework that improves traditional RAG by adding reflection and critique to the generation process.

Instead of only retrieving documents and generating an answer, Self-RAG also evaluates the retrieved evidence and the generated response.
## Main Idea

The main idea of Self-RAG is that a language model should not always retrieve information blindly.

The model should be able to decide when retrieval is useful, use the retrieved passages, generate an answer, and then check whether the answer is supported by the evidence.

This makes the system more reliable and helps reduce unsupported answers.
## Self-RAG Pipeline

A simplified Self-RAG workflow looks like this:

```text
User question
↓
Decide whether retrieval is needed
↓
Retrieve relevant passages
↓
Generate an answer
↓
Critique the evidence and answer
↓
Produce the final response
```
## Reflection

Reflection means that the model reviews its own process and output.

In Self-RAG, reflection helps the model check:

- whether retrieval is needed
- whether the retrieved passage is relevant
- whether the generated answer is supported
- whether the answer is useful

This is the part that makes Self-RAG different from simple RAG.
## Critique

Critique means evaluating the quality of the retrieved evidence and the generated answer.

For example, the system can ask:

- Is this evidence relevant?
- Does this evidence support the answer?
- Is the answer useful for the user?

This critique step helps reduce hallucination and unsupported responses.
## How This Project Uses Self-RAG

This project uses Self-RAG ideas in a simplified way.

The project does not train a new language model. Instead, it uses a language model API to simulate the generation and critique steps.

The project includes:

- document upload
- evidence retrieval
- answer generation
- structured critique
- support level checking

This makes the project a practical version inspired by the Self-RAG workflow.
## Difference Between RAG and Self-RAG

Traditional RAG mainly retrieves documents and generates an answer.

Self-RAG adds a reflective step. It checks the retrieved evidence and the generated answer before producing the final response.

In short:

```text
Traditional RAG:
Retrieve → Generate

Self-RAG:
Retrieve → Generate → Critique
```
## Summary

Self-RAG is useful because it makes retrieval-augmented generation more controlled and evidence-aware.

It does not only generate an answer. It also checks whether the answer is supported by the retrieved evidence.

This idea is the main inspiration for the Self-RAG Evidence Assistant project.