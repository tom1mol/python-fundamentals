fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0

while counter <= len(fruits) - 1:
    if fruits[counter] == "peach":
        break
    print(fruits[counter])
    counter += 1

print("Iteration has been completed")


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# apple
# banana
# Iteration has been completed
   