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


# 免文件播放
# 自动播放
# import base64
# async def speak(text):
#     voice = 'zh-CN-XiaoxiaoNeural'
#     rate = '-4%'
#     volume = '+0%'
#     communicates = edge_tts.Communicate(
#         text=text, voice=voice, rate=rate, volume=volume)

#     audio_list = []
#     async for communicate in communicates.stream():
#         if communicate["type"] == "audio":
#             audio_list.append(communicate["data"])
#     audio_bytes = b''.join(audio_list)
#     audio_base64 = base64.b64encode(audio_bytes).decode()
#     audio_tag = f"""
#             <audio controls autoplay="true" id="tts_speaker">
#             <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
#             </audio>
#             """
#     st.markdown(audio_tag, unsafe_allow_html=True)
#     return audio_bytes
