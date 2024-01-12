import streamlit as st

# from transformers import AutoTokenizer, AutoModel
# MODEL_PATH = "D:\Github\Repositories\models\huggingface\chatglm3-6b"

from modelscope import AutoTokenizer, AutoModelForCausalLM
MODEL_PATH = 'd:\\Github\\modelscope\\qwen\\Qwen-1_8B-Chat-Int4'


# @st.cache_resource(show_spinner=False)
# def get_model():
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
#     model = (
#         AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True)
#         .quantize(4)
#         .cuda()
#         .eval()
#     )
#     return tokenizer, model

@st.cache_resource(show_spinner=False)
def get_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        device_map="auto",
        trust_remote_code=True
    ).eval()
    return tokenizer, model

if __name__ == "__main__":
    tokenizer, model = get_model()
