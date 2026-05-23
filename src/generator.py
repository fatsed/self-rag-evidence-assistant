import os
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None

def generate_answer(question, retrieved_chunks):
    """
    generate an answer using the user question and retrieved evidence
    """
    if not retrieved_chunks:
        return "I could not find enough evidence in the uploaded documents to answer this question."

    if client is None:
        return "Groq API key is missing. Please add GROQ_API_KEY to your env_backup. file."

    evidence_text = ""
    for chunk in retrieved_chunks:
        evidence_text += f"Source: {chunk['file_name']} - chunk {chunk['chunk_id']}\n"
        evidence_text += chunk["text"] + "\n\n"

    prompt = f"""
    You are an evidence-based question answering assistant.

    Answer the user's question using only the evidence below.
    Do not use outside knowledge.
    Do not infer answers from related information.
    Only answer if the evidence directly supports the answer.
    If the evidence does not directly answer the question, say:
    "The provided evidence is not sufficient to answer this question."

    Question:
    {question}

    Evidence:
    {evidence_text}

    Answer:
    """
    messages: list[ChatCompletionUserMessageParam] = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = messages,
        temperature = 0.2,
    )

    return response.choices[0].message.content.strip()
