# 📈 AI Multi-Agent Financial Research System

An agentic AI system that autonomously researches any stock and generates a professional investment report — powered by **CrewAI**, **Google Gemini 2.5 Flash**, and real-time financial data.

---

## 🚀 Demo

Enter any stock ticker (e.g. `AAPL`, `TSLA`, `GOOGL`) and 4 specialized AI agents will automatically collaborate to produce a full research report in seconds.

---

## 🤖 How It Works

This project uses a **multi-agent architecture** where 4 AI agents work sequentially, each building on the previous agent's output:

```
You enter a ticker (e.g. AAPL)
        ↓
🔍 News Agent       → searches latest financial news from the web
📊 Data Agent       → fetches live stock price, PE ratio, market cap & more
🧠 Analysis Agent   → analyzes both news and data to form an investment view
📝 Report Agent     → writes a structured, professional research report
        ↓
Full investment report delivered in your browser
```

No human intervention between steps — the agents reason, act, and pass context autonomously.

---

## 🧠 What Makes It Agentic?

- **Autonomy** — agents decide how to achieve their goal without being told step by step
- **Tool Use** — agents actively use real-world tools (web search, Yahoo Finance API)
- **Multi-step Reasoning** — each agent builds on the previous one's findings
- **Role-based Collaboration** — specialized agents work as a team, just like humans would

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [CrewAI](https://crewai.com) | Multi-agent orchestration framework |
| [Google Gemini 2.5 Flash](https://aistudio.google.com) | LLM powering all agents |
| [yfinance](https://pypi.org/project/yfinance/) | Real-time stock data from Yahoo Finance |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Free web search for financial news |
| [Streamlit](https://streamlit.io) | Web interface |
| [Python Dotenv](https://pypi.org/project/python-dotenv/) | Secure API key management |

---

## 📁 Project Structure

```
finance-agent/
├── tools.py      # Tools agents use (news search, stock data fetching)
├── agents.py     # 4 specialized AI agents and their roles
├── tasks.py      # Task definitions and context flow between agents
├── crew.py       # Crew orchestration — wires agents and tasks together
├── app.py        # Streamlit web UI
└── .env          # API keys (not included in repo)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/finance-agent.git
cd finance-agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install crewai crewai-tools yfinance streamlit duckduckgo-search python-dotenv langchain-google-genai
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
Get your free Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📊 Sample Output

The system generates a structured report with the following sections:

- **Executive Summary**
- **Latest News**
- **Key Financial Metrics**
- **Analysis**
- **Conclusion & Recommendation**

---

## 🆓 Completely Free to Run

This project uses only free-tier APIs and open-source libraries. No paid subscriptions required.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only** and does not constitute financial advice. Always do your own research before making investment decisions.

---

