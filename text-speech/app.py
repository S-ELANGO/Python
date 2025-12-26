from gtts import gTTS
import os

def do_tts(text, filename, folder="audio"):
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, filename)

    tts = gTTS(text=text, lang='en')
    tts.save(file_path)

    print(f"Saved at: {file_path}")
    os.system(f"afplay {file_path}")

text = "Hello world, hi I am Elango"
do_tts(text, "voice.mp3")
