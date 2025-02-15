import os

import streamlit as st

from rag_utility import process_document_to_chroma_db, answer_question



working_dir = os.getcwd()

st.title("DeepSeek-R1 RAG")


uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # define save path
    save_path = os.path.join(working_dir, uploaded_file.name)
    #  save the file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    process_document = process_document_to_chroma_db(uploaded_file.name)
    st.info("Document Processed Successfully")



user_question = st.text_area("Ask your question about the document")

if st.button("Answer"):

    answer = answer_question(user_question)

    st.markdown("### DeepSeek-R1 Response")
    st.markdown(answer)
