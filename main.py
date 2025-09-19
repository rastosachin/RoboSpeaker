import pyttsx3

# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker")
#
#     engine = pyttsx3.init()
#
#     while True:
#         x = input("Enter what you want me to speak or 'q' to quit: ")
#         if x.lower() == "q":
#             engine.say("Goodbye! Have a nice day!")
#             engine.runAndWait()
#             break
#         engine.say(x)
#         engine.runAndWait()
#         engine.stop()

engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()
engine.stop()

engine.say("This is Robo Speaking")
engine.runAndWait()