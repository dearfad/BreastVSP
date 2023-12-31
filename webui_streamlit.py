import streamlit as st
from libs.models.mscope import get_model
import speech_recognition as sr
from libs.tts.edge import tts_say

# LLM
# ModelScope ZhipuAI/chatglm3-6b
# ASR
# Github openai/whisper
# TTS
# Github rany2/edge-tts
# Voice ['zh-CN-XiaoxiaoNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-liaoning-XiaobeiNeural', 'zh-CN-shaanxi-XiaoniNeural', 'zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-TW-HsiaoChenNeural', 'zh-TW-HsiaoYuNeural']

st.set_page_config(
    page_title="乳腺外科虚拟病人",
    page_icon="👩",
    layout='wide',
    initial_sidebar_state='expanded',
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.title('👩 - BreastVSP -')

    if llm_toggle := st.toggle('大语言模型'):
        with st.spinner('加载模型中...'):
            st.session_state.tokenizer, st.session_state.model = get_model()

    asr_toggle = st.toggle('麦克风输入')

    tts_toggle = st.toggle('语音输出')

    if st.button('清除会话历史', type="primary"):
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



prompt = st.chat_input('')


def chat():
    with st.chat_message("user"):
        st.markdown(prompt)

    if llm_toggle:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for response, history in st.session_state.model.stream_chat(st.session_state.tokenizer, prompt, history=st.session_state.messages):
                response_placeholder.markdown(response)
            st.session_state.messages = history
    else:
        with st.chat_message("assistant"):
            st.markdown('没有使用大语言模型')
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        st.session_state.messages.append(
            {'role': 'assistant', 'content': "没有使用大语言模型"})

    if tts_toggle:
        tts_say(response, voice='zh-CN-XiaoxiaoNeural')


if prompt:
    chat()


if asr_toggle:
    temp = True
    while temp:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            mic_status_placeholder = st.empty()
            mic_status_placeholder.write('请说...')
            audio = r.listen(source, timeout=None, phrase_time_limit=10)
            mic_status_placeholder.write('识别中...')
            asr_message = r.recognize_whisper(audio, model="small", language="chinese")
            mic_status_placeholder.empty()
            if asr_message:
                prompt = asr_message
                chat()
            if asr_message == '退出':
                temp = False
