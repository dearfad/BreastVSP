import gradio as gr
from libs.info.vsp import get_patient_info


def get_vsp():
    breastvsp = get_patient_info()

    photo = './patient.jpeg'
    infotext = f'''
                        ## {breastvsp.name}
                        #### 年龄：{breastvsp.age}岁
                        #### 地址：{breastvsp.address}
                        '''
    
    return photo, infotext

def chat(message, history):
    return message

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            photo = gr.Image(height=400)
            info = gr.Markdown()
            change_patient_btn = gr.Button(value='随机患者')
            change_patient_btn.click(get_vsp, outputs=[photo,info])
        with gr.Column(scale=2):
            gr.ChatInterface(chat)


if __name__ == '__main__':
    demo.launch(share=True)
