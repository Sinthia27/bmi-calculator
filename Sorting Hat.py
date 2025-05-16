#Points
Gryffindor = 0
Slytherin = 0
Ravenclaw = 0
Hufflepuff = 0

print('===============')
print('The Sorting Hat')
print('===============')


# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

answer1 = int(input("Enter the number of your choice: "))
if answer1 == 1:
    Gryffindor +=1
    Ravenclaw +=1
    print("1 point for Gryffindor and Ravenclaw\n")
else:
    Slytherin +=1
    Hufflepuff +=1
    print("1 point for Slytherin and Hufflepuff\n")


# Question 2
print("Q2) When I'm dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer2 = int(input("Enter the number of your choice: "))
if answer2 == 1:
    Hufflepuff +=2
    print("2 points for Hufflepuff\n")
elif answer2 == 2:
    Slytherin +=2
    print("2 points for Slytherin\n")
elif answer2 == 3:
    Ravenclaw +=2
    print("2 points for Ravenclaw\n")
elif answer2 == 4:
    Gryffindor +=2
    print("2 points for Gryffindor\n")
else:
    print("Wrong input\n")

# Question 3
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer3 = int(input("Enter the number of your choice: "))
if answer3 == 1:
    Slytherin +=4
    print("4 points for Slytherin\n")
elif answer3 == 2:
    Hufflepuff +=4
    print("4 points for Hufflepuff\n")
elif answer3 == 3:
    Ravenclaw +=4
    print("4 points for Ravenclaw\n")
elif answer3 == 4:
    Gryffindor +=4
    print("4 points for Gryffindor\n")
else:
    print("Wrong input\n")

print(f"Gryffindor has {Gryffindor} points!")
print(f"Slytherin has {Slytherin} points!")
print(f"Hufflepuff has {Hufflepuff} points!")
print(f"Ravenclaw has {Ravenclaw} points!\n")

if Gryffindor > Slytherin and Gryffindor > Ravenclaw and Gryffindor > Hufflepuff:
    print("You are Gryffindor!🦁")
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print("You are Slytherin!🐍")
elif Ravenclaw > Slytherin and Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff:
    print("You are Ravenclaw!🐦‍⬛")
else:
    print("You are Hufflepuff!🦫")