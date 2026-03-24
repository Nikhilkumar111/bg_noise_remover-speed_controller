# import os
# import sys

# # CRITICAL: This MUST be the first thing in the script
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# import torch
# import warnings
# import streamlit as st
# from streamlit_mic_recorder import mic_recorder



# # Import our custom modules
# from audio_utils import change_speed, remove_noise
# from stt import speech_to_text
# from tts import text_to_speech

# warnings.filterwarnings("ignore")


# # Create folder for audio files
# OUTPUT_DIR = "outputs"
# if not os.path.exists(OUTPUT_DIR):
#     os.makedirs(OUTPUT_DIR)

# RAW_AUDIO = os.path.join(OUTPUT_DIR, "1_raw.wav")
# SPEED_AUDIO = os.path.join(OUTPUT_DIR, "2_speed.wav")
# CLEAN_AUDIO = os.path.join(OUTPUT_DIR, "3_clean.wav")
# TTS_AUDIO = os.path.join(OUTPUT_DIR, "4_tts_result.wav")


# st.set_page_config(page_title="AI Voice Pipeline", layout="centered", page_icon="🎙️")
# st.title("🎙️ AI Voice Processing Pipeline")

# st.markdown("This application records your voice, processes it, converts it to text, and generates an AI voice response.")

# # Sidebar settings
# with st.sidebar:
#     st.header("⚙️ Settings")
#     speed_val = st.slider("🎚 Input Speed Adjustment", 0.5, 2.0, 1.0, 0.1)


# # ---------------- RECORD AUDIO ----------------
# st.header("1️⃣ Record Your Voice")
# st.write("Click the button below to start recording your voice.")

# audio = mic_recorder(
#     start_prompt="🎤 Start Recording",
#     stop_prompt="🛑 Stop Recording",
#     just_once=False,
#     use_container_width=True
# )

# if audio:

#     st.success("✅ Recording Completed")

#     with open(RAW_AUDIO, "wb") as f:
#         f.write(audio["bytes"])

#     st.subheader("🎧 Original Recorded Voice")
#     st.audio(RAW_AUDIO)


#     # ---------------- SPEED CONTROL ----------------
#     st.header("2️⃣ Speed Controller")
#     st.write("Adjust the playback speed of your voice using the slider.")

#     with st.spinner("🎚 Changing Speed..."):
#         try:
#             change_speed(RAW_AUDIO, SPEED_AUDIO, speed_val)

#             st.subheader("🎚 Speed Adjusted Voice")
#             st.audio(SPEED_AUDIO)

#         except Exception as e:
#             st.error(f"Speed Error: {e}")
#             SPEED_AUDIO = RAW_AUDIO


#     # ---------------- NOISE REMOVAL ----------------
#     st.header("3️⃣ Noise Removal")
#     st.write("Background noise is removed from the audio using AI filtering.")

#     with st.spinner("🧹 Cleaning Background Noise..."):
#         try:
#             remove_noise(SPEED_AUDIO, CLEAN_AUDIO)

#             st.success("✅ Noise Removed Successfully")

#             st.subheader("🔊 Cleaned Audio")
#             st.audio(CLEAN_AUDIO)

#         except Exception as e:
#             st.error(f"DeepFilterNet Error: {e}")
#             CLEAN_AUDIO = SPEED_AUDIO


#     # ---------------- SPEECH TO TEXT ----------------
#     st.header("4️⃣ Speech to Text")
#     st.write("The cleaned audio is converted into text using a Speech Recognition model.")

#     with st.spinner("📝 Transcribing..."):
#         text = speech_to_text(CLEAN_AUDIO)

#         if text:
#             st.text_area("📝 Recognized Text", text, height=120)


#             # ---------------- TEXT TO SPEECH ----------------
#             st.header("5️⃣ AI Voice Generation")
#             st.write("The recognized text is converted back into speech using an AI voice model.")

#             with st.spinner("🔊 Generating AI Voice..."):
#                 try:
#                     text_to_speech(text, TTS_AUDIO)

