from src.file_loader import load_uploaded_files
from src.chunker import create_document_chunks
from src.retriever import retrieve_relevant_chunks
from src.generator import generate_answer
from src.critic import critique_answer
from src.reflection import (
    decide_retrieval_need,
    judge_evidence_quality,
    create_reflection_summary,
)


def run_pipeline(uploaded_files, question, top_k=3, min_score=0.25):
    """
    Run the full Self-RAG-inspired evidence QA pipeline.
    """
    if not uploaded_files:
        critique = {
            "evidence_relevance": "Irrelevant",
            "support_level": "Not supported",
            "usefulness": "1/5",
            "warning": "No document was uploaded.",
            "reason": "The system cannot answer without uploaded documents.",
        }

        retrieval_decision = decide_retrieval_need(question, uploaded_files)
        evidence_quality = judge_evidence_quality([])

        reflection = create_reflection_summary(
            retrieval_decision,
            evidence_quality,
            [],
            critique,
        )

        return {
            "answer": "Please upload at least one document.",
            "evidence": [],
            "critique": critique,
            "reflection": reflection,
        }

    if not question.strip():
        critique = {
            "evidence_relevance": "Irrelevant",
            "support_level": "Not supported",
            "usefulness": "1/5",
            "warning": "No question was entered.",
            "reason": "The system needs a question to retrieve evidence.",
        }

        retrieval_decision = decide_retrieval_need(question, uploaded_files)
        evidence_quality = judge_evidence_quality([])

        reflection = create_reflection_summary(
            retrieval_decision,
            evidence_quality,
            [],
            critique,
        )

        return {
            "answer": "Please enter a question.",
            "evidence": [],
            "critique": critique,
            "reflection": reflection,
        }

    retrieval_decision = decide_retrieval_need(question, uploaded_files)

    if not retrieval_decision["needed"]:
        critique = {
            "evidence_relevance": "Irrelevant",
            "support_level": "Not supported",
            "usefulness": "1/5",
            "warning": "Retrieval was not performed.",
            "reason": retrieval_decision["reason"],
        }

        evidence_quality = judge_evidence_quality([])

        reflection = create_reflection_summary(
            retrieval_decision,
            evidence_quality,
            [],
            critique,
        )

        return {
            "answer": "The system could not perform retrieval for this question.",
            "evidence": [],
            "critique": critique,
            "reflection": reflection,
        }

    documents = load_uploaded_files(uploaded_files)
    chunks = create_document_chunks(documents)

    retrieved_chunks = retrieve_relevant_chunks(
        question,
        chunks,
        top_k=top_k,
        min_score=min_score,
    )

    evidence_quality = judge_evidence_quality(retrieved_chunks)

    answer = generate_answer(question, retrieved_chunks)
    critique = critique_answer(question, retrieved_chunks, answer)

    reflection = create_reflection_summary(
        retrieval_decision,
        evidence_quality,
        retrieved_chunks,
        critique,
    )

    return {
        "answer": answer,
        "evidence": retrieved_chunks,
        "critique": critique,
        "reflection": reflection,
    }