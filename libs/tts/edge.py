import edge_tts
import asyncio
from playsound import playsound


def say(message):
    asyncio.run(speak(message))

async def speak(message):
    text = message
    voice = 'zh-CN-XiaoyiNeural'
    output = './demo.mp3'
    rate = '-4%'
    volume = '+0%'
    tts = edge_tts.Communicate(text=text,voice = voice,rate = rate,volume=volume)
    await tts.save(output)
    playsound(output)

if __name__ == '__main__':
    say("你好")