#                     st.subheader("🤖 AI Generated Voice")
#                     st.audio(TTS_AUDIO)

#                     with open(TTS_AUDIO, "rb") as f:
#                         st.download_button(
#                             "⬇️ Download AI Voice",
#                             f,
#                             file_name="ai_output.wav"
#                         )

#                 except Exception as e:
#                     st.error(f"TTS Error: {e}")




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
st.title("🎙️ Open Source AI Voice Processing Pipeline")

st.markdown("This application records your voice, processes it, converts it to text, and generates an AI voice response.")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    speed_val = st.slider("🎚 Input Speed Adjustment", 0.5, 2.0, 1.0, 0.1)


# ---------------- INPUT SECTION ----------------
st.header("1️⃣ Provide Your Voice")

tab_record, tab_upload = st.tabs(["🎤 Record", "📂 Upload"])

audio_ready = False

with tab_record:
    st.write("Click the button below to start recording your voice.")

    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="🛑 Stop Recording",
        just_once=False,
        use_container_width=True
    )

    if audio:
        st.success("✅ Recording Completed")

        with open(RAW_AUDIO, "wb") as f:
            f.write(audio["bytes"])

        st.subheader("🎧 Original Recorded Voice")
        st.audio(RAW_AUDIO)
        audio_ready = True

with tab_upload:
    st.write("Upload a noisy audio file to process it through the pipeline.")

    uploaded_file = st.file_uploader(
        "Upload a noisy audio file",
        type=["wav", "mp3", "m4a", "ogg", "flac"]
    )

    if uploaded_file is not None:
        st.success("✅ File Uploaded Successfully")

        with open(RAW_AUDIO, "wb") as f:
            f.write(uploaded_file.read())

        st.subheader("🎧 Uploaded Voice")
        st.audio(RAW_AUDIO)
        audio_ready = True


if audio_ready:

    # ---------------- SPEED CONTROL ----------------
    st.header("2️⃣ Speed Controller")
    st.write("Adjust the playback speed of your voice using the slider.")

    with st.spinner("🎚 Changing Speed..."):
        try:
            change_speed(RAW_AUDIO, SPEED_AUDIO, speed_val)

            st.subheader("🎚 Speed Adjusted Voice")
            st.audio(SPEED_AUDIO)

        except Exception as e:
            st.error(f"Speed Error: {e}")
            SPEED_AUDIO = RAW_AUDIO


    # ---------------- NOISE REMOVAL ----------------
    st.header("3️⃣ Noise Removal")
    st.write("Background noise is removed from the audio using AI filtering.")

    with st.spinner("🧹 Cleaning Background Noise..."):
        try:
            remove_noise(SPEED_AUDIO, CLEAN_AUDIO)

            st.success("✅ Noise Removed Successfully")

            st.subheader("🔊 Cleaned Audio")
            st.audio(CLEAN_AUDIO)

        except Exception as e:
            st.error(f"DeepFilterNet Error: {e}")
            CLEAN_AUDIO = SPEED_AUDIO


    # ---------------- SPEECH TO TEXT ----------------
    st.header("4️⃣ Speech to Text")
    st.write("The cleaned audio is converted into text using a Speech Recognition model.")

    with st.spinner("📝 Transcribing..."):
        text = speech_to_text(CLEAN_AUDIO)

        if text:
            st.text_area("📝 Recognized Text", text, height=120)


            # ---------------- TEXT TO SPEECH ----------------
            st.header("5️⃣ AI Voice Generation")
            st.write("The recognized text is converted back into speech using an AI voice model.")

            with st.spinner("🔊 Generating AI Voice..."):
                try:
                    text_to_speech(text, TTS_AUDIO)

                    st.subheader("🤖 AI Generated Voice")
                    st.audio(TTS_AUDIO)

                    with open(TTS_AUDIO, "rb") as f:
                        st.download_button(
                            "⬇️ Download AI Voice",
                            f,
                            file_name="ai_output.wav"
                        )

                except Exception as e:
                    st.error(f"TTS Error: {e}")


