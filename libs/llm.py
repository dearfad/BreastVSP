import streamlit as st

from langchain_community.llms import Tongyi

from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM


MODEL_PATH = {
    "chatglm": "D:\\Github\\Repositories\\models\\huggingface\\chatglm3-6b",
    "qwen": "D:\\Github\\Repositories\\models\\modelscope\\Qwen-1_8B-Chat-Int4",
}


@st.cache_resource(show_spinner=False)
def chatglm():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH["chatglm"], trust_remote_code=True
    )
    model = (
        AutoModel.from_pretrained(MODEL_PATH["chatglm"], trust_remote_code=True)
        .quantize(4)
        .cuda()
        .eval()
    )
    return tokenizer, model


@st.cache_resource(show_spinner=False)
def qwen():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH["qwen"], trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH["qwen"],
        device_map="auto",
        trust_remote_code=True,
        use_flash_attn=False,
    ).eval()
    return tokenizer, model


MODEL = {
    "chatglm": chatglm,
    "qwen": qwen,
}


def chatglm_stream_chat(tokenizer, model, prompt: str, history: list):
    history = [
        {"role": message["role"], "content": message["content"]} for message in history
    ]
    for response, _ in model.stream_chat(
        tokenizer,
        prompt,
        history,
    ):
        yield response


def qwen_stream_chat(tokenizer, model, prompt: str, history: list):
    history = [
        {"role": message["role"], "content": message["content"]} for message in history
    ]

    for response in model.chat_stream(tokenizer, prompt, history):
        yield response


CHAT = {
    "chatglm": chatglm_stream_chat,
    "qwen": qwen_stream_chat,
}


def get_response(prompt: str, history: list, llm: bool, llm_model: str, online: bool):
    if llm:
        if online:
            model = Tongyi(model_name="qwen-1.8b-chat", streaming=True)
            yield model.invoke(prompt)

        else:
            tokenizer, model = MODEL[llm_model]()
            for response in CHAT[llm_model](tokenizer, model, prompt, history):
                yield response
    else:
        yield "No LLM, Switch On."


if __name__ == "__main__":
    for response in get_response(
        prompt="help", history=[], llm=True, llm_model="qwen", online=True
    ):
        print(response)
