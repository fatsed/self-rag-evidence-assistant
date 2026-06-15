import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


def get_groq_api_key():
    return os.getenv("GROQ_API_KEY")


def get_groq_client():
    api_key = get_groq_api_key()

    if not api_key:
        return None

    return Groq(api_key=api_key)


def missing_api_key_message():
    return (
        "API key is missing. "
        "Please create a .env file and add your GROQ_API_KEY."
    )