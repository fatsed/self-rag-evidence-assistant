import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None

def generate_answer(question, retrieved_chunks):
    """
    generate an answer using the user question and retrieved evidence
    """
    if not retrieved_chunks:
        return "I could not find enough evidence in the uploaded documents to answer this question."

    if client is None:
        return "Groq API key is missing. Please add GROQ_API_KEY to your .env file."

    evidence_text = ""
    for chunk in retrieved_chunks:
        evidence_text += f"Source: {chunk['file_name']} - chunk {chunk['chunk_id']}\n"
        evidence_text += chunk["text"] + "\n\n"

    prompt = f"""
    You are an evidence-based question answering assistant.

    Answer the user's question using only the retrieved evidence below.

    Rules:
    - Give a direct answer to the question.
    - Do not start by saying "The provided evidence is sufficient".
    - Do not use outside knowledge.
    - Do not add information that is not supported by the evidence.
    - If the evidence does not directly answer the question, say:
      "The retrieved evidence is not sufficient to answer this question."
    - Keep the answer clear and concise.
    - When useful, mention which evidence supports the answer.

    Question:
    {question}

    Retrieved evidence:
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
