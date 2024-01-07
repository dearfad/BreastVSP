# import os
# from huggingface_hub import snapshot_download
# from transformers import AutoTokenizer, AutoModel
import streamlit as st

# MODEL_PATH = 'D:\Github\Repositories\models\huggingface\chatglm3-6b'

MODEL_PATH = "D:\Github\Repositories\models\modelscope\Qwen-1_8B-Chat-Int4"

# @st.cache_resource(show_spinner=False)
# def get_model():
#     # HF_HOME_PATH = os.environ.get("HF_HOME")
#     # print("HF_HOME_PATH: ", HF_HOME_PATH)
#     # MODEL_PATH = snapshot_download(repo_id)
#     # print("MODEL_PATH: ", MODEL_PATH)
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
#     model = (
#         AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True)
#         .cuda()
#         .eval()
#     )
#     return tokenizer, model

from modelscope import AutoTokenizer, AutoModelForCausalLM, snapshot_download


@st.cache_resource(show_spinner=False)
def get_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, trust_remote_code=True
    ).eval()
    return tokenizer, model

if __name__ == "__main__":
    tokenizer, model = get_model()
