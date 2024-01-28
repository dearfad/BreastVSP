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
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(ttl=0)

st.write(df)

https://docs.google.com/spreadsheets/d/1LgpwZ3PkNWVkRXqYNd_eSQz4YOjZH5JFNLSPyGO_Dp8/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1LgpwZ3PkNWVkRXqYNd_eSQz4YOjZH5JFNLSPyGO_Dp8/edit?usp=sharing