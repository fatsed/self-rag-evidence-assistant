
from retriever import retrieve_relevant_chunks
from generator import generate_answer
from critic import critique_answer


def run_pipeline(question):
    """
    Run the full Self-RAG-inspired pipeline.
    """

    retrieved_chunks = retrieve_relevant_chunks(question)

    if not retrieved_chunks:
        return {
            "question": question,
            "retrieval_needed": "Yes",
            "evidence": "No relevant evidence found.",
            "answer": "I could not find enough evidence in the documents to answer this question.",
            "critique": "Evidence relevance: Irrelevant\nSupport level: Not supported\nUsefulness: 1\nWarning: No relevant evidence was found.",
        }

    evidence = "\n\n".join(
        [chunk["chunk"] for chunk in retrieved_chunks]
    )

    answer = generate_answer(question, evidence)

    critique = critique_answer(question, evidence, answer)

    return {
        "question": question,
        "retrieval_needed": "Yes",
        "evidence": evidence,
        "answer": answer,
        "critique": critique,
    }