# 🔍 Requirements Traceability with Python & NLP

Welcome to your Requirements Engineering mini-lab! In this project, you'll use Python and Natural Language Processing (NLP) to create traceability links between software requirements and test cases — a key task in software engineering.

---

## 🎯 What You'll Learn

By completing this lab, you will:
- Understand what traceability means in software development.
- Use Python to compare requirements and test cases automatically.
- Apply basic NLP to detect similarities in textual content.
- Visualize how requirement traceability can be automated using a Jupyter notebook or script.

---

## 🗂️ Project Structure

```bash
requirements-traceability-lab/
│
├── data/
│   ├── requirements.csv         # A list of sample requirements
│   └── test_cases.csv           # A list of matching test cases
│
├── script/
│   └── traceability_nlp.py      # Python script to generate traceability links
│
├── notebook/
│   └── traceability_nlp.ipynb   # Jupyter notebook version (interactive)
│
├── sample_output/
│   └── traceability_matrix.csv  # Output file with similarity scores
│
├── requirements.txt             # List of Python packages
└── README.md                    # You're reading it!
```bash

---

## 🚀 Getting Started

1. Clone This Repository
```bash
git clone https://github.com/yourusername/requirements-traceability-lab.git
cd requirements-traceability-lab

## 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

## 3. Install the Required Packages
```bash
pip install -r requirements.txt

---

## 📘 How to Use
** Option A: Run the Python Script
```bash
python scripts/traceability_nlp.py

* Outputs similarity scores in the terminal
* Generates traceability_matrix.csv in sample_output/

** Option B: Explore with Jupyter Notebook
Launch the notebook environment:
```bash
jupyter notebook

Then open:
```bash
notebooks/traceability_nlp.ipynb

You'll see step-by-step code cells where you can:
* Load and explore the data
* Run and modify NLP models
* Visualize results interactively

---

## 📁 About the Input Files
Each row contains a short statement. Your task is to automatically match requirements to test cases using similarity analysis.
```bash
requirements.csv
| ID | Requirement Description                 |
| -- | --------------------------------------- |
| R1 | The system shall allow users to log in. |

```bash
test_cases.csv
| ID | Test Case Description                              |
| -- | -------------------------------------------------- |
| T1 | Check login functionality using valid credentials. |

---

## 🧠 Tools & Techniques
This lab uses:
* TF-IDF Vectorisation to turn text into numerical vectors.
* Cosine Similarity is used to measure how closely two pieces of text relate.

---

## ✅ Output
You'll receive:
* A traceability matrix of similarity scores between requirements and test cases.
* A table of recommended trace links (if score > threshold).

---

## 🙋 Need Help?
Don’t hesitate to ask your instructor or peers. You're encouraged to modify the code and explore how changes affect results.

---

## 📜 License
This project is open-source and available under the **[MIT License](LICENSE)**. Feel free to use or adapt for educational purposes. 
