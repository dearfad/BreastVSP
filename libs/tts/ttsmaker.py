import requests
import json
from playsound import playsound

def say(message):
    url = 'https://api.ttsmaker.cn/v1/create-tts-order'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    params = {
        'token': 'ttsmaker_demo_token',
        'text': message,
        'voice_id': 348,
        'audio_format': 'mp3',
        'audio_speed': 0.9,
        'audio_volume': 0,
        'text_paragraph_pause_time': 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(params))
    mp3url = response.json()['audio_file_url']
    playsound(mp3url) 
    return

if __name__ == "__main__":
    say("This is a ttsmaker demo.")