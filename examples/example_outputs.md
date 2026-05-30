# Example Outputs

This file shows sample outputs from the Self-RAG Evidence Assistant.

The examples show how the app retrieves evidence, critiques the evidence, generates an answer, critiques the answer, revises the answer if needed, and shows a reflection summary.

---

## Example 1 — Supported Answer

### Question

```text
What is critique in Self-RAG?
```

### Final Answer

```text
In Self-RAG, critique is used to evaluate whether the generated answer is supported by the retrieved evidence. It helps the system check the relevance of the evidence, the support level of the answer, and the usefulness of the response.
```

### Retrieved Evidence

```text
Evidence 1
Source: self-rag-paper.pdf
Chunk: 6
Score: 0.635
Label: Relevant
Reason: This evidence directly explains how Self-RAG critiques generated answers using retrieved passages.

Evidence 2
Source: self-rag-paper.pdf
Chunk: 12
Score: 0.574
Label: Relevant
Reason: This evidence is useful because it describes reflection and support checking in Self-RAG.

Evidence 3
Source: self-rag-paper.pdf
Chunk: 21
Score: 0.421
Label: Partially relevant
Reason: This evidence is related to Self-RAG but does not fully explain critique.
```

### Answer Critique

```text
Evidence relevance: Relevant
Support level: Fully supported
Usefulness: 5/5
Warning: No warning.
Reason: The answer is supported by the retrieved evidence.
```

### Reflection Summary

```text
Retrieval decision: Retrieve
Retrieved chunks: 3
Best evidence score: 0.635
Evidence quality: Strong evidence

Relevant evidence: 2
Partially relevant evidence: 1
Weak evidence: 0

Support level: Fully supported
Warning: No warning.
```

---

## Example 2 — Unsupported Question

### Question

```text
What are the main limitations of Self-RAG?
```

### Final Answer

```text
The retrieved evidence is not sufficient to answer this question.
```

### Retrieved Evidence

```text
Evidence 1
Source: self-rag-paper.pdf
Chunk: 4
Score: 0.486
Label: Partially relevant
Reason: This evidence is related to Self-RAG but does not directly describe the main limitations.

Evidence 2
Source: self-rag-paper.pdf
Chunk: 17
Score: 0.412
Label: Partially relevant
Reason: This evidence discusses the method but does not provide enough information about limitations.

Evidence 3
Source: self-rag-paper.pdf
Chunk: 30
Score: 0.276
Label: Irrelevant
Reason: This evidence does not help answer the question about the limitations of Self-RAG.
```

### Answer Critique

```text
Evidence relevance: Partially relevant
Support level: Not supported
Usefulness: 1/5
Warning: No direct evidence found.
Reason: The retrieved evidence does not provide enough support to answer the question.
```

### Reflection Summary

```text
Retrieval decision: Retrieve
Retrieved chunks: 3
Best evidence score: 0.486
Evidence quality: Partial evidence

Relevant evidence: 0
Partially relevant evidence: 2
Weak evidence: 1

Support level: Not supported
Warning: No direct evidence found.
```

---

## Example 3 — No Retrieval Needed

### Question

```text
hello
```

### Final Answer

```text
The system could not perform retrieval for this question.
```

### Retrieved Evidence

```text
No evidence was retrieved.
```

### Answer Critique

```text
Evidence relevance: Irrelevant
Support level: Not supported
Usefulness: 1/5
Warning: Retrieval was not performed.
Reason: The question is conversational and does not need document retrieval.
```

### Reflection Summary

```text
Retrieval decision: No retrieval
Retrieved chunks: 0
Best evidence score: 0.000
Evidence quality: No evidence

Relevant evidence: 0
Partially relevant evidence: 0
Weak evidence: 0

Support level: Not supported
Warning: Retrieval was not performed.
```
