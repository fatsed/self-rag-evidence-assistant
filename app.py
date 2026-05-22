import streamlit as st

from src.pipeline import run_pipeline


st.set_page_config(
    page_title="Self-RAG Evidence Assistant",
    page_icon="📄",
    layout="wide",
)


st.title("Self-RAG Evidence Assistant 🧠📄")

st.write(
    "Upload documents, ask a question, and get an evidence-based answer with a support check."
)

uploaded_files = st.file_uploader(
    "Upload your documents",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True,
)

question = st.text_input("Ask a question about your documents")

top_k = st.slider(
    "Number of evidence chunks to retrieve",
    min_value=1,
    max_value=5,
    value=3,
)

if st.button("Generate Answer"):
    if not uploaded_files:
        st.warning("Please upload at least one document.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching documents and generating answer..."):
            result = run_pipeline(uploaded_files, question, top_k=top_k)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Retrieved Evidence")

        if result["evidence"]:
            for i, chunk in enumerate(result["evidence"], start=1):
                with st.expander(
                    f"Evidence {i} | {chunk['file_name']} | Chunk {chunk['chunk_id']} | Score: {chunk['score']:.3f}"
                ):
                    st.write(chunk["text"])
        else:
            st.info("No evidence found.")

        st.subheader("Critique")
        st.write(result["critique"])