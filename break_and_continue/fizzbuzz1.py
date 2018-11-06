for number in range(0, 16):
	print(number)
	
	
# OUTPUT:
# 0
# -
# -
# 15


# NOTES:
#     Fizzbuzz is one of the single most infamous coding challenges that developers are faced with in technical interviews. 
#     The idea of fizzbuzz is relatively simple; however, it’s usually the simplicity of this problem that catches out even some 
#     of the most battle-hardened developers. The purpose of fizzbuzz is to iterate over a list or range of numbers, and we end up 
#     some different choices that must be made depending on the value of that number. If the number is divisible by 3, then we print 
#     out fizz. If the number is divisible by 5, we print out buzz. If, however, the number is divisible by both 3 and 5, print out 
#     fizzbuzz. Otherwise, we just print out the number. To accomplish this, we need to start with a for loop that iterates over a 
#     range of numbers. Any range will do, so long as it at least reaches the number 15, as 15 is the first number in the numeric 
#     sequence that is divisible by both 3 and 5. Let’s take a look at how it looks.