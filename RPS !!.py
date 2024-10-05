import random
import time

# Rules Of The Game:
print("Winning Rules Of Rock Paper Scissors are: \n"
      + "1. Rock Vs Paper -> Paper Wins \n"
      + "2. Rock Vs Scissor -> Rock Wins \n"
      + "3. Paper Vs Scissor -> Scissor Wins")

# Options User can choose:
options = ["Rock", "Paper", "Scissors"]

# Choices:
while True:
    print("Choices: \n"
          + "Rock \n"
          + "Paper \n"
          + "Scissors \n")

    # User's Choice:
    user_choice = input("Enter Your Choice: ").title()

    if user_choice not in options:
        print("Enter a Valid Choice.")
        continue

    print('User choice is:', user_choice)
    
    # Computer's Choice:
    print("Now it's Computer's Turn....")
    time.sleep(2)

    comp_choice = random.choice(options)

    print("Computer choice is:", comp_choice)
    print(user_choice, 'vs', comp_choice)

    # Game Logic
    if user_choice == comp_choice:
        print("<== It's A Tie ==>")
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper') or \
         (user_choice == 'Paper' and comp_choice == 'Rock'):
        print("<== Hooray You Won! ==>")
    else:
        print("<== Sorry You Lose, Better Luck Next Time ==>")

    # Play Again:
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")
