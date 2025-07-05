import random

def introduction():
    name = input("What's your name: ")
    print(f"Hello {name}!")
    print("\nLet's start with a Rock Paper Scissors Game:\n")
    return name

def play_game(old_computer_score, old_user_score):
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print(f"Invalid choice made by user: {user_choice}")
        return old_computer_score, old_user_score  

    computer_choice = random.choice(choices)
    print(f"Computer choice is: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        old_computer_score += 5
        old_user_score += 5
    elif (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'scissors') or (computer_choice == 'scissors' and user_choice == 'rock'):
        print("You WIN!")
        old_user_score += 10
    else:
        print("You LOSE & computer WINS!")
        old_computer_score += 10

    print(f"Computer Score: {old_computer_score}\nUser  Score: {old_user_score}")
    return old_computer_score, old_user_score

# Main game loop
temp = 'y'
computer_score = 0
user_score = 0

while temp.lower() == 'y':
    introduction() 
    computer_score, user_score = play_game(computer_score, user_score)
    temp = input("Want to continue? (y/n): ")

print("Thank you for playing!")