import whisper

_model = None

def speech_to_text(audio_path: str) -> str:
    global _model
    if _model is None:
        _model = whisper.load_model("base.en")
    
    # language="en" ensures no translation errors
    result = _model.transcribe(audio_path, fp16=False, language="en")
    return result["text"].strip()