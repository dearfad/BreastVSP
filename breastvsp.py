import streamlit as st
from libs.utils import save_to_gspread
import random
from http import HTTPStatus
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role

st.set_page_config(
    page_title="BreastVSP",
    page_icon="👩",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title('乳腺外科虚拟病人')

# if "login" not in st.session_state:
#     st.session_state.login = False

# if not st.session_state.login:
#     login_placeholder = st.empty()
#     with login_placeholder.container():
#         with st.form('login_form'):
#             name = st.text_input('姓名', placeholder='无名氏')
#             grade = st.selectbox('年级',tuple(range(2010,2030)))
#             login_bt = st.form_submit_button('登录', use_container_width=True)

#     if login_bt:
#         if name:
#             save_to_gspread([name, grade])
#             login_placeholder.empty()
#             st.session_state.login = True
#         else:
#             st.error('请输入姓名', icon="🚨")

if "messages" not in st.session_state:
    st.session_state.messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({'role': 'user', 'content': prompt})


    with st.chat_message("assistant"):
        response = Generation.call(
            'qwen-1.8b-chat',
            messages=st.session_state.messages,
            # set the random seed, optional, default to 1234 if not set
            seed=random.randint(1, 10000),
            result_format='message',  # set the result to be "message"  format.
        )
        if response.status_code == HTTPStatus.OK:
            st.write(response)

        # response_placeholder = st.empty()
        # for response in get_response(prompt=prompt, history=st.session_state.messages, llm=llm_toggle, llm_model='qwen', online=True): 
        #     response_placeholder.markdown(response)
            
    # st.session_state.messages.append({"role": "user", "content": prompt})
    # st.session_state.messages.append({"role": "assistant", "content": response})