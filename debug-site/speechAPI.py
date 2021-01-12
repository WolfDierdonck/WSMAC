import azure.cognitiveservices.speech as speechsdk
import grammar_check

def from_file():
    f = open('output.txt', 'w')
    d = open('result.txt', 'w')
    speech_config = speechsdk.SpeechConfig(subscription="18b27d3bc19143fe9d581e9b40b4253e", region="eastus")
    audio_input = speechsdk.AudioConfig(filename="test.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
    result = speech_recognizer.recognize_once_async().get()
    d.write(result.text)
    d.close()

    returnedStuff = grammar_check.model_call(result.text)
    for i in returnedStuff:
        print(i + "\n")
        f.write(i)

    f.close()

from_file()