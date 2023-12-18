import pyttsx4

engine = pyttsx4.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('RATE', rate)                # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print ('VOLUME', volume)                # printing current volume level
engine.setProperty('volume', 1)         # setting up volume level  between 0 and 1

"""VOICE"""
# voices = engine.getProperty('voices')           # getting details of current voice
# engine.setProperty('voice', voices[0].id)     # changing index, changes voices. o for female
# engine.setProperty('voice', voices[1].id)     # changing index, changes voices. 1 for unknown

# only coqui_ai_tts engine support cloning voice.
# engine = pyttsx4.init('coqui_ai_tts')
# engine.setProperty('speaker_wav', './docs/i_have_a_dream_10s.wav')

# engine.say('this is an english text to voice test, listen it carefully and tell who i am.')
# engine.runAndWait()


engine.say('这是一个虚拟乳房疾病患者的项目。')

engine.runAndWait()
engine.stop()