import gradio as gr
import whisper

def speech_to_text(tmp_filename,model_size):
    model = whisper.load_model(model_size)
    # model = whisper.load_model('large-v3')
    # audio = whisper.load_audio(tmp_filename)
    # _, probs = model.detect_language(audio)
    # lang = max(probs, key=probs.get)
    result = model.transcribe(tmp_filename)
    return result["text"]


gr.Interface(
    fn=speech_to_text,
    inputs=[gr.Audio(sources=['microphone'], type="filepath"), gr.Dropdown(choices=["tiny", "base", "small", "medium", "large"])],
    outputs='text').launch()