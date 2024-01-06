import os
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModel
import streamlit as st

MODEL_PATH = 'D:\Github\Repositories\models\huggingface\chatglm3-6b'

@st.cache_resource(show_spinner=False)
def get_model(repo_id="THUDM/chatglm3-6b"):
    # HF_HOME_PATH = os.environ.get("HF_HOME")
    # print("HF_HOME_PATH: ", HF_HOME_PATH)
    # MODEL_PATH = snapshot_download(repo_id)
    # print("MODEL_PATH: ", MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = (
        AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True)
        .quantize(4)
        .cuda()
        .eval()
    )
    return tokenizer, model


if __name__ == "__main__":
    tokenizer, model = get_model("THUDM/chatglm3-6b")
