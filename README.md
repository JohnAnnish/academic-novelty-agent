# 🔬 Academic Novelty Checker Agent

An autonomous Full-Stack AI Agent designed to streamline academic literature reviews and assess the novelty of proposed research pipelines. Built with a modern Agentic Workflow, this tool leverages live internet search and Large Language Models to compare user-provided abstracts against published papers.

## 🚀 Features

- **Agentic AI Workflow:** Utilizes **LangGraph** to autonomously formulate search queries and execute function calls.
- **Live Literature Search:** Integrates **SerpApi** to dynamically scrape and analyze abstracts from Google Scholar.
- **Novelty Assessment:** Automatically generates detailed, cited Markdown reports outlining structural similarities, novelty ratings, and recommendations for improvement.
- **Full-Stack Architecture:** 
  - **Backend:** A robust **FastAPI** Python server handling the LangChain/LangGraph agent loops.
  - **Frontend:** A modern, responsive **React (Vite)** web application featuring a sleek Glassmorphism UI.

## 🛠️ Tech Stack

- **AI Framework:** LangChain, LangGraph
- **LLM:** Google Gemini Flash (3.6) / OpenAI GPT-4o-mini
- **Backend Server:** Python, FastAPI, Uvicorn
- **Frontend UI:** React, Vite, CSS (Glassmorphism), React-Markdown
- **External Tools:** SerpApi (Google Scholar Search)

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/academic-novelty-agent.git
cd academic-novelty-agent
```

### 2. Set up the Backend (FastAPI + AI Agent)
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
*Create a `.env` file in the root directory and add your API keys:*
```env
GOOGLE_API_KEY="your_gemini_key"
SERPAPI_API_KEY="your_serpapi_key"
```
*Start the backend server:*
```bash
python api.py
```

### 3. Set up the Frontend (React UI)
Open a new terminal window:
```bash
cd frontend
npm install
npm run dev
```

## 💡 How it Works
1. The user inputs a proposed research pipeline (e.g., *“Hybrid AI model using FCM, EfficientNet, and XGBoost for Leukemia detection”*).
2. The React frontend sends the payload to the FastAPI backend.
3. The LangGraph Agent extracts key methodologies and triggers the SerpApi tool to search Google Scholar.
4. The Agent cross-references the findings with the user's proposal and streams a Markdown-formatted Novelty Report back to the frontend UI.
