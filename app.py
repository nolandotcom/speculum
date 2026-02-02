import streamlit as st
from openai import OpenAI

# Silent Monastery UI
st.set_page_config(page_title="SPECULUM", layout="centered")
st.markdown("<style> .stApp {background-color: #000; color: #fff; font-family: monospace;} </style>", unsafe_allow_html=True)

# Securely fetch API key from Cloud Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("SPECULUM")
st.write("TRUTH OVER COMFORT")

if "history" not in st.session_state:
    st.session_state.history = []

# Core Protocol: Pattern -> Probe -> Reframe
SYSTEM_PROMPT = "You are SPECULUM. 1. ID Pattern. 2. Ask sharp question. 3. Reframe in one sentence. Clinical tone. No emojis."

user_input = st.chat_input("State your truth...")
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.history
    )
    msg = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": msg})
    for m in st.session_state.history:
        st.write(f"**{m['role'].upper()}**: {m['content']}")
      
