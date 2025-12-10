import sounddevice as sd
import numpy as np
import whisper
import time


SAMPLE_RATE = 16000        
CHUNK_DURATION = 5        

print("⏳ Loading Whisper model (small)...")
model = whisper.load_model("small")
print("✅ Whisper loaded.\n")

def record_audio(duration=CHUNK_DURATION):
    """Record audio from microphone for given duration."""
    print(f"🎙 Speak now ({duration} seconds)...")
    audio = sd.rec(int(duration * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1,
                   dtype='float32')
    sd.wait()
    return audio.flatten()

def transcribe(audio_data):
    """Convert audio to English text using Whisper."""
    
    result = model.transcribe(audio_data, task="translate")
    return result["text"]

if __name__ == "__main__":
    print("▶️ Voice-to-Caption system started. Press Ctrl + C to stop.\n")

    try:
        while True:
            audio = record_audio()
            text = transcribe(audio)
            print(f"📝 Caption: {text}\n")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
