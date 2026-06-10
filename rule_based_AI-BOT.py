import datetime #for display the current time

import pyttsx3  #for text-to-speech


# After importing installing the engine
engine = pyttsx3.init() 

#voice speed (100 - slow, 150 - normal, 200 - fast)
engine.setProperty("rate",150)  

#voice 1 for female & 0 for male
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)    

#defining the function:
def speak(text):
    engine.say(text)
    engine.runAndWait()

print("\t\tWELCOME TO MY RULE-BASED AI CHATBOT")
print("important note! if your can typ the bye then this code is stop! ")

# printing the greeting using date-time !
user_name = input("enter your name: ")
current_time = datetime.datetime.now().hour

if 5 <= current_time <= 11:
    print(f"good morning {user_name}")
    speak(f"good morning {user_name}")
elif 11 <= current_time <= 17:
    print(f"good afternoon {user_name}")
    speak(f"good afternoon {user_name}")
elif 17 <= current_time <= 20:
    print(f"good evening {user_name}")
    speak(f"good evening {user_name}")

responses ={
    "hello" : "hi , welcome buddy",
    "how are you": "i am good what about you",
    "i'm also good":"okay, how can i help you",
    "are you motivate me": "Yes, of course! I am always here to motivate you.",
    "then motivate me": "Believe in yourself. Every expert was once a beginner. Keep learning, keep practicing, and success will come to you one step at a time.",
    "i want to become a programmer": "Keep coding every day. Even one hour of practice daily can make a huge difference in your programming journey.",
    "i want to learn python": "Python is a great choice for beginners. Start with basics, build small projects, and practice regularly.",
    "give me study tips": "Study consistently, take short breaks, revise regularly, and focus on understanding concepts instead of memorizing them.",
    "thank you": "You are welcome! I am happy to help you anytime.",

}

def botResponse(userQues):
    userQues =  userQues.lower()
    for eachkeys in responses:
        if eachkeys in userQues:
            return responses[eachkeys]
    return "Sorry buddy, I don't know much about that. I'm just a simple chatbot."
    
while True:
    user_input = input("ask anything!: ")
    bot_reply = botResponse(user_input)
    print("bot reply: ",bot_reply)
    speak(bot_reply)

    if user_input.lower() == "bye":
        print("goodbye! have a nice day")
        speak("goodbye! have a nice day")
        break

