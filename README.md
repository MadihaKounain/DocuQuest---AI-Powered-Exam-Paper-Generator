# 📘 DocuQuest - AI-Powered Exam Paper Generator

**DocuQuest** is an intelligent document-based question paper generator. It allows you to upload any textbook, notes, or slides (PDF, Word, PPT) — even scanned PDFs — and automatically generates **MCQs** or **Descriptive Questions**, optionally with answers, using **Cohere AI**.

---

## 🚀 Features

- 📄 **Supports PDF (text + scanned), Word (.docx), and PPT (.pptx)**
- 🧠 **Cohere API** powered question generation
- 🗂 **Choose Question Type**: 
  - MCQs with options and answers
  - Descriptive questions
  - Descriptive with answers
- 📝 **Up to 20 Questions** per session
- 🔍 **OCR support** for scanned documents using `pdf2image` and `pytesseract`
- 💬 Clean and simple **Streamlit UI**
- 💾 Download generated questions as `.txt` or `.pdf`
- 📦 Exportable and customizable

---

## 📂 Project Structure

```
docuquest/
├── app.py                  # Streamlit UI
├── utils/
│   ├── text_extractor.py   # Extracts and cleans text
├──cohere_question_generator.py  # Generates questions using Cohere
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/docuquest.git
cd docuquest
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Add your Cohere API key**:
Set your Cohere API key as an environment variable:
```bash
export COHERE_API_KEY=your_key_here  # Linux/Mac
set COHERE_API_KEY=your_key_here     # Windows
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Usage Guide

1. Upload a document (PDF, DOCX, or PPTX)
2. Choose question type (MCQ or Descriptive)
3. Select number of questions (up to 20)
4. (Optional) Include answers
5. Click **Generate**
6. Preview the output and download as `.txt` or `.pdf`

---

## 📚 Example Outputs

- **MCQ**  
  *Q1. What is the main objective of water harvesting?*  
  a) Increase humidity  
  b) Recharge groundwater ✔  
  c) Reduce salinity  
  d) Control erosion  

- **Descriptive**  
  *Q3. Explain the process of rainwater harvesting and its importance in drought-prone areas.*

---

## ✅ Requirements

- Python 3.8+
- Streamlit
- Cohere
- pdf2image
- pytesseract
- python-docx
- python-pptx
- fpdf

---

## 🌐 API Used

- [Cohere Generate API](https://docs.cohere.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## 📌 Future Enhancements

- 🔍 Topic-wise question generation
- 📊 Difficulty-level classification
- 🗃️ Store and manage multiple documents
- 🌐 Support for more languages
- 👨‍🏫 Teacher feedback or editing interface

---

## 📄 License

MIT License © 2025 Madiha Kounain

---

## 💬 Feedback

Feel free to open issues or suggest features!  
**GitHub**: [github.com/yourusername/docuquest](https://github.com/yourusername/docuquest)  
**Email**: yourname@example.com
