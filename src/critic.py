import os
from pathlib import Path
import json
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None

def critique_answer(question, retrieved_chunks, answer):
    """
    critic the generated answer based on the retrieved evidence.
    """
    if not retrieved_chunks:
        return {
            "evidence_relevance": "Irrelevant",
            "support_level": "Not supported",
            "usefulness": "1/5",
            "warning": "No relevant evidence was found.",
            "reason": "The system could not retrieve any evidence from the uploaded documents.",
        }

    if client is None:
        return {
            "evidence_relevance": "Unknown",
            "support_level": "Not supported",
            "usefulness": "1/5",
            "warning": "Groq API key is missing.",
            "reason": "Please add GROQ_API_KEY to your .env file."
        }

    evidence_text = ""

    for chunk in retrieved_chunks:
        evidence_text += f"Source: {chunk['file_name']} - Chunk {chunk['chunk_id']}\n"
        evidence_text += f"Similarity score: {chunk['score']:.3f}\n"
        evidence_text += chunk["text"] + "\n\n"

    prompt = f"""
        You are a strict evidence checker.
        Your job is to evaluate whether the generated answer is supported by the retrieved evidence.
    
        Use only the evidence provided below.
        Do not use outside knowledge.
        Do not explain the topic generally.
        Focus only on whether the answer is grounded in the evidence.
        
        Question:
        {question}
        
        Retrieved evidence:
        {evidence_text}
        
        Generated answer:
        {answer}
        
        Return only valid JSON using exactly this structure:
        
        {{
          "evidence_relevance": "Relevant / Partially relevant / Irrelevant",
          "support_level": "Fully supported / Partially supported / Not supported",
          "usefulness": "1/5, 2/5, 3/5, 4/5, or 5/5",
          "warning": "No warning. OR a short warning if the answer is not fully supported.",
          "reason": "One short sentence explaining the evaluation."
        }}
        
        Rules:
        - If the answer includes information not found in the evidence, mark it as Partially supported or Not supported.
        - If the retrieved evidence is weak or unrelated, mark evidence relevance as Partially relevant or Irrelevant.
        - If the answer is fully grounded in the evidence, mark it as Fully supported.
        - If the generated answer says that the evidence is not sufficient, do not say it contradicts the evidence.
        - In that case, mark support level as Not supported and warning as "No direct evidence found."
        - Keep the JSON values short.
        - Do not include markdown.
        - Do not include extra text outside the JSON.
        """

    messages: list[ChatCompletionUserMessageParam] = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    critique_text = response.choices[0].message.content.strip()

    try:
        return json.loads(critique_text)
    except json.JSONDecodeError:
        return {
            "evidence_relevance": "Unknown",
            "support_level": "Unknown",
            "usefulness": "Unknown",
            "warning": "The critique could not be parsed as JSON.",
            "reason": critique_text,
        }