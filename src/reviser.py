import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def revise_answer_if_needed(question, retrieved_chunks, answer, critique):
    """
    Revise the generated answer if the critique shows that it is not fully supported.
    """

    support_level = critique.get("support_level", "Unknown")

    if support_level == "Fully supported":
        return answer

    if client is None:
        return answer

    evidence_text = ""

    for chunk in retrieved_chunks:
        evidence_text += f"Source: {chunk['file_name']} - Chunk {chunk['chunk_id']}\n"
        evidence_text += f"Evidence label: {chunk.get('evidence_label', 'Unknown')}\n"
        evidence_text += f"Evidence reason: {chunk.get('evidence_reason', 'No reason provided.')}\n"
        evidence_text += chunk["text"] + "\n\n"

    prompt = f"""
You are revising an answer for a Self-RAG-style evidence assistant.

The original answer may not be fully supported by the retrieved evidence.

Your task:
- Revise the answer using only the retrieved evidence.
- Remove any unsupported information.
- Keep the answer clear and concise.
- If the evidence is not enough, say:
  "The retrieved evidence is not sufficient to answer this question."

Question:
{question}

Retrieved evidence:
{evidence_text}

Original answer:
{answer}

Critique:
Support level: {critique.get("support_level", "Unknown")}
Warning: {critique.get("warning", "No warning.")}
Reason: {critique.get("reason", "No reason provided.")}

Revised answer:
"""

    messages: list[ChatCompletionUserMessageParam] = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.1,
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return answer