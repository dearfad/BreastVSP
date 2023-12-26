# from libs.asr.speechrecognition import listen
# from libs.tts.edge import say
# from modelscope import AutoTokenizer, AutoModel, snapshot_download
import gradio as gr
from transformers import AutoTokenizer, AutoModel

def test(name):
    return 'A'

if __name__=='__main__':

    model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision = "v1.0.0")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).quantize(8).cuda()
    model = model.eval()


    history = []
    while True:
        message = listen()
        print(message)
        response, history = model.chat(tokenizer, message, history=history)
        print(response)
        say(response)
