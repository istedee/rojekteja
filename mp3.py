from gtts import gTTS
import os

def text_to_audio():
    mytext = input('Haloo?: ')
    language = 'fi'
    mymp = gTTS(text=mytext, lang=language, slow=False)
    mymp.save('filu.mp3')
    os.system(f'xdg-open filu.mp3')

if __name__ == '__main__':
    text_to_audio()
