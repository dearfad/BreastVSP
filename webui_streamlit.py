import streamlit as st
from libs.llm import get_model
from libs.asr import get_speech
from libs.tts import tts_play

st.set_page_config(
    page_title="MiniAI",
    page_icon="👩",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.title("👩 - MiniAI -")
    llm_toggle = st.toggle("大语言模型")
    asr_toggle = st.toggle("麦克风输入")
    tts_toggle = st.toggle("语音输出")

    if llm_toggle:
        with st.spinner("加载模型中..."):
            st.session_state.tokenizer, st.session_state.model = get_model()

    if st.button("清除会话历史", type="primary"):
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("")


def chat():
    with st.chat_message("user"):
        st.markdown(prompt)

    if llm_toggle:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for response, history in st.session_state.model.stream_chat(
                st.session_state.tokenizer, prompt, history=st.session_state.messages
            ):
                response_placeholder.markdown(response)
            st.session_state.messages = history
    else:
        response = "没有使用大语言模型, 需要时可以打开大语言模型开关"
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})

    if tts_toggle:
        tts_play(response)


if prompt:
    chat()

while asr_toggle:
    asr_message = get_speech()
    if asr_message:
        prompt = asr_message
        chat()
