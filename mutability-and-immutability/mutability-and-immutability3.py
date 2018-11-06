# Tuples, however, are not mutable, meaning that they cannot be changed or modified and have a fixed size 
# and fixed values. Therefore if we create a tuple containing two items, then it will always have two items. 
# It cannot be changed. If we wanted to use the del keyword on an item in a tuple, then Python will complain.


my_tuple = ("item one", "item two")

del my_tuple[0]

# OUTPUT:
    
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Traceback (most recent call last):
#   File "python", line 3, in <module>
# TypeError: 'tuple' object doesn't support item deletion
   
   
# Now Python is telling us that the ‘tuple’ object doesn’t support item deletion because a tuple is 
# immutable and cannot be changed.