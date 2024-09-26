import os
import re
import time
import azure.cognitiveservices.speech as speechsdk
from rosieTextGen import textGen

# Environment variables
#speech_key = 'e79b2f4680b24fe5b24d91384e7faa21'
#speech_region = 'eastus'

#if not speech_key or not speech_region:
#    print(f"Environment variables not set correctly. SPEECH_KEY={speech_key}, SPEECH_REGION={speech_region}")
#else:
#    print("Environment variables loaded correctly.")

keywords = ['Hey, Rosie', 'Hey Rosie', 'Hi, Rosie', 'Hi Rosie']
actionwords = ['tuck', 'untuck', 'push', 'open', 'close','extend','contract']
endwords = ['End conversation.', 'That will be all.']

# Azure speech service setup
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
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
            endword_detected = any(re.search(re.escape(endword), transcription, re.IGNORECASE) for endword in endwords)

            response = None

            # Check if a keyword is detected first and prioritize it
            for keyword in keywords:
                match = re.search(re.escape(keyword), transcription, re.IGNORECASE)
                if match:
                    print('Keyword detected.')
                    keyword_detected = True
                    start_index = match.start()
                    transcription = transcription[start_index:]
                    print(f"This text will be sent to GPT '{transcription}'")
                    printline()
                    response = rosieText.textGen(transcription)
                    if response:
                        to_speaker(response)
                    break  # Exit the loop and skip action word detection

            # If no keyword was detected, check if an action word is detected
            if not keyword_detected:
                for actionword in actionwords:
                    match = re.search(re.escape(actionword), transcription, re.IGNORECASE)
                    if match:
                        print(f"Action word '{actionword}' detected.")
                        actionword_detected = True
                        to_speaker(f"Do you want me to {actionword}?")
                        # Wait for user response
                        confirmation = speech_recognizer.recognize_once_async().get().text.strip()
                        if re.search(f"yes, {actionword}", confirmation, re.IGNORECASE):
                            to_speaker(f"Performing {actionword}.")
                            # Placeholder for your actual script that will run when confirmed
                            print(f"Action '{actionword}' confirmed and executed.")
                        else:
                            to_speaker("Action cancelled.")
                        break

            if endword_detected:
                print("Ending conversation.")
                break  # Exit the loop if an endword is detected

            if not keyword_detected and not actionword_detected and not endword_detected:
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

