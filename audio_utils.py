import librosa
import soundfile as sf
import numpy as np
import torch
import os
from df.enhance import enhance, init_df, load_audio, save_audio

# Singletons to save RAM
_df_model = None
_df_state = None

def remove_noise(input_path: str, output_path: str):
    """Integrated DeepFilterNet2 Noise Removal"""
    global _df_model, _df_state
    if _df_model is None:
        _df_model, _df_state, _ = init_df()
    
    audio, _ = load_audio(input_path, sr=_df_state.sr())
    enhanced = enhance(_df_model, _df_state, audio)
    save_audio(output_path, enhanced, _df_state.sr())

def change_speed(input_path: str, output_path: str, speed: float):
    """Adjusts speed using librosa 0.9.2"""
    y, sr = librosa.load(input_path, sr=None)
    y = y.astype(np.float32)
    
    if speed != 1.0:
        # FIX: Added 'rate=' to solve the positional argument error
        y_stretched = librosa.effects.time_stretch(y, rate=speed)
    else:
        y_stretched = y
        
    sf.write(output_path, y_stretched, sr)