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

with st.expander("请输入你的姓名、年级"):
    name = st.text_input('姓名')
    grade = st.selectbox('年级',tuple(range(1,10)))

st.write('你的姓名是：', name)
st.write('你的年级是：', grade)