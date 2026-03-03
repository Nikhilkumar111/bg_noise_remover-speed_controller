import whisper

_model = None

def speech_to_text(audio_path: str) -> str:
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    
    # fp16=False allows it to run on CPU
    result = _model.transcribe(audio_path, fp16=False)
    return result["text"]