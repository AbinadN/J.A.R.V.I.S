from cvzone.SerialModule import SerialObject
import speech_recognition as sr

# Arduino Serial Connection
mySerial = SerialObject("COM3", 9600, 1)

# Function to map speech commands to finger gestures
def map_commands(command):
    if command == "peace":
        return [0, 1, 1, 0, 0]  # Gesture for peace
    elif command == "rock on":
        return [1, 1, 0, 0, 1]  # Gesture for rock on
    elif command == "swag":
        return [1, 0, 0, 0, 1]  # Gesture for swag
    elif command == "point":
        return [0, 1, 0, 0, 0]  # Gesture for pointing
    else:
        return [1, 1, 1, 1, 1]  # Default gesture (closed hand)

# Initialize Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Continuously listen to spoken commands and control hand gestures
while True:
    # Recognize Speech Commands
    with microphone as source:
        print("Speak:")
        audio = recognizer.listen(source)

    try:
        speech_text = recognizer.recognize_google(audio).lower()
        print("You said:", speech_text)

        # Map speech commands to finger gestures
        fingers = map_commands(speech_text)

        # Send finger gestures to Arduino
        mySerial.sendData(fingers)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
