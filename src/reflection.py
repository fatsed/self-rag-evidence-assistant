def decide_retrieval_need(question, uploaded_files):
    """
    Decide whether document retrieval should be used.

    This is a simplified Self-RAG-style decision step.
    In the original Self-RAG paper, the model learns when retrieval is needed.
    In this project, retrieval is needed when the user uploads documents
    and asks a valid question.
    """
    if not uploaded_files:
        return {
            "needed": False,
            "reason": "No documents were uploaded.",
        }

    if not question.strip():
        return {
            "needed": False,
            "reason": "No question was provided.",
        }

    return {
        "needed": True,
        "reason": "The answer should be grounded in the uploaded documents.",
    }


def create_reflection_summary(retrieval_decision, retrieved_chunks, critique):
    """
    Create a small reflection summary for the pipeline output.
    """
    if retrieved_chunks:
        best_score = max(chunk["score"] for chunk in retrieved_chunks)
        retrieved_count = len(retrieved_chunks)
    else:
        best_score = 0.0
        retrieved_count = 0

    return {
        "retrieval_needed": retrieval_decision["needed"],
        "retrieval_reason": retrieval_decision["reason"],
        "retrieved_chunks": retrieved_count,
        "best_evidence_score": round(best_score, 3),
        "support_level": critique.get("support_level", "Unknown"),
        "warning": critique.get("warning", "No warning."),
    }