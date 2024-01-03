import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    print('recognition')
    message = r.recognize_whisper(audio, model="base", language="chinese")
    return message

if __name__ == "__main__":
    print(listen())



        # prompt = '以下是普通话的句子'
        # result = self.whisper_model[model].transcribe(
        #     audio_array,
        #     language=language,
        #     task="translate" if translate else None,
        #     fp16=torch.cuda.is_available(),
        #     initial_prompt=prompt,
        #     **transcribe_options
        # )