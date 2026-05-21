import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def critique_answer(question, evidence, answer):
    """
    Critique the generated answer based on the retrieved evidence.
    """

    prompt = f"""
You are a strict evidence checker.

Your task is to evaluate the answer using only the evidence provided.

Question:
{question}

Evidence:
{evidence}

Answer:
{answer}

Evaluate the answer using this format:

Evidence relevance: Relevant / Irrelevant
Support level: Fully supported / Partially supported / Not supported
Usefulness: 1-5
Warning: Write a short warning if the answer is not fully supported. Otherwise write "No warning."
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.1,
    )

    return response.choices[0].message.content.strip()