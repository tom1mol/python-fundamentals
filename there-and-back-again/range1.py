for item in range(5):
    print(item)
    
    
# OUTPUT:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 0
# 1
# 2
# 3
# 4

# NOTES:
#     Instead of just starting from 0, we can use additional arguments to achieve various sequence combinations. 
#     We know this by looking at the Python documentation for range() - https://docs.python.org/3/library/stdtypes.html#range. 
#     Looking at the documentation is a great way of finding out more information about the functions that Python provides.

# range() can take up to three arguments, which are:

# Start - This is the first argument that range() accepts. It is an optional argument and will be given a default value of 0.

# Stop - This is the second argument. It is the number at which to stop our sequence. In order for range() to work, we need to provide
# a stop argument.

# Step - This is the last argument that range() takes. It is also an optional argument. If we don’t provide one, 
# Python will default to 1.

# In the last example, we only supplied one argument. Given that the start and step arguments are optional, 
# the argument that we provided was the stop argument. This indicates that we want a sequence comprised of 5 
# numbers.