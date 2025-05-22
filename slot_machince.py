import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]

play = input("Would you like to play? Yes or No: ").strip().capitalize()

if play != "Yes":
    print("Come back again~")
    exit()

# At this point, we know play == "Y"
while True:
        results = random.choices(symbols, k=3)
        print(" | ".join(results))

        if results == ["7️⃣", "7️⃣", "7️⃣"]:
            print("Jackpot! 💰")
            exit()
        else:
            print("Thanks for playing!")

        play_again = input("Do you want to play again? Yes or No: ").strip().capitalize()
        if play_again != "Yes":
            print("Come back again~")
            break

