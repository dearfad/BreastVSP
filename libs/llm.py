from transformers import AutoTokenizer, AutoModel
import streamlit as st

MODEL_PATH = "D:\Github\Repositories\models\huggingface\chatglm3-6b"


@st.cache_resource(show_spinner=False)
def get_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = (
        AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True)
        .quantize(4)
        .cuda()
        .eval()
    )
    return tokenizer, model


if __name__ == "__main__":
    tokenizer, model = get_model()
