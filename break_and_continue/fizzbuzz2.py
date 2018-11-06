for number in range(0, 16):
	if number % 3 == 0 and number % 5 == 0:
		print("fizzbuzz")
	else:
		print(number)
		
		
# NOTES:
# So to start off, we’ve created a range from 0 to 15 (remember that the number 16 isn’t counted here). After that, we just print 
# out the number. We’ll deal the most complicated part of this first, and that’s checking to see if a value is divisible by both 3 
# and 5. To do this, we just use a simple if statement with an and condition.

# OUTPUT:
    
#     fizzbuzz
#     1
#     2
#     ....
#     14
#     fizzbuzz

# To check to see if a number can be divided evenly by 3, we need to use the modulo operator. If the modulo operator returns a 
# value of zero, then that number is evenly divisible by 3. The same applies to 5. We just use the and operator here to say that
# both of these conditions must be true to execute the code in the if block. Notice that we’ve also moved our initial call to the
# print function into the else block. This way we can ensure that if the conditions in the if block aren’t met, then we’ll print 
# out the number.