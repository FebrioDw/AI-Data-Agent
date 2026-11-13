# 📉 Automated Data Insights Dashboard

An interactive, AI-powered data analytics workspace built with **Streamlit**, **LangChain**, and the **Groq API**. This application allows users to upload raw business datasets (CSV) and perform conversational analytics using natural language queries.

### Active Model Engine
This AI Data Agent is powered by the **OpenAI GPT-OSS-120b** model as its core reasoning engine. By orchestrating this specific model through the Groq API, the agent achieves ultra-low latency inference while driving the ReAct (Reasoning and Acting) framework. This allows the system to accurately interpret complex natural language queries and dynamically generate executable Pandas code for seamless tabular data analysis.

## 🚀 Features
- **Automated EDA**: Instantly view summary statistics, dataset structure, and missing values.
- **Conversational Analytics**: Ask complex business questions in plain English (or Indonesian). The LangChain agent translates your intent into Pandas code and executes it in an isolated environment.
- **Tool-Calling Architecture**: Utilizes advanced tool-calling for stable, fast, and accurate output parsing.

## ⚠️ Prerequisite: Bring Your Own Key (BYOK)
This project uses the Groq API for ultra-fast LLM inference. To run this application, you must provide your own API key. 
1. Get your free API key from the [Groq Cloud Console](https://console.groq.com/).
2. You will need to insert this key during the local setup.

## 💻 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/FebrioDw/AI-Data-Agent.git](https://github.com/FebrioDw/AI-Data-Agent.git)
cd AI-Data-Agent
```

**2. Install dependencies**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

**3. Setup Environment Variables**
Create a new file named `.env` in the root directory and add your Groq API Key:
```text
GROQ_API_KEY=your_groq_api_key_here
```
*(Note: The `.env` file is ignored by Git to keep your credentials secure).*

**4. Launch the application**
```bash
streamlit run app.py
```

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI Agent**: LangChain (`create_pandas_dataframe_agent`)
- **LLM**: OpenAI GPT-OSS-120b via Groq API (`ChatGroq`)
- **Data Manipulation**: Pandas
