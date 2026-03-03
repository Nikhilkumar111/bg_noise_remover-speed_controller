from TTS.api import TTS

_tts_model = None

def text_to_speech(text: str, output_path: str):
    global _tts_model
    if _tts_model is None:
        # Fast, CPU-friendly model
        _tts_model = TTS(model_name="tts_models/en/ljspeech/vits", progress_bar=False, gpu=False)
    
    _tts_model.tts_to_file(text=text, file_path=output_path)