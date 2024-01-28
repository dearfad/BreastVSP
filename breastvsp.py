import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np

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

df = conn.read(worksheet=1, ttl=0)

# data = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

# conn.update(wordsheet=1, data=data)

st.write(df)