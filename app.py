import streamlit as st
import pandas as pd
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

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

# Active Model Engine
active_model = "openai/gpt-oss-120b"

# --- 2. SIDEBAR LAYOUT ---
with st.sidebar:
    st.title("⚙️ Workspace Setup")
    st.write("Upload your business dataset to begin automated processing.")
    uploaded_file = st.file_uploader("Data Source (CSV)", type=["csv"])
    st.markdown("---")
    st.success(f"🟢 Groq Engine: **{active_model}**")

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
                    # Initialize LLM
                    llm = ChatGroq(
                        temperature=0, 
                        model_name=active_model, 
                        groq_api_key=groq_api_key,
                        max_tokens=8000
                    )
                    
                    data_context = df.head(50).to_csv(index=False)
                    
                    
                    pesan_sistem = SystemMessage(content="You are a smart data analyst. Perform data aggregation and calculations quickly based ONLY on the provided CSV data. DO NOT print, write, or explain step-by-step mathematical additions. Provide only the final conclusion directly in English. If the format requires a list or ranking, you MUST use a Markdown table.")
                    pesan_user = HumanMessage(content=f"Sales Data:\n{data_context}\n\nQuestion: {user_question}")
                    
                    response = llm.invoke([pesan_sistem, pesan_user])
                    
                    hasil_teks = response.content
                    proses_berpikir = response.additional_kwargs.get("reasoning_content", "")
                        
                    st.success("Query Executed Successfully")
                    
                    
                    if proses_berpikir:
                        with st.expander("🧠 View AI Reasoning Chain"):
                            st.write(proses_berpikir)
                            
                    st.markdown("### 📊 Analysis Result:")
                    
        
                    if not hasil_teks or hasil_teks.strip() == "":
                        if proses_berpikir:
                            st.info("Note: The final answer was not summarized, but you can view the complete analysis in the 'View AI Reasoning Chain' menu above.")
                        else:
                            st.warning("Warning: The model processed without error, but refused to provide a text response.")
                    else:
                        st.info(hasil_teks)
                        
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