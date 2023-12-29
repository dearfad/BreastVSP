import streamlit as st
from libs.models.hface import get_model
# from libs.asr.speechrecognition import listen
# from libs.tts.edge import say
from libs.info.vsp import get_patient_info
# import speech_recognition as sr

st.set_page_config(
    page_title="乳腺外科虚拟病人",
    page_icon="👩",
    layout='wide',
    initial_sidebar_state='expanded',
)


with st.sidebar:
    st.title('👩 - BreastVSP -')
    with st.container(border=True):
        llm = st.toggle('大语言模型')
        model = st.selectbox('语言模型', ['THUDM/chatglm3-6b'])
    with st.container(border=True):
        micphone = st.toggle('麦克风输入')
        asr = st.selectbox('语音识别', ['openai/whisper'])
    with st.container(border=True):
        voice = st.toggle('语音输出')
        tts = st.selectbox('发音模型', ['rany2/edge-tts'])
        tts_voice = st.selectbox('语音选择', ['zh-CN-XiaoxiaoNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-liaoning-XiaobeiNeural',
                                 'zh-CN-shaanxi-XiaoniNeural', 'zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-TW-HsiaoChenNeural', 'zh-TW-HsiaoYuNeural'])
    with st.container(border=True):
        patient = st.selectbox('患者信息', ['random'])


info_col, empty_col, chat_col, right_col = st.columns([1, 1, 3, 1])

if "patient" in st.session_state:
    pass
else:
    st.session_state.patient = get_patient_info()


with info_col:
    st.image('patient.jpeg')
    st.markdown(f'''
            #### {st.session_state.patient.name}
            ###### 年龄：{st.session_state.patient.age}岁
            ###### 地址：{st.session_state.patient.address}
            ###### 电话：{st.session_state.patient.phone}
            ''')
    if st.button('更改患者', use_container_width=True):
        st.session_state.patient = get_patient_info()


def chat():
    if llm:
        tokenizer, model = get_model('THUDM/chatglm3-6b')
        response, history = model.chat(tokenizer, prompt, history=st.session_state.messages)
    else:
        return 'NO LLM'
    return response

with chat_col:
    prompt = st.text_input('说点什么吧...', '')
    chat_holder = st.empty()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if prompt:
        response = chat()
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})
        x = ''
        for message in st.session_state.messages:
            x = x + f"{message['role']}, {message['content']}\n"
        chat_holder.text(x)

    # pro = st.empty()
    # if st.button('listen'):
    #     a = True
    #     while a:
    #         r = sr.Recognizer()
    #         with sr.Microphone() as source:
    #             pro.text('say')
    #             audio = r.listen(source, timeout=None, phrase_time_limit=10)
    #             pro.text('recognition')
    #             message = r.recognize_whisper(audio, model="base", language="chinese")
    #             pro.text(message)
    #             say(message)
    #             if message == '退出':
    #                 a = False
