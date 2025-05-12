import random
characters = ["deborah", "mia", "isdor", "pilaf", "orgo", "cookie", "henrique"]
chosen_character = random.choice(characters) #this will randomise the values in the list above
print(chosen_character)


chosen_character_letters = list(chosen_character)  # makes a list with each letter of the name of the chosen character
random.shuffle(chosen_character_letters) # shuffling of the list of letters
scramble = ''.join(chosen_character_letters) # the job of ''.join() is to combine all the values in a list together. e.g. ''.join(characters) = deborahmiaisdorpilaforgocookiehenrique
print(scramble)

game_over = False
chances = 3

while not game_over:
    guess = input("\nGuess the character: ").lower()

    # The first two `if` and `else` statements are their own code blocks.
    # The `else` ends the first `if` statement, allowing a new `if` statement to start for the next check.
    # This wouldn't be possible if I used `elif` like before, because `elif` would link the checks together, causing the second `if` to be skipped if the first condition was true.

    if guess == chosen_character:
        print(f"Bingo!! You guessed the character! It was {chosen_character.capitalize()}.")
        game_over = True

    else:
        print("You guessed incorrectly! Try again!")
        chances -= 1

    if chances == 0:
        print(f"\nYou lose! The character was {chosen_character.capitalize()}.")
        game_over = True





















