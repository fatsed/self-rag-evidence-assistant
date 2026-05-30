def decide_retrieval_need(question, uploaded_files):
    """
    Decide whether document retrieval should be used.
    This is a simplified Self-RAG-style decision step.
    In this project, retrieval is needed when the user uploads documents
    and asks a valid document-based question.
    """
    if not uploaded_files:
        return {
            "needed": False,
            "decision": "No retrieval",
            "reason": "No documents were uploaded.",
        }

    question_text = question.strip().lower()

    if not question_text:
        return {
            "needed": False,
            "decision": "No retrieval",
            "reason": "No question was provided.",
        }

    conversational_inputs = [
        "hi",
        "hello",
        "hey",
        "thanks",
        "thank you",
        "what can you do",
        "what can you do?",
    ]

    if question_text in conversational_inputs:
        return {
            "needed": False,
            "decision": "No retrieval",
            "reason": "The question is conversational and does not need document retrieval.",
        }

    return {
        "needed": True,
        "decision": "Retrieve",
        "reason": "The answer should be grounded in the uploaded documents.",
    }

def judge_evidence_quality(retrieved_chunks, good_score_threshold=0.35):
    """
    Judge the quality of the retrieved evidence based on the best similarity score.
    """
    if not retrieved_chunks:
        return {
            "quality": "No evidence",
            "best_score": 0.0,
            "reason": "No relevant evidence was retrieved from the uploaded documents.",
        }

    best_score = max(chunk["score"] for chunk in retrieved_chunks)

    if best_score >= good_score_threshold:
        return {
            "quality": "Strong evidence",
            "best_score": round(best_score, 3),
            "reason": "The retrieved evidence has a good similarity score and is likely relevant to the question.",
        }
    return {
        "quality": "Weak evidence",
        "best_score": round(best_score, 3),
        "reason": "The retrieved evidence may not be strongly related to the question.",
    }

def count_evidence_labels(retrieved_chunks):
    """
    Count relevance labels for retrieved evidence chunks.
    """
    label_counts = {
        "Relevant": 0,
        "Partially relevant": 0,
        "Weak evidence": 0,
    }

    for chunk in retrieved_chunks:
        label = chunk.get("evidence_label", "Weak evidence")

        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts["Weak evidence"] += 1

    return label_counts

def create_reflection_summary(retrieval_decision, evidence_quality, retrieved_chunks, critique):
    """
    Create a reflection summary for the final pipeline output.
    """
    label_counts = count_evidence_labels(retrieved_chunks)
    return {
        "retrieval_decision": retrieval_decision.get("decision", "Unknown"),
        "retrieval_needed": retrieval_decision.get("needed", False),
        "retrieval_reason": retrieval_decision.get("reason", "No reason provided."),
        "retrieved_chunks": len(retrieved_chunks),
        "evidence_quality": evidence_quality.get("quality", "Unknown"),
        "best_evidence_score": evidence_quality.get("best_score", 0.0),
        "evidence_reason": evidence_quality.get("reason", "No evidence reason provided."),
        "support_level": critique.get("support_level", "Unknown"),
        "warning": critique.get("warning", "No warning."),
        "relevant_evidence_count": label_counts["Relevant"],
        "partially_relevant_evidence_count": label_counts["Partially relevant"],
        "weak_evidence_count": label_counts["Weak evidence"],
    }