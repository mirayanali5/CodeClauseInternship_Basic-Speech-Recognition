import whisper
import ffmpeg

# Load Whisper model (small, medium, or large based on system capacity)
model = whisper.load_model("base")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]
