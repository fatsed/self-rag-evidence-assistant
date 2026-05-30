# Example Output

This file shows a sample output from the Self-RAG Evidence Assistant.

## Example Question

What is critique in Self-RAG?

## Generated Answer

In Self-RAG, critique is used to evaluate whether the generated answer is supported by the retrieved evidence. It helps the system check the relevance of the evidence and the support level of the answer.

## Retrieved Evidence

### Evidence 1

**Source:** self-rag-paper.pdf  
**Chunk:** 6  
**Score:** 0.623

The retrieved passage explains that Self-RAG uses reflection tokens to decide when retrieval is needed and to critique whether the generated output is supported by evidence.

### Evidence 2

**Source:** self-rag-paper.pdf  
**Chunk:** 38  
**Score:** 0.586

The retrieved passage describes how critique tokens help evaluate generated responses using retrieved passages.

## Critique

**Evidence relevance:** Relevant  
**Support level:** Fully supported  
**Usefulness:** 5/5  
**Warning:** No warning.  
**Reason:** The answer is supported by the retrieved evidence.

## Reflection Summary

**Retrieval decision:** Retrieve  
**Retrieved chunks:** 3  
**Best evidence score:** 0.623  
**Evidence quality:** Strong evidence  
**Retrieval reason:** The answer should be grounded in the uploaded documents.