# 🤖 AI-Powered Resume Screener Web App

A Streamlit-based web app that screens resumes using AI — compares uploaded resumes to a job description, highlights matching skills, summarizes key points, and returns a match score.

---

## 📌 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Example Output](#example-output)  
7. [Future Work](#future-work)  
8. [License](#license)

---

## 🧠 Project Overview

This AI-Powered Resume Screener helps recruiters or HR teams to:
- Parse PDF resumes
- Extract key info (skills, experience, education)
- Compare with a job description
- Score relevance using embeddings + cosine similarity
- (Optional) Summarize resumes using local LLM (via Ollama)

---

## 🚀 Features

- 📂 Upload multiple PDF resumes
- 📝 Paste job description for comparison
- 🧠 Compute match scores using SentenceTransformer
- 🔍 Highlight overlapping skills between JD and resume
- 🧾 (Optional) Summarize resumes using LLM (Ollama)
- ✅ Responsive UI via Streamlit + CSS

---

## 🧰 Tech Stack

| Feature                | Tool/Library                |
|------------------------|-----------------------------|
| File Upload UI         | Streamlit                   |
| PDF Parsing            | PyMuPDF (`fitz`)            |
| Text Embedding         | `sentence-transformers`     |
| Similarity Scoring     | Cosine Similarity (`sklearn`)|
| LLM Summary (Optional) | Ollama (LLaMA2, Mistral...) |

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/AI-Powered-Resume-Screener.git
cd AI-Powered-Resume-Screener
pip install -r requirements.txt
