import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

username = input("Enter your username to continue to RoboSpeaker: ")
print(f'Hello {username}! I am your Voice Assistant Jarvis v1.1.\nDesigned for Windows. Developed by Sachin Rastogi.\n')

speak(f'Hello {username}, this is Jarvis, your personal Voice Assistant v1.1.')
while True:
    audio = input("Please enter what you want me to speak: ").strip()
    if not audio:
        continue
    if audio.lower() in ("quit", "exit"):
        speak("Exiting Jarvis.")
        break
    speak(audio)