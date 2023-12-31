import streamlit as st
from libs.models.mscope import get_model
from libs.info.vsp import get_patient_info
import speech_recognition as sr
# from libs.asr.speechrecognition import listen
from libs.tts.edge import say

st.set_page_config(
    page_title="乳腺外科虚拟病人",
    page_icon="👩",
    layout='wide',
    initial_sidebar_state='expanded',
)

st.echo('testsdaf')

if "patient" not in st.session_state:
    st.session_state.patient = get_patient_info()

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.title('👩 - BreastVSP -')
    st.image('patient.jpeg')
    st.markdown(f'''
            #### {st.session_state.patient.name}
            ###### 年龄：{st.session_state.patient.age}岁
            ###### 地址：{st.session_state.patient.address}
            ###### 电话：{st.session_state.patient.phone}
            ''')
    if st.button('更改患者', use_container_width=True):
        st.session_state.patient = get_patient_info()

    with st.expander('📂 设置'):
        with st.container(border=True):
            llm = st.toggle('大语言模型')
            model = st.selectbox('语言模型', ['ZhipuAI/chatglm3-6b'])
            if llm:
                tokenizer, model = get_model()
        with st.container(border=True):
            micphone = st.toggle('麦克风输入')
            mic_placeholder = st.empty()
            asr = st.selectbox('语音识别', ['openai/whisper'])
        with st.container(border=True):
            voice = st.toggle('语音输出')
            tts = st.selectbox('发音模型', ['rany2/edge-tts'])
            tts_voice = st.selectbox('语音选择', ['zh-CN-XiaoxiaoNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-liaoning-XiaobeiNeural',
                                              'zh-CN-shaanxi-XiaoniNeural', 'zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-TW-HsiaoChenNeural', 'zh-TW-HsiaoYuNeural'])
        with st.container(border=True):
            patient = st.selectbox('患者信息', ['random'])

        if st.button('清除会话历史', type="primary"):
            st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input('说点什么吧...')


def c():
    with st.chat_message("user"):
        st.markdown(prompt)

    if llm:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for response, history in model.stream_chat(tokenizer, prompt, history=st.session_state.messages):
                response_placeholder.markdown(response)
            st.session_state.messages = history
    else:
        with st.chat_message("assistant"):
            st.markdown('没有使用大语言模型')
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        st.session_state.messages.append(
            {'role': 'assistant', 'content': "没有使用大语言模型"})

    if voice:
        say(response, voice=tts_voice)

if prompt:

    c()


if micphone:
    a = True
    while a:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            mic_placeholder.markdown('say')
            audio = r.listen(source, timeout=None, phrase_time_limit=10)
            mic_placeholder.markdown('recognition')
            asr_message = r.recognize_whisper(
                audio, model="small", language="chinese")
            mic_placeholder.markdown(asr_message)
            if asr_message:
                prompt = asr_message
                c()                
            if asr_message == '退出':
                a = False
