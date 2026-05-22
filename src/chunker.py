def split_text_into_chunks(text, chunk_size=120, overlap=30):
    """
    split a long text into smaller overlapping chunks.
    chunk_size and overlap are based on number of words.
    """
    words = text.split()
    chunks = []

    if not words:
        return chunks

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append(chunk_text)

        start += chunk_size - overlap

    return chunks


def create_document_chunks(documents, chunk_size=120, overlap=30):
    """
    create chunks from all uploaded documents.
    each chunk keeps its source file name.
    """
    all_chunks = []

    for document in documents:
        file_name = document["file_name"]
        text = document["text"]

        chunks = split_text_into_chunks(
            text,
            chunk_size=chunk_size,
            overlap=overlap
        )

        for index, chunk in enumerate(chunks, start=1):
            all_chunks.append(
                {
                    "file_name": file_name,
                    "chunk_id": index,
                    "text": chunk,
                }
            )

    return all_chunks