import edge_tts
import asyncio
from playsound import playsound

# Github rany2/edge-tts
# Voice ['zh-CN-XiaoxiaoNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-liaoning-XiaobeiNeural', 'zh-CN-shaanxi-XiaoniNeural', 'zh-HK-HiuGaaiNeural', 'zh-HK-HiuMaanNeural', 'zh-TW-HsiaoChenNeural', 'zh-TW-HsiaoYuNeural']


def tts_play(text, voice):
    asyncio.run(speak(text, voice))


async def speak(text, voice):
    output_file = './static/latest_tts.mp3'
    rate = '-4%'
    volume = '+0%'
    pitch = "+0Hz"
    communicate = edge_tts.Communicate(
        text=text, voice=voice, rate=rate, volume=volume, pitch=pitch)
    await communicate.save(output_file)
    playsound(output_file)

if __name__ == '__main__':
    tts_play("测试EDGE TTS ", voice='zh-CN-XiaoyiNeural')
