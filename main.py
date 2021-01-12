from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import requests

import importlib

# Import specialized serial connection
from feedback_writer import FeedbackWriter
from speechToText import record_to_file


def debug_result(grammar_result):
    if "gramatically correct" in grammar_result.lower():
        print("YAY Grammar works: Result below:") #tested


# Sends a grammar result to a FeedbackWriter, if it is open
def send_serial_feedback(grammar_result, feedbackWriter):
    if feedbackWriter: 
        if "gramatically correct" in grammar_result.lower():
            feedbackWriter.write_positive_feedback()
        else:
            feedbackWriter.write_negative_feedback()  
    else:
        print("Feedback writer null why")

# Returns a serial connection to an Arduino (for rpi devices)
# Returns None if unsuccessful connection
def open_feedback_serial():
    try:
        feedbackWriter = FeedbackWriter(input("Serial Port, e.g. 'COM8' or '/dev/ttyACM0': "))
        return feedbackWriter
    except:
        return None


#remember 2 refactor
if __name__ == '__main__':

    transcript = open('stt_transcript.txt', 'w+b')
    feedback = open_feedback_serial()
    
    #test feedbackwriter/arduino functioning:
    feedback.write_positive_feedback()

    while True:
        print("Recording Audio")
        record_to_file('recording.wav')
        recordings = {'testSubmit':("test.wav", open('recording.wav', 'rb'))}
        print("Please hold...")
        
        t = requests.post("http://debugsite.herokuapp.com/recieveData.php", files=recordings)
        r = requests.get("http://debugsite.herokuapp.com/sendData.php")

        # Apparently there's only one line
        requestLines = r.content.decode("utf-8").split("\n")


        grammar_result = requestLines[0]
        debug_result(grammar_result)
        send_serial_feedback(grammar_result, feedback)

        
        transcript.write(r.content)
        print("------")
        

