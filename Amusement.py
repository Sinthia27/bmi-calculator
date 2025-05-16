height = int(input("Height? "))
credits = int(input("Credits? "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height >= 137 and credits < 10:
  print("Not enough credits!")
elif height < 137 and credits >= 10:
  print ("Not tall enough!")
else:
  print("Not tall enough and not enough credits!")


