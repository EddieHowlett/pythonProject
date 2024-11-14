user_age = int(input("What is your age?"))
if user_age < 12:
    print("The ticket will cost £5")
elif user_age < 18:
    print("The ticket will cost £7")
else:
    print("The ticket will cost £10")