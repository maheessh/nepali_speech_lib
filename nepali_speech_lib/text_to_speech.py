from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play


def text_to_speech(text):
    tts = gTTS(text=text, lang='ne')
    tts.save("output.mp3")

    # Play the audio
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)
