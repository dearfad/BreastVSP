import gradio as gr
from libs.info.vsp import get_patient_info
from libs.models.mscope import get_model

tokenizer, model = get_model()


def get_vsp():
    breastvsp = get_patient_info()

    photo = './patient.jpeg'
    infotext = f'''
                        ## {breastvsp.name}
                        #### 年龄：{breastvsp.age}岁
                        #### 地址：{breastvsp.address}
                        '''
    
    return photo, infotext
    # return infotext

def chat(message, history):
    response, history = model.chat(tokenizer, message, history=history)
    return response['content']

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            photo = gr.Image(height=400, show_label=False, show_download_button=False, container=False)
            info = gr.Markdown()
            change_patient_btn = gr.Button(value='随机患者')
            change_patient_btn.click(get_vsp, outputs=[photo,info])
            # change_patient_btn.click(get_vsp, outputs=info)
        with gr.Column(scale=2):
            gr.ChatInterface(chat)


if __name__ == '__main__':
    demo.launch(share=False)
