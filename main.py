import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

st.title("SmartStudyGuide")

load_dotenv()

AI71_BASE_URL = "https://api.ai71.ai/v1/"
AI71_API_KEY = os.getenv("AI71_API_KEY")


def generate_response(input_text):
    
    chat = ChatOpenAI(
        model="tiiuae/falcon-180B-chat",
        api_key=AI71_API_KEY,
        base_url=AI71_BASE_URL,
        streaming=True,
    )
    st.info(chat.invoke(input_text).content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "",
    )
    submitted = st.form_submit_button("Submit")
    if not AI71_API_KEY.startswith("api71"):
        st.warning("Please enter your AI71 API key!", icon="⚠")
    if submitted and AI71_API_KEY.startswith("api71"):
        generate_response(text)