import os
import streamlit as st
from streamlit_javascript import st_javascript
import speech_recognition as sr

import edge_tts
import asyncio
import base64

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
    st.markdown(audio_tag, unsafe_allow_html=True)
    return


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
        st.session_state.speaking = True
        tage = asyncio.run(speak(response))



if prompt:
    chat()


if asr_toggle:

    
# if (audio.paused) {
#   console.log("音频当前处于暂停状态");
# } else {
#   console.log("音频正在播放");
# }

# if (audio.ended) {
#   console.log("音频已经播放完毕");
# } else {
#   console.log("音频还未播放完毕");
# }

    # return_value = st_javascript("""return document.getElementById("tts_speaker");""")
    return_value = st_javascript("""document.getElementById("tts_speaker");""")
    st.markdown(f"Return value was: {return_value}")
    # print(f"Return value was: {return_value}")


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
