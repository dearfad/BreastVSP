import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=0):
            llm = gr.Checkbox(label='语言模型')
            model = gr.Dropdown(
                ['THUDM/chatglm3-6b', 'ZhipuAI/chatglm3-6b'], label='模型选择')
            micphone = gr.Checkbox(label='麦克风输入')
            asr = gr.Dropdown(['openai/whisper'], label='语音识别')
            voice = gr.Checkbox(label='语音输出')
            tts = gr.Dropdown(['rany2/edge-tts'], label='发音模型')
            tts_voice = gr.Dropdown(['zh-CN-XiaoxiaoNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-liaoning-XiaobeiNeural',
                                     'zh-CN-shaanxi-XiaoniNeural', 'zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-TW-HsiaoChenNeural', 'zh-TW-HsiaoYuNeural'], label="'语音选择")
        with gr.Column(scale=1):
            photo = gr.Image('patient.jpeg', height=380, show_label=False, show_download_button=False)
            info = gr.Textbox()
        with gr.Column(scale=2):
            out = gr.Textbox()

    with gr.Accordion("See Details"):
        gr.Markdown("lorem ipsum")

    # with st.container(border=True):
    #     patient = st.selectbox('患者信息', ['random'])

demo.launch(share=False)
