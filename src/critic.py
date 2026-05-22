import os

from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def critique_answer(question, retrieved_chunks, answer):
    """
    critic the generate answer based on the retrieved evidence.
    """
    if not retrieved_chunks:
        return (
            "Evidence relevance: Irrelevant\n",
            "Support Level: Not supported\n",
            "Usefulness: 1/5\n",
            "Warning: No relevant evidence was found",
        )

    evidence_text = ""
    for chunk in retrieved_chunks:
        evidence_text += f"Source: {chunk['file_name']} - Chunk {chunk['chunk_id']}\n"
        evidence_text += chunk["text"] + "\n\n"

    prompt = f"""
    You are a strict evidence checker.
    Your task is to check whether the answer is supported by the retrieved evidence.
    Use only the evidence below. Do not use outside knowledge.
    
    Question: {question}
    Evidence: {evidence_text}
    Answer: {answer}
    
    Evaluate the answer using this exact format:
    Evidence relevance: Relevant/Irrelevant
    Support Level: supported / Partially supported / Not supported
    Usefulness: 1-5
    Warning: Write a short warning if the answer is not fully supported. Otherwise write "No warning."
    """
    messages: list[ChatCompletionUserMessageParam] = [
        {
            "role": "user",
            "content": prompt,
        }
    ]
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = messages,
        temperature = 0.1,
    )
    return response.choices[0].message.content.strip()