countdown_number = 10

print("Initiating Countdown Sequence...")
print("Lift Off Will Commence In...")

while countdown_number >= 0:
    print("%s seconds..." % countdown_number)
    countdown_number -= 1

print("And We Have Lift Off!")


# In this example we declare a variable called countdown_number, then we proceed to begin a countdown sequence. 
# Then we have our while loop. We create this by starting with the while keyword, followed by a condition. 
# In this case, the code inside the while loop will be executed so long as countdown_number is greater than or equal to 0. 
# Inside the while block, we print out the countdown_number, followed by the word “seconds”. 
# Next, we subtract 1 from the countdown_number, meaning that with each iteration, the countdown_number gets closer to 0. 
# Once the countdown_number reaches 0, on the last iteration the countdown_number will be set to -1. 
# Since this value is not greater than or equal to 0, the conditional expression of the while loop won’t evaluate to true 
# and the while loop will be skipped. After exiting the loop, we simply print out, “And We Have Lift Off!”

# NOTE: Be careful when constructing a while loop. If we’d forgotten to subtract one from the countdown_number at the end of
# each iteration, the loop would have run forever as the condition would have run forever as the condition would always evaluate to
# true. This error is called an infinite loop.


# OUTPUT:
    
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Initiating Countdown Sequence...
# Lift Off Will Commence In...
# 10 seconds...
# 9 seconds...
# 8 seconds...
# 7 seconds...
# 6 seconds...
# 5 seconds...
# 4 seconds...
# 3 seconds...
# 2 seconds...
# 1 seconds...
# 0 seconds...
# And We Have Lift Off!
   