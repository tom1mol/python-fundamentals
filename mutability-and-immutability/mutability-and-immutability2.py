#What if we wanted to ensure that our list is sorted alphabetically. Well, in that case, we’d just use the .sort() method.

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

fruits.sort()

print(fruits)


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# ['apple', 'banana', 'orange', 'peach', 'pear', 'plum']


#Now all of the elements have reorganised themselves, so they’re alphabetically ordered. And we can also delete elements from 
#a list using the del keyword. In this one we delete apple.

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

del fruits[0]

print(fruits)

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# ['banana', 'peach', 'pear', 'plum', 'orange']
    