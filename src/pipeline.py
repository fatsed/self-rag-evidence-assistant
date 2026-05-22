from src.file_loader import load_uploaded_files
from src.chunker import create_document_chunks
from src.retriever import retrieve_relevant_chunks
from src.generator import generate_answer
from src.critic import critique_answer


def run_pipeline(uploaded_files, question, top_k=3, min_score=0.25):
    """
    run the full evidence QA pipeline.
    """
    if not uploaded_files:
        return {
            "answer": "Please upload at least one document.",
            "evidence": [],
            "critique": {
                "evidence_relevance": "Irrelevant",
                "support_level": "Not supported",
                "usefulness": "1/5",
                "warning": "No document was uploaded.",
                "reason": "The system cannot answer without uploaded documents.",
            },
        }
    if not question.strip():
        return {
            "answer": "Please enter a question.",
            "evidence": [],
            "critique": {
                "evidence_relevance": "Irrelevant",
                "support_level": "Not supported",
                "usefulness": "1/5",
                "warning": "No question was entered.",
                "reason": "The system needs a question to retrieve evidence.",
            },
        }

    documents = load_uploaded_files(uploaded_files)
    chunks = create_document_chunks(documents)

    retrieved_chunks = retrieve_relevant_chunks(
        question,
        chunks,
        top_k=top_k,
        min_score=min_score,
    )

    answer = generate_answer(question, retrieved_chunks)
    critique = critique_answer(question, retrieved_chunks, answer)

    return {
        "answer": answer,
        "evidence": retrieved_chunks,
        "critique": critique,
    }