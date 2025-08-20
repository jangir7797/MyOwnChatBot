import streamlit as st
from utils.api_client import ask_google_ai

st.set_page_config(page_title="ChatGPT-style Chatbot", page_icon="🤖")

st.markdown("<h1 style='text-align:center;'>ChatGPT-style Chatbot</h1>", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

def add_message(user_input):
    try:
        response = ask_google_ai(user_input)
        st.session_state.history.append({"role": "user", "message": user_input})
        st.session_state.history.append({"role": "bot", "message": response})
    except Exception as e:
        st.error(f"API error: {e}")

# Chat message rendering with styled bubbles
def render_messages():
    for chat in st.session_state.history:
        if chat["role"] == "user":
            st.markdown(
                f"""
                <div style="
                    background-color:#dcf8c6;
                    border-radius:10px;
                    padding: 10px 15px;
                    width: 60%;
                    margin-left:auto;
                    margin-bottom: 10px;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                ">
                <b>You:</b><br>{chat["message"]}
                </div>""",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    background-color:#f1f0f0;
                    border-radius:10px;
                    padding: 10px 15px;
                    width: 60%;
                    margin-right:auto;
                    margin-bottom: 10px;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                ">
                <b>Bot:</b><br>{chat["message"]}
                </div>""",
                unsafe_allow_html=True
            )

# User input form fixed at bottom with full width
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your message...", label_visibility="collapsed")
    submit = st.form_submit_button("Send")

if submit and user_input:
    add_message(user_input)

render_messages()

# Add some spacing at bottom for input comfort
st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
