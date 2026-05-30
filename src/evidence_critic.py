import json
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def critique_evidence_chunk(question, chunk):
    """
    Use the language model to evaluate one retrieved evidence chunk.
    """
    if client is None:
        return {
            "evidence_label": chunk.get("evidence_label", "Unknown"),
            "evidence_reason": "API key is missing, so the evidence was not evaluated by the language model.",
        }

    prompt = f"""
        You are evaluating one retrieved evidence chunk for a Self-RAG-style assistant.
        
        Question:
        {question}
        
        Evidence chunk:
        {chunk["text"]}
        
        Evaluate whether this evidence chunk is useful for answering the question.
        
        Return only valid JSON using this exact structure:
        
        {{
          "evidence_label": "Relevant / Partially relevant / Irrelevant",
          "evidence_reason": "One short sentence explaining why."
        }}
        
        Rules:
        - Use Relevant if the evidence directly helps answer the question.
        - Use Partially relevant if the evidence is related but does not fully answer the question.
        - Use Irrelevant if the evidence does not help answer the question.
        - Do not include markdown.
        - Do not include extra text outside the JSON.
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
            temperature=0.0,
            response_format={"type": "json_object"},
        )

        critique_text = response.choices[0].message.content.strip()
        return json.loads(critique_text)

    except Exception as error:
        return {
            "evidence_label": chunk.get("evidence_label", "Unknown"),
            "evidence_reason": f"Evidence critique failed. Error: {error}",
        }

def critique_retrieved_evidence(question, retrieved_chunks):
    """
    Add LLM-based evidence critique labels and reasons to retrieved chunks.
    """
    critiqued_chunks = []

    for chunk in retrieved_chunks:
        critique = critique_evidence_chunk(question, chunk)

        updated_chunk = {
            **chunk,
            "evidence_label": critique.get(
                "evidence_label",
                chunk.get("evidence_label", "Unknown")
            ),
            "evidence_reason": critique.get(
                "evidence_reason",
                "No evidence critique reason provided."
            ),
        }

        critiqued_chunks.append(updated_chunk)

    return critiqued_chunks