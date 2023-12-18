from libs.asr.speechrecognition import listen
from libs.tts.pytts import say

if __name__=='__main__':
    message = 'start'
    while message!="再見":
        message = listen()
        print(message)
        say(message)