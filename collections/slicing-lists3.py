#In addition to the start: stop values, we also have step. Again, this works in the same way as the range function.
#Now we start at 0, stop at 4, and get there by stepping in 2s


fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:4:2])

# OUTPUT:
# ['apple', 'peach']

#If we wanted to reverse our list, for example, we would just do the following:

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[::-1])

# OUTPUT:
# ['orange', 'plum', 'pear', 'peach', 'banana', 'apple']