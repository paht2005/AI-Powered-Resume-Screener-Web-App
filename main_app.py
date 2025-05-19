import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import score_resume, highlight_matching_skills
from summarizer import summarize_with_ollama

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
st.title("📄 AI-Powered Resume Screener")

job_description = st.text_area("📌 Paste Job Description Here")
uploaded_files = st.file_uploader("📂 Upload Resumes (PDF only)", type="pdf", accept_multiple_files=True)

if job_description and uploaded_files:
    st.subheader("🧠 Matching Scores")
    for uploaded_file in uploaded_files:
        with st.spinner(f"Processing {uploaded_file.name}..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            score = score_resume(resume_text, job_description)
            st.markdown(f"✅ **{uploaded_file.name}** — Match Score: **{score}%**", unsafe_allow_html=True)

            # Highlight kỹ năng
            st.markdown("🔍 **Highlighted Skills:**", unsafe_allow_html=True)
            highlighted = highlight_matching_skills(resume_text, job_description)
            st.markdown(highlighted, unsafe_allow_html=True)

            # Tóm tắt
            if st.checkbox(f"📄 Show Summary for {uploaded_file.name}"):
                summary = summarize_with_ollama(resume_text)
                st.markdown("📝 **Resume Summary**:")
                st.markdown(summary)
