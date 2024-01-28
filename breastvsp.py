import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="BreastVSP",
    page_icon="👩",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title('Breast VSP')

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.write(df)