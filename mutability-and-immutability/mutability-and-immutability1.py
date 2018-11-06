#Allows creation of data structures that can be modified, as well as others that cannot be changed
#For data that can be modified and updated; or are static values that will always remain the same

# Something that’s mutable is something that can be changed. Lists, for example, are mutable. Mutable 
# means that it can be mutated and immutable implies that it cannot be mutated. Lists are likely to grow 
# and change over time, and we can achieve this by using the .append() method. In the example below, we’ve 
# added strawberry to our list of fruits using .append().

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

fruits.append("strawberry")

print(fruits)


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# ['apple', 'banana', 'peach', 'pear', 'plum', 'orange', 'strawberry']
   

