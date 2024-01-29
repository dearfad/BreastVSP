import streamlit as st
import gspread

st.set_page_config(
    page_title="BreastVSP",
    page_icon="👩",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title('Breast VSP')

gc = gspread.service_account_from_dict(st.secrets.gspread_credentials)
sh = gc.open("breastvsp")

st.write(sh)
