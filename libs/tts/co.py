import torch
from TTS.api import TTS
from playsound import playsound

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/zh-CN/baker/tacotron2-DDC-GST").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="test.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text="你好，我是世界上最好的人了", speaker_wav="test.wav", file_path="./output.wav")

playsound("./output.wav")