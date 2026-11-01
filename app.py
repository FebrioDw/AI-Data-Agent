import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# --- 1. UI CONFIGURATION ---
st.set_page_config(page_title="Data Analytics Workspace", page_icon="📉", layout="wide")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {margin-top: -50px;}
    </style>
    """, unsafe_allow_html=True)

active_model = "gemini-3.8-flash"

# --- 2. SIDEBAR LAYOUT ---
with st.sidebar:
    st.title("⚙️ Workspace Setup")
    st.write("Upload your business dataset to begin automated processing.")
    uploaded_file = st.file_uploader("Data Source (CSV)", type=["csv"])
    st.markdown("---")
    st.success(f"🟢 Google Engine: **{active_model}**")
    st.caption("Powered by Google Generative AI")

# --- 3. MAIN DASHBOARD ---
st.title("📉 Automated Data Insights Dashboard")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    tab1, tab2 = st.tabs(["📋 Data Preview", "🤖 Analytics Console"])
    
    with tab1:
        st.subheader("Dataset Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())
        
        st.markdown("---")
        st.dataframe(df.head(10), use_container_width=True)
        
    with tab2:
        st.subheader("Query Your Data")
        user_question = st.text_input("Enter your command (e.g., 'Sum the revenue by region', 'Find the missing values'):")
        
        if user_question:
            with st.spinner("Processing query execution..."):
                try:
                    llm = ChatGoogleGenerativeAI(temperature=0, model=active_model, api_key=google_api_key)
                    
                    agent = create_pandas_dataframe_agent(
                        llm, 
                        df, 
                        verbose=True, 
                        allow_dangerous_code=True,
                        agent_type="tool-calling",
                        agent_executor_kwargs={"handle_parsing_errors": True}
                        
                    )
                    
                    forced_prompt = user_question + " \n(Provide only the final clear answer directly in Indonesian)."
                    response = agent.invoke(forced_prompt)
                    
                    raw_output = response["output"]
                    if isinstance(raw_output, list) and len(raw_output) > 0 and isinstance(raw_output[0], dict):
                        clean_output = raw_output[0].get("text", str(raw_output))
                    elif isinstance(raw_output, dict):
                        clean_output = raw_output.get("text", str(raw_output))
                    else:
                        clean_output = str(raw_output)
                        
                    st.success("Query Executed Successfully")
                    st.info(clean_output)
                except Exception as e:
                    st.error(f"Execution Error: {e}")
else:
    # --- WELCOME SCREEN ---
    st.write("Streamline your reporting process. Upload data on the left panel to begin.")
    st.markdown("---")
    
    st.subheader("🚀 Platform Capabilities")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Automated EDA**\n\nInstantly generate summary statistics, detect missing values, and understand your dataset structure without writing a single line of Python.")
    with col2:
        st.info("**Conversational Analytics**\n\nAsk complex business questions in plain English. The AI agent translates your intent into Pandas code and executes it in real-time.")
    with col3:
        st.info("**Enterprise Grade**\n\nPowered by advanced LLMs with an isolated execution environment for secure data manipulation and seamless analysis.")
        
    st.markdown("### 💡 How to start?")
    st.write("1. Prepare your `.csv` file (e.g., Sales Data, Inventory, Customer Records).")
    st.write("2. Drag and drop the file into the sidebar on the left.")
    st.write("3. Navigate to the **Analytics Console** tab and start asking questions!")