import streamlit as st
import speech_recognition as sr

# Page config
st.set_page_config(page_title="🎧 Speech Recognition", layout="centered")

# Custom CSS for glassmorphism and dark UI
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .main {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("## 🔊 Real-Time Speech Recognition")
st.markdown("#### 🎙️ Speak a command and get instant transcription.")

# Start Listening
if st.button("🎤 Tap to Speak"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("🔎 Listening... Please speak clearly"):
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio)
        st.success("✅ Recognized Speech:")
        st.markdown(f"**📝 `{text}`**")
    except sr.UnknownValueError:
        st.error("⚠️ Sorry, couldn't understand your voice.")
    except sr.RequestError:
        st.error("🚫 Could not connect to Google's service. Check your internet.")

st.markdown("</div>", unsafe_allow_html=True)
