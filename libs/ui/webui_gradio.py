import gradio as gr
from libs.models.mscope import get_model
from libs.models.mscope import get_model

tokenizer, model = get_model()
def chat(message, history):
    response, history = model.chat(tokenizer, message, history=history)
    return response, history
history = []
demo = gr.ChatInterface(fn=chat)
demo.launch()