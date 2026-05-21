import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(question, evidence):
    """
    Generate an answer using the user question and retrieved evidence.
    """
    prompt = f"""You are an evidence-based assistant.
    Answer the user's question using only the evidence provided below.
    If the evidence is not enough, say that the evidence is not sufficient.

    Question:
    {question}

    Evidence:
    {evidence}

    Answer:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()