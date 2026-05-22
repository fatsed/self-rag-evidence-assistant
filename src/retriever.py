import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.embedder import create_embeddings

def retrieve_relevant_chunks(question, chunks, top_k = 3):
    """
    find the most relevant chunks for the user question.
    """
    if not chunks:
        return []

    chunks_texts = [chunk['text'] for chunk in chunks]

    question_embeddings = create_embeddings([question])
    chunk_embeddings = create_embeddings(chunks_texts)
    #The similarity between the question and each chunk is calculated.
    #[0.82, 0.31, 0.67, 0.12]
    similarities = cosine_similarity(question_embeddings, chunk_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for index in top_indices:
        chunk = chunks[index]

        results.append(
            {
                "file_name": chunk["file_name"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "score": float(similarities[index]),
            }
        )

    return results