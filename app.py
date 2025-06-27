import streamlit as st
import tempfile
import whisper

# Load Whisper model
model = whisper.load_model("base")

# Page configuration
st.set_page_config(page_title="Audio2Text Pro | MP3 Transcription with Timestamps", layout="centered")

# Custom CSS for sleek look
st.markdown("""
    <style>
    body {
        background-color: #0F1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #1A1D24;
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #00B4D8;
        text-align: center;
    }
    .stButton>button {
        background-color: #00B4D8;
        color: white;
        border-radius: 5px;
        height: 3em;
        width: 10em;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0077B6;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎧 Audio2Text Transcription")

st.write("Upload your audio file below and get accurate text with timestamps.")

# File uploader
uploaded_file = st.file_uploader("🔽 Upload an MP3 File", type=["mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')
    
    if st.button("🚀 Transcribe Now"):
        with st.spinner("Transcribing audio, please wait..."):
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_audio_path = temp_audio.name
            
            # Transcription with timestamps
            result = model.transcribe(temp_audio_path, word_timestamps=False)

            st.success("✅ Transcription Completed!")

            st.subheader("📝 Full Transcription")
            st.text_area("", result["text"], height=200)

            st.subheader("🕒 Segment-wise Timestamps")
            for segment in result["segments"]:
                start = round(segment["start"], 2)
                end = round(segment["end"], 2)
                text = segment["text"]
                st.info(f"[{start}s - {end}s]: {text}")
