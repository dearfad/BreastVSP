from modelscope import AutoTokenizer, AutoModelForCausalLM
import logging
logging.basicConfig(level=logging.CRITICAL) 

model_path = 'D:\\Github\\Repositories\\models\\modelscope\\Qwen-1_8B-Chat-Int4'
tokenizer = AutoTokenizer.from_pretrained(model_path, revision='master', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True,
    use_flash_attn=False,
).eval()


question = '北京在哪里啊？'

prompt = f"""问题是 {question}，请用简体中文回答。"""


response, history = model.chat(tokenizer, prompt, history=None)

print(response)
