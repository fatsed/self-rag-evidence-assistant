# Key Concepts in Self-RAG

This file explains the main concepts used in the Self-RAG paper and in this project.

The goal is to understand the basic meaning of each concept in a simple way.

## Retrieval

Retrieval means finding relevant information from an external source.

In a RAG system, the model does not answer only from its internal knowledge. It first searches documents, passages, or chunks to find useful evidence.

In this project, retrieval means searching the uploaded files and finding the most relevant text chunks for the user's question.

## Generation

Generation means producing an answer.

After relevant evidence is retrieved, the language model uses that evidence to generate a response.

In this project, the answer is generated using the retrieved chunks, and the model is instructed not to use outside knowledge.

## Critique

Critique means checking the quality of the retrieved evidence and the generated answer.

In Self-RAG, critique helps the model decide whether the evidence is relevant, whether the answer is supported, and whether the response is useful.

In this project, critique is shown as structured output with:

- evidence relevance
- support level
- usefulness
- warning
- reason

## Reflection

Reflection means that the model reviews its own output or decision.

In Self-RAG, reflection is used to make the model more careful about retrieval and generation.

Instead of only producing an answer, the model also checks whether its answer is grounded in evidence.

## Retrieval Token

A retrieval token is used in the original Self-RAG paper to help the model decide whether external information should be retrieved.

In this project, there is no real trained retrieval token.

Instead, the project simulates this idea using retrieval logic and a minimum evidence score threshold.

## Critique Token

A critique token is used in the original Self-RAG paper to evaluate the retrieved evidence and generated output.

It can help judge things like:

- whether the retrieved passage is relevant
- whether the answer is supported
- whether the answer is useful

In this project, this idea is simulated through the structured critique step.

## Evidence Relevance

Evidence relevance means checking whether the retrieved text is actually related to the user's question.

If the evidence is not related to the question, the answer should not rely on it.

In this project, evidence relevance is shown in the critique section of the app.

## Support Level

Support level means checking whether the answer is supported by the retrieved evidence.

The answer can be:

- fully supported
- partially supported
- not supported

This helps the system avoid unsupported or hallucinated answers.

## Usefulness

Usefulness means checking whether the answer is helpful for the user's question.

An answer may be supported by evidence, but it should also be clear and useful.

In this project, usefulness is shown as a score from 1/5 to 5/5.

## Evidence Score Threshold

The evidence score threshold is a minimum similarity score used to decide whether a retrieved chunk is strong enough.

If the score is too low, the chunk is ignored.

This helps the system avoid using weak or unrelated evidence.

## Summary

The main idea of Self-RAG is not only to generate answers, but also to check the quality of retrieval and the support level of the generated answer.

This project uses these ideas in a simplified way by combining:

- document retrieval
- evidence-based answer generation
- structured critique
- support checking