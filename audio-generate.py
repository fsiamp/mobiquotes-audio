# tested with python 3.9 on mac high sierra
# https://www.python.org/downloads/macos/
# https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg

from gtts import gTTS
import random

lines = open('quotes.txt').read().splitlines()

pickedLine =random.choice(lines)


# Text to convert to speech
#text = "Hello, this is a text-to-speech example."

# Convert text to speech
tts = gTTS(text=pickedLine, lang='en', slow=False)

# Save the audio file
number = str(random.randint(1000000000, 9999999999))
#tts.save("output.mp3")
tts.save(number + ".mp3")
print(pickedLine)
print(number + ".mp3")
