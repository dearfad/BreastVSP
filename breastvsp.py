from libs.models.mscope import get_model
from libs.asr.speechrecognition import listen
from libs.tts.edge import say


def main():

    tokenizer, model = get_model('ZhipuAI/chatglm3-6b')
    model = model.quantize(4).cuda().eval()

    history = []
    while True:
        message = listen()
        print(message)
        response, history = model.chat(tokenizer, message, history=history)
        print(response)
        say(response)


if __name__ == '__main__':
    main()
