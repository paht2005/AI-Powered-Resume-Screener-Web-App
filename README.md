# 🤖 AI-Powered Resume Screener Web App

A Streamlit-based web app that screens resumes using AI — integrated with [Ollama](https://ollama.ai/) LLMs to compare uploaded resumes to a job description, highlight matching skills, summarize key points, and return a match score.
![demo](/demo.png)

---

## 📌 Table of Contents

1. [✨ Project Overview](#-project-overview)  
2. [🚀 Features](#-features)  
3. [🗂️ Project Structure](#-project-structure)
4. [🧰 Tech Stack](#-tech-stack)
5. [⚙️ Installation](#-installation)  
6. [✅ Example Output](#-example-output)  
7. [🧭 Future Work](#-future-work)  
8. [📄 License](#-license)
9. [🤝 Contributing](#-contributing)
10. [🧠 Acknowledgements](#-acknowledgements)
11. [📬 Contact](#-contact)

---

## ✨ Project Overview

This AI-Powered Resume Screener helps recruiters or HR teams to:
- Parse PDF resumes
- Extract key info (skills, experience, education)
- Compare with a job description
- Score relevance using embeddings + cosine similarity
- (Optional) Summarize resumes using local LLM (via Ollama)

---

## 🚀 Features

- Upload multiple PDF resumes
- Paste job description for comparison
- Compute match scores using SentenceTransformer
- Highlight overlapping skills between JD and resume
- *(Optional) Summarize resumes using LLM (Ollama)*
- Responsive UI via Streamlit + CSS

---
## 🗂️ Project Structure
```
├── __pyache__/
├── main_app.py
├── resume_parser.py
├── scorer.py
├── summarizer.py
├── style.css
├── requirements-webapp.txt # Python dependences
└── demo.png 
└── README.md  # Project documentation
└── LICENSE

```
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
pip install -r requirements-webapp.txt
streamlit run main_app.py # Usage
```
---
## ✅ Example Output
- 📄 John_Doe_CV.pdf — Match Score: 87.6%
- 📄 Jane_Smith_CV.pdf — Match Score: 65.4%

--- 
## 🧭 Future Work
- Export results to CSV
- Use named-entity recognition (NER) for skill extraction
- Add job role suggestions via LLM
- Multi-language support (English + Vietnamese)

---
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


---
## 🤝 Contributing
I welcome contributions to improve this project!
Feel free to:
- Submit pull requests
- Report bugs
- Suggest new features

--- 
## 🧠 Acknowledgements

### 1. What is Ollama?
- [Ollama](https://ollama.ai/) is a tool for running lightweight open-source LLMs (like LLaMA 2, Mistral, Phi, etc.) **locally on your machine** with a simple CLI.
- In this project, Ollama is used to **summarize PDF resumes** into 3–5 bullet points using models like `llama2`.

### 2. Install Ollama (Optional for LLM Summary)
If you want to enable **AI-powered resume summarization**, install Ollama:
- Download Ollama: https://ollama.com/download
- Install a model (example: `llama2`):
```bash
ollama run llama2
```
- After installation, make sure the `ollama` command is available in your system PATH.

### 3. Troubleshooting Ollama Issues
If you see this error:
```bash
FileNotFoundError: [WinError 2] The system cannot find the file specified
```
Make sure that:
- Ollama is installed correctly
- The `ollama` CLI is in your system `PATH`
- You’ve downloaded a model (like `llama2`) with `ollama run llama2`


--- 
## 📬 Contact
Contact for work: **Nguyễn Công Phát** – congphatnguyen.work@gmail.com
