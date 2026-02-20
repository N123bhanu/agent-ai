# 🤖 Agent-AI (Google ADK Based AI Agent)

A simple AI Agent built using **Google Agent Development Kit (ADK)** and **Gemini Model**.  
This project demonstrates how to create and run an AI agent using modern LLM infrastructure.

---

## 🚀 Project Overview

This project contains a root agent that:

- Uses Google ADK framework
- Connects to Gemini model (`gemini-2.0-flash`)
- Provides clear and concise responses
- Runs interactively via CLI

---

## 🛠️ Tech Stack

- Python 3.13
- Google ADK
- Gemini 2.0 Flash Model
- Virtual Environment (uv)
- Git & GitHub

---

## 📂 Project Structure

```
agent-ai/
│
├── my_first_agent/
│   ├── __init__.py
│   ├── agent.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/N123bhanu/agent-ai.git
cd agent-ai
```

### 2️⃣ Create Virtual Environment

```
uv venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
uv pip install -r requirements.txt
```

### 4️⃣ Set API Key

Set your Gemini API key as environment variable:

```
setx GOOGLE_API_KEY "your_api_key_here"
```

Restart terminal after setting.

### 5️⃣ Run Agent

```
adk run my_first_agent
```

---

## 🧠 How It Works

1. ADK initializes the root agent.
2. The agent connects to Gemini model.
3. User input is sent to the LLM.
4. Model generates response.
5. Response is displayed in CLI.

---

## 📈 Learning Outcomes

- LLM Integration
- API Key Management
- Virtual Environment Handling
- Git & Version Control
- AI Agent Architecture

---

## ⚠️ Important Notes

- Ensure billing/quota is enabled for Gemini API.
- Never upload API keys to GitHub.
- `.venv` and `.adk` folders are ignored via `.gitignore`.

---

## 👨‍💻 Author

**Nunna Bhanu Shankar**  
GitHub: https://github.com/N123bhanu

---

## ⭐ Future Improvements

- Add tool integrations
- Add memory persistence
- Build Web UI using FastAPI or Streamlit
- Deploy on Cloud (GCP / AWS)
- Add CI/CD pipeline
