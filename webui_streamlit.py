import os
import io
import streamlit as st
from streamlit_javascript import st_javascript
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder

import edge_tts
import asyncio
import base64
import sounddevice as sd
from playsound import playsound

from modelscope.hub.snapshot_download import snapshot_download
from modelscope import AutoTokenizer, AutoModel

# LLM MODEL


@st.cache_resource(show_spinner=False)
def get_model(model_id='ZhipuAI/chatglm3-6b'):
    # MODELSCOPE_CACHE_PATH = os.environ.get('MODELSCOPE_CACHE')
    # print('MODELSCOPE_CACHE_PATH: ', MODELSCOPE_CACHE_PATH)
    # MODEL_PATH = snapshot_download(model_id)
    # print('MODEL_PATH: ', MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModel.from_pretrained(
        model_id, trust_remote_code=True).quantize(8).cuda().eval()
    return tokenizer, model

# TTS


async def speak(text):
    voice = 'zh-CN-XiaoxiaoNeural'
    rate = '-4%'
    volume = '+0%'
    communicates = edge_tts.Communicate(
        text=text, voice=voice, rate=rate, volume=volume)

    audio_list = []
    async for communicate in communicates.stream():
        if communicate["type"] == "audio":
            audio_list.append(communicate["data"])
    audio_bytes = b''.join(audio_list)
    audio_base64 = base64.b64encode(audio_bytes).decode()
    audio_tag = f"""
            <audio controls autoplay="true" id="tts_speaker">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
            """
    # st_javascript("""
    #                 document.write("<h1>what</h1>")
    #               """)
    st.markdown(audio_tag, unsafe_allow_html=True)
    return audio_bytes


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

if "speaking" not in st.session_state:
    st.session_state.speaking = False

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
        response = '没有使用大语言模型, 需要时可以打开大语言模型开关'
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        st.session_state.messages.append(
            {'role': 'assistant', 'content': response})

    if tts_toggle:
        # st.session_state.speaking = True
        audio_bytes = asyncio.run(speak(response))


if prompt:
    chat()


if asr_toggle:

    # audio_mic = audio_recorder(
    #     text="识别",
    #     icon_name='user',
    #     icon_size='6x'
    # )
    # if audio_mic:
    #     r = sr.Recognizer()
    #     asr_message = r.recognize_whisper(
    #             audio_mic, model="small", language="chinese")
    #     if asr_message:
    #         prompt = asr_message
    #         chat()

    if not st.session_state.speaking:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            mic_status_placeholder = st.empty()
            mic_status_placeholder.write('请说...')
            audio = r.listen(source, timeout=None, phrase_time_limit=10)
            mic_status_placeholder.write('识别中...')
            asr_message = r.recognize_whisper(
                audio, model="small", language="chinese")
            mic_status_placeholder.empty()
            if asr_message:
                prompt = asr_message
                chat()
