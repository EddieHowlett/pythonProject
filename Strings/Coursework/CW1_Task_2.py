def mood_sense(mood_score):
    if 1 <= mood_score <= 3:
        return "I'm sorry you're feeling this way. Consider talking to a friend or taking some time for yourself."

    elif 4 <= mood_score <= 7:
        return "It seems like you're having an okay day. Remember to take breaks and focus on self-care."

    elif 8 <= mood_score <= 10:
        return "That's great to hear! Keep up the positive energy!"

    else:
        return "Please enter a valid mood rating between 1 and 10."


print("Hello! I am the MoodSense chatbot")

mood_input = input("On a scale of 1-10 (1 being the least and 10 being best) how would you rate your mood today? ")

if mood_input.isdigit():
    mood_score = int(mood_input)

    if 1 <= mood_score <= 10:
        print(f'You are feeling {mood_score}/10 today')
        response = mood_sense(mood_score)
        print(response)
    else:
        print("Please enter a number between 1 and 10.")
else:
    print("Please enter a valid number between 1 and 10.")