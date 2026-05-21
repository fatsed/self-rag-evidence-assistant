from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent
def load_documents(documents_folder="documents"):
    """
    Load all .txt files from the documents folder.
    """
    folder = PROJECT_ROOT / documents_folder
    documents = []
    if not folder.exists():
        raise FileNotFoundError(f"Documents folder not found: {folder}")

    for file_path in folder.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        documents.append({
            "file_name": file_path.name,
            "text": text
        })
    return documents

def split_into_chunks(text, chunk_size=500):
    """
    Split text into smaller chunks.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


def clean_text(text):
    """
    Lowercase and remove extra punctuation for simple matching.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_chunk(question, chunk):
    """
    Give a simple relevance score based on shared words.
    """
    question_words = set(clean_text(question).split())
    chunk_words = set(clean_text(chunk).split())

    if not question_words:
        return 0

    common_words = question_words.intersection(chunk_words)
    return len(common_words)


def retrieve_relevant_chunks(question, documents_folder="documents", top_k=2):
    """
    Retrieve the most relevant chunks for the user question.
    """
    documents = load_documents(documents_folder)
    scored_chunks = []

    for document in documents:
        chunks = split_into_chunks(document["text"])

        for chunk in chunks:
            score = score_chunk(question, chunk)

            if score > 0:
                scored_chunks.append({
                    "file_name": document["file_name"],
                    "chunk": chunk,
                    "score": score
                })

    scored_chunks = sorted(scored_chunks, key=lambda x: x["score"], reverse=True)

    return scored_chunks[:top_k]

if __name__ == "__main__":
    question = "What is Self-RAG?"
    results = retrieve_relevant_chunks(question)

    for result in results:
        print("File:", result["file_name"])
        print("Score:", result["score"])
        print("Chunk:", result["chunk"])
        print("-" * 50)