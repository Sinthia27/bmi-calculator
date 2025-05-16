correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Password? ")
    if password == correct_password:
       print("Correct!")
       break

    else:
        print("Access Denied!")
        attempts += 1
if attempts == 3:
    print("Too many attempts. Try again later.")

