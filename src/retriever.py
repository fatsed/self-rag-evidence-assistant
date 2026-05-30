import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.embedder import create_embeddings

def label_evidence(score):
    """
    Add a simple relevance label to each retrieved evidence chunk.
    This is a simplified Self-RAG-style reflection step.
    """
    if score >= 0.45:
        return "Relevant"
    if score >= 0.25:
        return "Partially relevant"
    return "Weak evidence"

def retrieve_relevant_chunks(question, chunks, top_k=3, min_score=0.25):
    """
    find the most relevant chunks for the user question.
    only keep chunks with similarity score above min_score.
    """
    if not chunks:
        return []

    chunk_texts = [chunk["text"] for chunk in chunks]

    question_embedding = create_embeddings([question])
    chunk_embeddings = create_embeddings(chunk_texts)

    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1]

    results = []

    for index in top_indices:
        score = float(similarities[index])
        if score < min_score:
            continue
        chunk = chunks[index]
        results.append(
            {
                "file_name": chunk["file_name"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "score": score,
                "evidence_label": label_evidence(score),
            }
        )
        if len(results) == top_k:
            break

    return results