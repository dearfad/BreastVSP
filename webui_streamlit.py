import streamlit as st
from libs.llm import get_response
from libs.asr import get_speech
from libs.tts import tts_play

st.set_page_config(
    page_title="BreastVSP",
    page_icon="👩",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.title("👩 - BreastVSP -")
    llm_toggle = st.toggle("大语言模型")
    asr_toggle = st.toggle("麦克风输入")
    tts_toggle = st.toggle("语音输出")

    if st.button("清除会话历史", type="primary"):
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input(""):

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        for response in get_response(prompt=prompt, history=st.session_state.messages, llm=llm_toggle, llm_model='qwen', online=True): 
            response_placeholder.markdown(response)
            
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})

    if tts_toggle:
        tts_play(response)

while asr_toggle:
    asr_message = get_speech()
    if asr_message:
        prompt = asr_message
