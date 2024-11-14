import random
def guess_game():
    computer_guess = random.choice([i for i in range(1,11)])
    num_trial = 0
    while num_trial <=5:
        user_guess = int(input("Plese enter your guess here: "))
        if computer_guess == user_guess:
            print("Congratulations! You guessed it right!")
        elif computer_guess < user_guess:
            print(f"Your guess is to high by at least {user_guess-computer_guess-1}")
            num_trial +=1
            continue
        elif computer_guess > user_guess:
            print(f"Your guess is to low by {computer_guess-user_guess-1}")
            num_trial +=1
            continue


if __name__ == '__main__':
    guess_game()