import random
moves = ('rock', 'paper', 'scissors')
user_choice = input("Please enter your choice rock, paper, or scissors: ").lower()
computer_choice = random.choice (moves)
print(f"The computer chose {computer_choice}")


if user_choice == computer_choice:
    print("It's a draw")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
     print("You win!")
else:
    print("Computer wins!")
