fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0

while counter < len(fruits):
    if fruits[counter] == "peach":
        counter += 1
        continue

    print(fruits[counter])
    counter += 1

print("Iteration has been completed")


#  OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# apple
# banana
# pear
# plum
# orange
# Iteration has been completed


# Notes:
#     In this example, we’ve decided that we don’t want to print out peach. As such, inside of our while loop, 
#     we have a condition that will check to see if the element is equal to “peach”. If this is true, then we use 
#     the continue keyword. Once the continue keyword is executed, this stops the current cycle and will continue straight
#     into the next cycle.
    
   