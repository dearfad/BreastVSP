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