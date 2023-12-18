import pyttsx4

def say(message):
    engine = pyttsx4.init()
    engine.setProperty('rate', 125)
    engine.say(message)
    engine.runAndWait()
    return

if __name__ == '__main__':
    say("This is pyttsx4 demo.")


# MAY USE IN WHISPER

# import pyttsx4
# from io import BytesIO
# from pydub import AudioSegment
# from pydub.playback import play
# import os
# import sys

# engine = pyttsx4.init()
# b = BytesIO()
# engine.save_to_file('i am Hello World', b)
# engine.runAndWait()
# #the bs is raw data of the audio.
# bs=b.getvalue()
# # add an wav file format header
# b=bytes(b'RIFF')+ (len(bs)+38).to_bytes(4, byteorder='little')+b'WAVEfmt\x20\x12\x00\x00' \
#                                                                b'\x00\x01\x00\x01\x00' \
#                                                                b'\x22\x56\x00\x00\x44\xac\x00\x00' +\
#     b'\x02\x00\x10\x00\x00\x00data' +(len(bs)).to_bytes(4, byteorder='little')+bs
# # changed to BytesIO
# b=BytesIO(b)
# audio = AudioSegment.from_file(b, format="wav")
# play(audio)

# sys.exit(0)