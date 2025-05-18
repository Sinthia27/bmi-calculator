import random

# int() so the value inputted by the player is an integer. In order to prevent repeated printing of "Error🚨Invalid Input", below.
player_choice = int(input("1 is for “✊” (Rock).\n2 is for “✋” (Paper).\n3 is for “✌️️” (Scissors).\nPick a number: "))

# Turning the inputted numbers in to emojis
if player_choice == 1:
    player_choice = "✊"
elif player_choice == 2:
    player_choice = "✋"
elif player_choice == 3:
    player_choice = "✌️"
else:
    print("🚨 Error 🚨Invalid Input!")
    exit() # ends the code

print(f"You chose: {player_choice}")


# using random.randint to get randomised number between 1-3
computer_choice = random.randint(1,3)
if computer_choice == 1:
    computer_choice = "✊"
elif computer_choice == 2:
    computer_choice = "✋"
else:
    computer_choice = "✌️️"

print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == "✊" and computer_choice == "✌️️":
    print("The player won!")
elif computer_choice == "✊" and player_choice == "✌️":
    print("The computer won!")
elif player_choice == "✌️" and computer_choice == "✋":
    print("The player won!")
elif computer_choice == "✌️" and player_choice == "✋":
    print("The computer won!")
elif player_choice == "✋" and computer_choice == "✊":
    print("The player won!")
elif computer_choice == "✋" and player_choice == "✊":
    print("The computer won!")
else:
    print("Invalid Input!")




