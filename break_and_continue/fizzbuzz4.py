for number in range(0, 16):
  if number % 3 == 0 and number % 5 == 0:
    print("fizzbuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("buzz")
  elif number % 2 == 0:
    print("bollox")
  else:
    print(number)