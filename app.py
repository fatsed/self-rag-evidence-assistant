import streamlit as st
from src.pipeline import run_pipeline

st.set_page_config(
    page_title="Self-RAG Evidence Assistant",
    page_icon="📄",
    layout="wide",
)

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] h3 {
    margin-bottom: 0.4rem;
    }
    
    section[data-testid="stSidebar"] p {
        margin-bottom: 0.4rem;
    }
    
    section[data-testid="stSidebar"] li {
        margin-bottom: 0.2rem;
    }
    
    section[data-testid="stSidebar"] hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .main-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 17px;
        color: #555;
        margin-bottom: 25px;
    }
    .answer-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #f7f7f7;
        border: 1px solid #ddd;
        line-height: 1.6;
    }
    .small-note {
        font-size: 14px;
        color: #666;
    }
    .block-container {
    max-width: 1050px;
    padding-top: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "result" not in st.session_state:
    st.session_state.result = None
if "last_question" not in st.session_state:
    st.session_state.last_question = ""
if "uploaded_file_names" not in st.session_state:
    st.session_state.uploaded_file_names = []
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0
if "question_key" not in st.session_state:
    st.session_state.question_key = 0

st.markdown(
    '<div class="main-title">Self-RAG Evidence Assistant 🧠📄</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Upload documents, ask a question, retrieve evidence, and check whether the answer is supported.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        """
        ### About this project
        This app is inspired by **Self-RAG**. It retrieves evidence from uploaded documents, generates an answer, and critiques the support level of the answer.

        ---
        ### Supported files
        - PDF
        - TXT
        - DOCX

        ---
        ### Pipeline
        1. Upload documents
        2. Split text into chunks
        3. Retrieve relevant evidence
        4. Generate answer
        5. Critique the answer
        """
    )
input_col, settings_col = st.columns([1.5, 1])

with input_col:
    st.subheader("Upload documents")
    uploaded_files = st.file_uploader(
        "Choose one or more files",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True,
        key=f"file_uploader_{st.session_state.uploader_key}",
    )
    st.subheader("Ask a question")
    question = st.text_area(
        "Your question",
        placeholder="Example: What is critique in Self-RAG?",
        height=120,
        key=f"question_{st.session_state.question_key}",
    )

with settings_col:
    st.subheader("Settings")
    top_k = st.slider(
        "Number of evidence chunks",
        min_value=1,
        max_value=5,
        value=3,
    )
    min_score = st.slider(
    "Minimum evidence score",
    min_value=0.0,
    max_value=1.0,
    value=0.15,
    step=0.05,
    )

    st.caption(
    "Evidence score shows how similar a retrieved chunk is to your question. "
    "Higher scores usually mean more relevant evidence."
    )
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded")
    else:
        st.info("No file uploaded yet")
    st.markdown(
        '<p class="small-note">Tip: Upload more than one document to test multi-document retrieval.</p>',
        unsafe_allow_html=True,
    )
st.divider()

col_run, col_clear = st.columns([3, 1])
with col_run:
    run_button = st.button(
        "Generate Answer",
        type="primary",
        use_container_width=True
    )

with col_clear:
    clear_button = st.button(
        "Clear",
        type="secondary",
        use_container_width=True
    )

if clear_button:
    st.session_state.result = None
    st.session_state.last_question = ""
    st.session_state.uploaded_file_names = []
    st.session_state.uploader_key += 1
    st.session_state.question_key += 1
    st.rerun()

if run_button:
    if not uploaded_files:
        st.warning("Please upload at least one document.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        st.info("Searching documents and generating answer...")

        result = run_pipeline(
            uploaded_files,
            question,
            top_k=top_k,
            min_score=min_score,
        )
        st.session_state.result = result
        st.session_state.last_question = question
        st.session_state.uploaded_file_names = [
            uploaded_file.name for uploaded_file in uploaded_files
        ]
        st.success("Answer generated successfully.")

if st.session_state.result:
    result = st.session_state.result
    answer_tab, evidence_tab, critique_tab, files_tab = st.tabs(
        ["Answer", "Retrieved Evidence", "Critique", "Uploaded Files"]
    )
    answer = result.get("answer", "")
    critique = result.get("critique", "")
    evidence = result.get("evidence", [])

    if isinstance(critique, dict):
        evidence_relevance = critique.get("evidence_relevance", "Unknown")
        support_level = critique.get("support_level", "Unknown")
        usefulness = critique.get("usefulness", "Unknown")
        warning = critique.get("warning", "No warning.")
        reason = critique.get("reason", "")
    else:
        evidence_relevance = "Unknown"
        support_level = "Unknown"
        usefulness = "Unknown"
        warning = "The critique was returned as plain text."
        reason = critique

    with (answer_tab):
        st.subheader("Answer")

        st.markdown(
            f"""
            <div class="answer-box">{answer}
            </div>
            """,
            unsafe_allow_html=True,
        )
        output_text = f"""
            Question:
            {st.session_state.last_question}
            Answer:
            {answer}
            Critique:
            Evidence relevance: {evidence_relevance}
            Support level: {support_level}
            Usefulness: {usefulness}
            Warning: {warning}
            Reason: {reason}
            """

        st.download_button(
            label="Download result as TXT",
            data=output_text,
            file_name="evidence_qa_result.txt",
            mime="text/plain",
        )

    with evidence_tab:
        st.subheader("Retrieved Evidence")
        st.caption(
            "Each score is based on semantic similarity between your question and the retrieved text chunk."
        )
        if evidence:
            for i, chunk in enumerate(evidence, start=1):
                score = chunk["score"]
                with st.expander(
                    f"Evidence {i} | {chunk['file_name']} | Chunk {chunk['chunk_id']} | Score: {score:.3f}"
                ):
                    st.write(chunk["text"])
        else:
            st.info("No evidence found.")

    with critique_tab:
        st.subheader("Critique")

        card1, card2, card3 = st.columns(3)
        with card1:
            st.metric("Evidence relevance", evidence_relevance)
        with card2:
            st.metric("Support level", support_level)
        with card3:
            st.metric("Usefulness", usefulness)

        st.markdown("### Warning")

        if support_level == "Fully supported":
            st.success(warning)
        elif support_level == "Partially supported":
            st.warning(warning)
        elif support_level == "Not supported":
            st.error(warning)
        else:
            st.info(warning)

        st.markdown("### Reason")
        st.write(reason)


    with files_tab:
        st.subheader("Uploaded Files")

        if st.session_state.uploaded_file_names:
            for file_name in st.session_state.uploaded_file_names:
                st.write(f"- {file_name}")
        else:
            st.info("No uploaded file information found.")
