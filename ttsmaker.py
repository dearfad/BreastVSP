import requests
import json
from playsound import playsound
url = 'https://api.ttsmaker.cn/v1/create-tts-order'
headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    'token': 'ttsmaker_demo_token',
    'text': '乳腺上皮细胞发生增殖失控，进而恶变，乳腺癌的发病率居女性恶性肿瘤首位，具体病因尚不明确，存在遗传风险',
    'voice_id': 348,
    'audio_format': 'mp3',
    'audio_speed': 1.0,
    'audio_volume': 0,
    'text_paragraph_pause_time': 0
}
response = requests.post(url, headers=headers, data=json.dumps(params))
mp3url = response.json()['audio_file_url']
playsound(mp3url) 