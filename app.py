import streamlit as st
from utils.api_client import ask_google_ai

st.set_page_config(page_title="JangirAI", page_icon="🤖", layout="centered")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🤖 JangirAI")
    st.markdown(
        """
        Welcome! Chat with a Google AI-powered assistant.
        
        - 💬 Type your message below
        - 🧹 Use 'Clear Chat' to start over
        - 🚀 Powered by Google AI Studio & Streamlit
        """
    )
    if st.button("🧹 Clear Chat"):
        st.session_state.history = []

# --- HEADER STYLES & DRAGGABLE JS ---
st.markdown(
    """
    <style>
    .draggable-header {
        position: absolute;
        top: 1px;
        left: 50%;
        transform: translateX(-50%);
        width: 55vw;
        max-width: 500px;
        background: #22223b;
        z-index: 1000;
        padding: 12px 16px 10px 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.10);
        border: 1.5px solid #4a4e69;
        border-radius: 10px;
        text-align: center;
        color: #fff;
        cursor: move;
        overflow-wrap: break-word;
        word-break: break-word;
        user-select: none;
    }
    .draggable-header h1 {
        margin-bottom: 0.2rem;
        font-size: 1.5rem;
        color: #f2e9e4;
    }
    .draggable-header p {
        margin-top: 0;
        color: #c9ada7;
        font-size: 1rem;
    }
    .main-content {
        margin-top: 180px; /* Increased from 120px */
    }
    @media (max-width: 800px) {
        .draggable-header {
            width: 98vw;
            max-width: 98vw;
            padding: 10px 2vw 8px 2vw;
        }
        .main-content {
            margin-top: 200px; /* Increased from 140px */
        }
    }
    </style>
    <script>
    // Draggable header logic
    window.onload = function() {
        var header = document.getElementById('draggable-header');
        var offsetX = 0, offsetY = 0, mouseX = 0, mouseY = 0;
        if(header){
            header.onmousedown = dragMouseDown;
        }
        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            mouseX = e.clientX;
            mouseY = e.clientY;
            document.onmouseup = closeDragElement;
            document.onmousemove = elementDrag;
        }
        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            offsetX = mouseX - e.clientX;
            offsetY = mouseY - e.clientY;
            mouseX = e.clientX;
            mouseY = e.clientY;
            header.style.top = (header.offsetTop - offsetY) + "px";
            header.style.left = (header.offsetLeft - offsetX) + "px";
            header.style.transform = "none";
        }
        function closeDragElement() {
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
    </script>
    """,
    unsafe_allow_html=True,
)

# --- MAIN HEADER (DRAGGABLE) ---
st.markdown(
    """
    <div class="draggable-header" id="draggable-header">
        <h1>JangirAI</h1>
        <p>Your AI assistant, powered by Google</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- CHAT UI ---
def render_messages():
    for chat in st.session_state.history:
        if chat["role"] == "user":
            with st.chat_message("user", avatar="🧑"):
                st.markdown(chat["message"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(chat["message"])

def add_message(user_input):
    st.session_state.history.append({"role": "user", "message": user_input})
    with st.spinner("Bot is typing..."):
        try:
            response = ask_google_ai(user_input)
            if hasattr(response, "text"):
                response_text = response.text
            else:
                response_text = str(response)
            st.session_state.history.append({"role": "assistant", "message": response_text})
        except Exception as e:
            st.session_state.history.append({"role": "assistant", "message": f"API error: {e}"})

# --- MAIN CONTENT CONTAINER ---
with st.container():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown('<div class="scrollable-chat">', unsafe_allow_html=True)
    render_messages()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FIXED INPUT BOX ---
user_input = st.chat_input(
    "Type your message...",
    key="user_input"
)
if user_input and user_input.strip():
    add_message(user_input.strip())
    st.rerun()
