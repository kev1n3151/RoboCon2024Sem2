#purpose of this code is to run locally on the rosie computer to listen for a phrase that will launch the EC2 instances for further processing and more advanced functions
#this code is going to be a duplicate version of the realtime.py file with the only difference being the keyword that is listened and reduced scope
import os
import re
import azure.cognitiveservices.speech as speechsdk
from rosieTextGen import textGen



#if not speech_key or not speech_region:
#    print(f"Environment variables not set correctly. SPEECH_KEY={speech_key}, SPEECH_REGION={speech_region}")
#else:
#    print("Environment variables loaded correctly.")

keywords = ['rosie wake up', 'rosie, wake up', 'wake up, rosie', 'wake up rosie']

#word to cancel an action, may not be necessary for current program itteration

speech_key = 'e79b2f4680b24fe5b24d91384e7faa21'
speech_region = 'eastus'
# Azure speech service setup
speech_config = speechsdk.SpeechConfig(speech_key, speech_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_config.speech_synthesis_voice_name = 'en-AU-AnnetteNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


def printline():
    print('------------------------------------------------\n')


def from_mic():
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")

    while True:
        result = speech_recognizer.recognize_once_async().get()
        transcription = result.text.strip()
        print(f"Transcription: {transcription}")

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"Recognized: {transcription}")

            keyword_detected = False
            actionword_detected = False


            response = None

            # Check if a keyword is detected first and prioritize it
            for keyword in keywords:
                match = re.search(re.escape(keyword), transcription, re.IGNORECASE)
                if match:
                    print('Keyword detected.')
                    keyword_detected = True
                    start_index = match.start()
                    transcription = transcription[start_index:]
                    print(f"Startup-Phrase detected: '{transcription}'")
                    printline()
                    to_speaker("Starting up, Boot sequence initiated.")
                    exit(0)

                    # add code here to start the EC2 instances, maybe inlcude checks to see if they are already running or in rhe process of initializing


                    # maybe exit process here? or continue listening in case someone closes the program and you want to restart it through voice command
                    break



            if not keyword_detected :
                print('No keywords or actionwords detected, continue listening.')
                printline()

        elif result.reason == speechsdk.ResultReason.NoMatch:
            print(f"No speech could be recognized: {result.no_match_details}")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech Recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")
                break


def to_speaker(text):
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized for text [{text}]")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")


# Main
try:
    rosieText = textGen()
    from_mic()
except Exception as err:
    print(f"Encountered exception. {err}")
