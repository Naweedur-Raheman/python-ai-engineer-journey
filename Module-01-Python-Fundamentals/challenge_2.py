user_mood = input("How are you feeling today: ").lower()

if user_mood == "happy" or user_mood == "excited":
    print("Thats awesome.Keep smiling!")
elif user_mood == "sad" or user_mood == "tired":
    print("I'm sorry to hear that, take a break")
elif user_mood == "angry" or user_mood == "stressed":
    print("Take a deep breath. You've got this")
else:
    print("Interesting, tell me more about that.")    

