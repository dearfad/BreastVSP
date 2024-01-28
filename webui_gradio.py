from modelscope import AutoTokenizer, AutoModelForCausalLM
import logging
import gradio as gr

logging.basicConfig(level=logging.CRITICAL)

model_path = "D:\\Github\\Repositories\\models\\modelscope\\Qwen-1_8B-Chat-Int4"
tokenizer = AutoTokenizer.from_pretrained(
    model_path, revision="master", trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True,
    use_flash_attn=False,
).eval()

system_prompt = """你是一名乳房疾病的患者,下面是你的疾病特征。
【信息】性别:女,年龄:30岁。
【主诉】右侧乳房疼痛3天。
【病程】哺乳后15天,右侧乳房皮肤红肿。
【查体】右侧乳房外上象限皮肤红肿,有触痛,皮温升高,范围约2*2厘米大小。心、肝、肺、肾没有异常。
【辅助检查】
体温:39度,
心率:120次/分,
呼吸16次/分,
【血常规】
白细胞12.0,
血红蛋白:110。
请用简体中文回答,请不要回答疾病特征以外的问题。
"""


def chat(query, history):
    response, history = model.chat(
        tokenizer=tokenizer, query=query, history=history, system=system_prompt
    )
    return response


demo = gr.ChatInterface(fn=chat)

demo.launch()
