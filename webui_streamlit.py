# from libs.models.mscope import get_model
from libs.asr.speechrecognition import listen
from libs.tts.edge import say
import streamlit as st
from libs.info.vsp import get_patient_info
import speech_recognition as sr

st.title("Breast Virtual Standard Patient")


def get_vsp():
    breastvsp = get_patient_info()

    # photo = './patient.jpeg'
    infotext = f'''
                        #### {breastvsp.name}
                        ###### 年龄：{breastvsp.age}岁
                        ###### 地址：{breastvsp.address}
                        '''
    
    # return photo, infotext
    return breastvsp, infotext
breastvsp, patient_info = get_vsp()
info_col, chat_col = st.columns(2)
with info_col:
    st.image('patient.jpeg')
    st.markdown(patient_info)
    if st.button('change'):
        breastvsp, patient_info = get_vsp()


with chat_col:
    pro = st.empty()
    if st.button('listen'):
        a = True
        while a:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                pro.text('say')
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                pro.text('recognition')
                message = r.recognize_whisper(audio, model="base", language="chinese")
                pro.text(message)
                say(message)
                if message == '退出':
                    a = False

# tokenizer, model = get_model()


# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):
#     print('1st prompt', list(st.session_state.messages))
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     print('2nd message: ', list(st.session_state.messages))
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         for response, history in model.stream_chat(tokenizer, prompt, history=list(st.session_state.messages)):
#             message_placeholder.markdown(response)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     print('3: ', list(st.session_state.messages))
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     print(list(st.session_state.messages))



# def main():

#     tokenizer, model = get_model()

#     history = []
#     while True:
#         message = listen()
#         print(message)
#         response, history = model.chat(tokenizer, message, history=history)
#         print(response)
#         say(response)
