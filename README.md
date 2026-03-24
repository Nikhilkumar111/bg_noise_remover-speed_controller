<!-- 🎤 Mic (Streamlit)
        ↓
🎚 Speed Control (librosa / torchaudio)   ← applied to RAW mic audio
        ↓
📝 STT (Whisper)
        ↓
🔊 TTS (Coqui TTS)
        ↓
🔊 Play + Download (Streamlit)
        ↓
🔁 Loop (Speak again) -->



                                     Speed controller + background noise remover 

                                              🎤 Mic (Streamlit) 
                                                       ↓
🎚                                Speed Control (librosa / torchaudio)->"Libraries used"
                                                       ↓
                                        🧹 Noise Removal (DeepFilterNet2)
                                                       ↓
                                               📝 STT (Whisper)
                                                       ↓
                                               🔊 TTS (Coqui TTS)
                                                       ↓
                                             🔊 Play + Download (Streamlit)
                                                       ↓
                                              🔁 Loop (Speak again)









Processing time:
<!-- "The system took 29.88 seconds to complete the full audio processing pipeline" -->

Real-time-factor:
RTF=Audio Duration/Processing Time
	​
