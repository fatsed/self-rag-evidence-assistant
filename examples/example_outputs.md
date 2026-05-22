# Example Outputs

This file shows sample outputs from the Self-RAG Evidence Assistant.

The examples demonstrate how the assistant retrieves evidence, generates an answer, and critiques whether the answer is supported by the retrieved evidence.

---

## Example 1 — Supported Answer

### Question

```text
How does Self-RAG evaluate generated answers?
```

### Answer

```text
Self-RAG evaluates generated answers by checking whether the retrieved evidence is relevant and whether the generated answer is supported by that evidence. It uses critique-style evaluation to review the quality and usefulness of the response.
```

### Retrieved Evidence

```text
Source: self-rag-paper.pdf
Chunk: 3
Score: 0.635

The retrieved passage explains that Self-RAG reflects on retrieved passages and generated outputs, and uses critique tokens to evaluate relevance, support, and usefulness.
```

### Critique

```text
Evidence relevance: Fully relevant
Support level: Fully supported
Usefulness: 5/5
Warning: No warning.
Reason: The answer is directly supported by the retrieved evidence.
```

---

## Example 2 — Unsupported Question

### Question

```text
What is the capital of Japan?
```

### Answer

```text
The provided evidence is not sufficient to answer this question.
```

### Retrieved Evidence

```text
No evidence found.
```

### Critique

```text
Evidence relevance: Irrelevant
Support level: Not supported
Usefulness: 1/5
Warning: No direct evidence found.
Reason: The uploaded documents do not provide evidence for answering this question.
```