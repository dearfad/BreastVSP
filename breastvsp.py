import pyttsx3
def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart('name start'))
engine.connect('started-word', onWord('name','location','length'))
engine.connect('finished-utterance', onEnd('name','complete'))
engine.say('：语音合成播报 安装 pyttsx3： API封装 API使用 博主热门文章推荐： pyttsx3 是python中最常用的文字转语音库，使用方便，功能较')
engine.runAndWait()
