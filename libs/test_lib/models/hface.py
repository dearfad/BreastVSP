import os
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModel

# MODEL_NAME_DICT = {
#     'modelscope': 'ZhipuAI/chatglm3-6b',
#     'huggingface': 'THUDM/chatglm3-6b',
# }


def get_model(repo_id):
    HF_HOME_PATH = os.environ.get('HF_HOME')
    print('HF_HOME_PATH: ', HF_HOME_PATH)
    MODEL_PATH = snapshot_download(repo_id)
    print('MODEL_PATH: ', MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True)
    model = AutoModel.from_pretrained(repo_id, trust_remote_code=True)
    return tokenizer, model


if __name__ == '__main__':
    tokenizer, model = get_model('THUDM/chatglm3-6b')
