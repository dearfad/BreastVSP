import edge_tts
import asyncio
from playsound import playsound


def tts_say(message, voice):
    asyncio.run(speak(message, voice))


async def speak(message, voice):
    text = message
    output = './static/lastspeech.mp3'
    rate = '-4%'
    volume = '+0%'
    tts = edge_tts.Communicate(
        text=text, voice=voice, rate=rate, volume=volume)
    await tts.save(output)
    playsound(output)

if __name__ == '__main__':
    say("测试EDGE TTS ", voice='zh-CN-XiaoyiNeural')
