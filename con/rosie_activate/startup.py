#!/usr/bin/python3
import pyaudio
import wave
import json
from vosk import Model, KaldiRecognizer
import subprocess  # To use espeak via subprocess

# Load Vosk model
model = Model(lang="en-us")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a new stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

keywords = {'rosie wake up', 'wake up rosie', 'wake up'}
print("Listening...")

try:
    keywords_detected = False
    while not keywords_detected:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print("Recognized text:", text)
            if any(keyword in text for keyword in keywords):
                keywords_detected = True

                print("Keyword detected")
                subprocess.call(['espeak', '-v', 'en+f3', '"Ok, I am waking up"'])

                exit(0) 

except KeyboardInterrupt:
    print("Stopped by user")

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
