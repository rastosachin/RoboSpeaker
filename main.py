import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

while True:
    audio = input("Enter something to be said: ").strip()
    if not audio:
        continue
    if audio.lower() in ("quit", "exit"):
        speak("Goodbye")
        break
    speak(audio)