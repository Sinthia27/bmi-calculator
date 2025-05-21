menu = ["🍗 Korean Fried Chicken", "🥘 Bibimbap", "🍙 Kimbap", "🌶️ Kimchi", "🍚 Rice", "🥩 Korean BBQ"]

name = input("What would you like us to call you? ")

def welcome(name):
    print("Welcome to Golden Square Mart!")
    print(f"I hope you are having a good day, {name}!")
    # print(f"Here is the menu:\n{menu}")
    print("Here's the menu:")
    for i, item in enumerate(menu, 1):  # It goes through each item in the menu list one at a time. It starts with 1 because of (,1). If it was (,10) it would've been 10.Korean Fried Chicken.
        print(f"{i}. {item}")

welcome(name)

number = int(input(f"So {name}, what would you like to get? "))

def get_item(number):
    return menu[number - 1]

print (f"Your order is {get_item(number)}!")

