import streamlit as st
from utils.text_extractor import extract_text
from cohere_question_generator import generate_questions
from fpdf import FPDF
import os

st.set_page_config(page_title="DocuQuest", layout="wide")
st.markdown("<h1 style='text-align: center;'>📘 DocuQuest: Document to Question Generator</h1>", unsafe_allow_html=True)
st.markdown("---")

def save_to_pdf(text: str, filename: str = "questions_output.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

uploaded_file = st.file_uploader("📂 Upload a file (PDF, Word, PowerPoint):", type=["pdf", "docx", "pptx"])

st.markdown("### 🔍 What would you like to generate?")
option = st.selectbox("Choose Type", ["✅ MCQs", "📝 Descriptive Questions"])

include_answers = False
if option == "✅ MCQs":
    include_answers = st.checkbox("Include Answers and Explanations in MCQs", value=True)
elif option == "📝 Descriptive Questions":
    include_answers = st.checkbox("Include Answers with Descriptive Questions", value=True)

num_questions = st.number_input("How many questions?", min_value=1, max_value=20, value=5, step=1)
st.markdown("---")

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    file_path = f"temp.{file_ext}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ File uploaded: {uploaded_file.name}")

    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text(file_path, file_ext)

    st.markdown("### 📄 Extracted Text Preview")
    st.text_area("Extracted Text", extracted_text[:2000] + "...", height=200)

    if st.button("🚀 Generate Questions"):
        with st.spinner("✍️ Generating questions..."):
            if option == "✅ MCQs":
                question_type = "mcq_with_answers" if include_answers else "mcq"
            else:
                question_type = "long_with_answers" if include_answers else "long"

            generated = generate_questions(extracted_text, question_type=question_type, num_questions=num_questions)

        st.markdown("## 📋 Generated Questions")
        st.text_area("Output", generated.strip(), height=400)

        st.download_button("⬇️ Download TXT", generated.strip(), file_name="questions.txt", mime="text/plain")

        save_to_pdf(generated.strip(), "questions_output.pdf")
        with open("questions_output.pdf", "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name="questions_output.pdf", mime="application/pdf")

        st.success("✅ Questions generated successfully!")
else:
    st.info("📁 Please upload a file to begin.")
