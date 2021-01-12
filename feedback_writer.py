import serial

class FeedbackWriter:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = serial.Serial(port)
    
    def write_positive_feedback(self):
        print("gramatically correct | via feedbackWriter")
        self.port.write(bytes("P", "utf-8"))

    def write_negative_feedback(self):
        print("gramatically incorrect | via feedbackWriter")
        self.port.write(bytes("N", "utf-8"))


if __name__ == "__main__":
    import time
    
    feedbackWriter = FeedbackWriter(input("Serial Port, e.g. 'COM8' or '/dev/ttyACM0': "))

    while True:
        feedbackWriter.write_positive_feedback()
        time.sleep(2)
        feedbackWriter.write_negative_feedback()
        time.sleep(2)
