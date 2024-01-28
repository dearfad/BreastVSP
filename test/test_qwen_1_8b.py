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


prompt = '你哪里不舒服呢？'

system_msg = '你是一名乳房疾病的患者，右侧乳房疼痛，哺乳后15天，30岁，乳房皮肤红肿，心、肝、肺、肾没有异常。请用简体中文回答。'


response, history = model.chat(tokenizer, prompt, history=None, system=system_msg)

print(response)
