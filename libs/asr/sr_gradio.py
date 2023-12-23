import gradio as gr
import speech_recognition as sr

def listen(temp):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    print('recognition')
    message = r.recognize_whisper(audio, model="base", language="chinese")
    return message

gr.Interface(fn=listen, inputs='text', outputs='text').launch()