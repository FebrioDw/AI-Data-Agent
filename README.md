# 📉 Automated Data Insights Dashboard

An interactive, AI-powered data analytics workspace built with **Streamlit**, **LangChain**, and **Google Generative AI**. This application allows users to upload raw business datasets (CSV) and perform conversational analytics using natural language queries.

## 🚀 Features
* **Automated EDA**: Instantly view summary statistics, dataset structure, and missing values.
* **Conversational Analytics**: Ask complex business questions in plain English (or Indonesian). The LangChain agent translates your intent into Pandas code and executes it in an isolated environment.
* **Tool-Calling Architecture**: Utilizes advanced tool-calling for stable, fast, and accurate output parsing.

## ⚠️ Prerequisite: Bring Your Own Key (BYOK)
This project uses Google's Gemini API. To run this application, you must provide your own API key. 
1. Get your free API key from Google AI Studio.
2. You will need to insert this key during the local setup.

## 💻 How to Run Locally

1. Clone the repository
git clone https://github.com/FebrioDw/AI-Data-Agent.git
cd AI-Data-Agent

2. Install dependencies
Make sure you have Python installed, then run:
pip install -r requirements.txt

3. Setup Environment Variables
Create a new file named .env in the root directory and add your Google API Key:
GOOGLE_API_KEY=your_google_api_key_here
(Note: The .env file is ignored by Git to keep your credentials secure).

4. Launch the application
streamlit run app.py

## 🛠️ Tech Stack
* Frontend: Streamlit
* AI Agent: LangChain (create_pandas_dataframe_agent)
* LLM: Google Gemini Flash (ChatGoogleGenerativeAI)
* Data Manipulation: Pandas
