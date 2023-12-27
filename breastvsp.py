from libs.models.mscope import get_model
# from libs.asr.speechrecognition import listen
# from libs.tts.edge import say
import streamlit as st

st.title("Echo Bot")

tokenizer, model = get_model()


# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    print('1st prompt', list(st.session_state.messages))
    with st.chat_message("user"):
        st.markdown(prompt)
    print('2nd message: ', list(st.session_state.messages))
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        for response, history in model.stream_chat(tokenizer, prompt, history=list(st.session_state.messages)):
            message_placeholder.markdown(response)
    st.session_state.messages.append({"role": "user", "content": prompt})
    print('3: ', list(st.session_state.messages))
    st.session_state.messages.append({"role": "assistant", "content": response})
    print(list(st.session_state.messages))



# def main():

#     tokenizer, model = get_model()

#     history = []
#     while True:
#         message = listen()
#         print(message)
#         response, history = model.chat(tokenizer, message, history=history)
#         print(response)
#         say(response)
