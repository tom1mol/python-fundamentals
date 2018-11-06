for number in range(0, 16):
	if number % 3 == 0 and number % 5 == 0:
		print("fizzbuzz")
	elif number % 3 == 0:
		print("fizz")
	else:
		print(number)
		
		
		

		
		
		
# NOTES:
# So far we’ve managed to print out the fizzbuzz if the number is divisible by 3 and 5, and then we print out the number 
# if it’s not. That’s two parts of the criteria down. Next, we’ll update it to print fizz. For this, we just need an elif 
# to see if the number is divisible by 3.		    

# OUTPUT:
# fizzbuzz
# 1
# 2
# fizz
# 4
# 5
# fizz
# 7
# 8
# fizz
# 10
# 11
# fizz
# 13
# 14
# fizzbuzz