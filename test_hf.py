import os
import gradio as gr
# MODELSCOPE.CN
# from modelscope.hub.snapshot_download import snapshot_download
# from modelscope import AutoTokenizer, AutoModel
# HUGGINGFACE.CO
# from huggingface_hub import snapshot_download
# from transformers import AutoTokenizer, AutoModel

# MODEL_HUB = 'huggingface'

# MODEL_NAME_DICT = {
#     'modelscope': 'ZhipuAI/chatglm3-6b',
#     'huggingface': 'THUDM/chatglm3-6b',
# }
# modelname = MODEL_NAME_DICT[MODEL_HUB]
# print('modelname: ', modelname)

# modelscope
# MODELSCOPE_CACHE_PATH = os.environ.get('MODELSCOPE_CACHE')
# print('MODELSCOPE_CACHE_PATH: ', MODELSCOPE_CACHE_PATH)
# HUGGINGFACE.CO

# HF_HOME_PATH = os.environ.get('HF_HOME')
# print('HF_HOME_PATH: ', HF_HOME_PATH)

# MODEL_PATH = snapshot_download(modelname)
# print('MODEL_PATH: ', MODEL_PATH)
# tokenizer = AutoTokenizer.from_pretrained(modelname, trust_remote_code=True)
# model = AutoModel.from_pretrained(modelname, trust_remote_code=True).quantize(4).cuda().eval()


def chat(message, history):
    history = [] if history else history
    response, history = model.chat(tokenizer, message, history=history)
    return response, history


def main():
    demo = gr.Interface(fn=chat, inputs=gr.Text(), outputs=[gr.Text(),gr.Text()])
    demo.launch()
    return


if __name__ == '__main__':
    # main()
    demo = gr.load("Helsinki-NLP/opus-mt-en-es", src="models")

    demo.launch()