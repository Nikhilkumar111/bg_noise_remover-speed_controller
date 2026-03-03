import os
import sys

# CRITICAL: This MUST be the first thing in the script
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import warnings
import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Import our custom modules
from audio_utils import change_speed, remove_noise
from stt import speech_to_text
from tts import text_to_speech

warnings.filterwarnings("ignore")



# Create folder for audio files
OUTPUT_DIR = "outputs"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

RAW_AUDIO = os.path.join(OUTPUT_DIR, "1_raw.wav")
SPEED_AUDIO = os.path.join(OUTPUT_DIR, "2_speed.wav")
CLEAN_AUDIO = os.path.join(OUTPUT_DIR, "3_clean.wav")
TTS_AUDIO = os.path.join(OUTPUT_DIR, "4_tts_result.wav")



st.set_page_config(page_title="AI Voice Pipeline", layout="centered", page_icon="🎙️")
st.title("🎙️ AI Voice Processing Pipeline")

with st.sidebar:
    st.header("Settings")
    speed_val = st.slider("🎚 Input Speed Adjustment", 0.5, 2.0, 1.0, 0.1)

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="🛑 Stop Recording",
    just_once=False,
    use_container_width=True
)

if audio:
    with open(RAW_AUDIO, "wb") as f:
        f.write(audio["bytes"])

    with st.spinner("🎚 Changing Speed..."):
        try:
            change_speed(RAW_AUDIO, SPEED_AUDIO, speed_val)
        except Exception as e:
            st.error(f"Speed Error: {e}")
            SPEED_AUDIO = RAW_AUDIO

    with st.spinner("🧹 Cleaning Background Noise..."):
        try:
            remove_noise(SPEED_AUDIO, CLEAN_AUDIO)
            st.success("✅ Noise Removed Successfully")
            st.audio(CLEAN_AUDIO)
        except Exception as e:
            st.error(f"DeepFilterNet Error: {e}")
            CLEAN_AUDIO = SPEED_AUDIO

    with st.spinner("📝 Transcribing..."):
        text = speech_to_text(CLEAN_AUDIO)
        if text:
            st.text_area("Recognized Text", text, height=100)
            
            with st.spinner("🔊 Generating AI Voice..."):
                try:
                    text_to_speech(text, TTS_AUDIO)
                    st.audio(TTS_AUDIO)
                    with open(TTS_AUDIO, "rb") as f:
                        st.download_button("⬇️ Download Result", f, file_name="ai_output.wav")
                except Exception as e:
                    st.error(f"TTS Error: {e}")