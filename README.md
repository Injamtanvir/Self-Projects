````md
# 📚 PDF to Python Audio Book

Convert any **PDF document** into an **audio book** using Python.  
This project reads text from a PDF file and generates speech output automatically, allowing you to listen to documents instead of reading them.

---

## 🚀 Project Setup

Initialize the project using **uv**:

```bash
uv init
uv venv
````

---

## 📦 Requirements

Install the required dependencies:

```bash
uv pip install pyttsx3
uv pip install pypdf
```

### Dependencies Used

* **pyttsx3** — Text-to-Speech engine (offline)
* **pypdf** — Extracts text from PDF files

---

## ▶️ Run the Program

Execute the main script:

```bash
uv run python main.py
```

---

## 💡 Features

* 📄 Extracts text from PDF files
* 🔊 Converts text into speech
* 🎧 Creates an audiobook-like listening experience
* 🌐 Works offline (no API required)

---

## 🛠️ Tech Stack

* Python
* pyttsx3
* pypdf
* uv (Python package & environment manager)

---

## 📌 Usage

1. Place your PDF file in the project directory.
2. Update the file path inside `main.py` if needed.
3. Run the program and enjoy your audiobook 🎧.

