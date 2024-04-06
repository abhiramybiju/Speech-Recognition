import speech_recognition as sr
# import pyttsx3
# txt_sp=pyttsx3.init()
def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("Speak............")
        r.energy_threshold=100
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)
            print("You said:",text)
            # txt_sp.say(text)
            # txt_sp.runAndWait()
        except:
            text1="Didn't hear anything. please speak again..."
            # txt_sp.say(text1)
            # txt_sp.runAndWait()
speech_recog()