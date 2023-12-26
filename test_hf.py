import os
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer, AutoModel

# HF_HOME_PATH = os.environ.get('HF_HOME')
# print('HF_HOME_PATH: ', HF_HOME_PATH)

# snapshot_download(repo_id='THUDM/chatglm3-6b')

print('start tokenizer...')
tokenizer = AutoTokenizer.from_pretrained(
    'THUDM/chatglm3-6b', trust_remote_code=True)

print('start model...')
model = AutoModel.from_pretrained(
    'THUDM/chatglm3-6b', trust_remote_code=True)

print('start quantize...')
model = model.quantize(4)

print('start cuda...')
model = model.cuda()

print('start eval...')

model = model.eval()
