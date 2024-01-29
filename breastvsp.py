import streamlit as st
from libs.utils import save_to_gspread

st.set_page_config(
    page_title="BreastVSP",
    page_icon="👩",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title('乳腺外科虚拟病人')

login_placeholder = st.empty()
with login_placeholder.container():
    with st.form('login_form'):
        name = st.text_input('姓名', placeholder='无名氏')
        grade = st.selectbox('年级',tuple(range(2010,2030)))
        login_bt = st.form_submit_button('登录', use_container_width=True)

if login_bt:
    if name:
        save_to_gspread([name, grade])
        login_placeholder.empty()
        st.write(f'{name} 医生')
    else:
        st.error('请输入姓名', icon="🚨")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input(""):

    with st.chat_message("user"):
        st.markdown(prompt)

    # with st.chat_message("assistant"):
    #     response_placeholder = st.empty()
    #     for response in get_response(prompt=prompt, history=st.session_state.messages, llm=llm_toggle, llm_model='qwen', online=True): 
    #         response_placeholder.markdown(response)
            
    # st.session_state.messages.append({"role": "user", "content": prompt})
    # st.session_state.messages.append({"role": "assistant", "content": response})