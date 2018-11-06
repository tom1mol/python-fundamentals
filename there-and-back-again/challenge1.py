age = int(input("How old are you?"))

if age < 0:
    print("Sorry. I can’t tell what drink because that age is incorrect!")
elif age < 14:
    print("Drink Toddy")
elif age < 18:
    print("Drink Coke")
elif age < 21:
    print("Drink Beer")
elif age < 130:
    print("Drink Whisky")
else:
    print("Sorry. I can’t tell what drink because that age is incorrect!")
    