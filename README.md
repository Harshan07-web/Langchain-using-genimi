# Gemini LangChain Project

A hands-on project to explore the capabilities of LangChain using Google Gemini chat models. This project demonstrates chat models, prompt templates, chains, RAG (Retrieval-Augmented Generation), and agents.

## 🧠 Overview

This repository is a collection of modular scripts structured by:

- **Chat Models** (`1-chat_models`)  
- **Prompt Templates** (`2-prompt_templates`)  
- **Chains** (`3-chains`)  
- **RAG (Retrieval-Augmented Generation)** (`4-rag`)  
- **Agents** (`5-agents`)  

Each folder contains independent Python scripts demonstrating LangChain usage with Gemini.

## 🗂 Project Structure

```bash
.
├── 1-chat_models/
│   ├── 1st_chat_model_gemini.py
│   └── ...
├── 2-prompt_templates/
│   └── 1st_prompt_template.py
├── 3-chains/
│   ├── 1st_chain_model.py
│   └── ...
├── 4-rag/
│   ├── db/
│   ├── documents/
│   ├── 1st_rag_model.py
│   └── ...
├── 5-agents/
│   └── aganet.py
├── .env
├── .gitignore

⚙️ Setup
Clone the repository

git clone https://github.com/YOUR_USERNAME/gemini-langchain.git
cd gemini-langchain


Create a virtual environment and activate it

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies
pip install -r requirements.txt
Setup your .env file
Make sure your .env file contains:

GOOGLE_API_KEY=your_google_generative_ai_key

🚀 Running Examples
Each Python file is standalone and can be executed directly:

python 1-chat_models/1st_chat_model_gemini.py
Modify or run other files similarly to explore different concepts.

📁 RAG Setup
To use the RAG models, place your source files inside:

4-rag/documents/
The script will automatically index and query these documents.

🧠 Tech Stack
LangChain

Google Generative AI (Gemini)


