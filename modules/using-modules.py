# In Python, we call a Python file a module. Python comes with a plethora of modules, but as a developer, we also create
# modules every time we create our files.  We can even import functions, classes, and variables from other modules. 
# One example of one of Python’s built-in modules is random. The random module contains a function called randint. 
# Below is an example of how we can import the randint function from the random module:


from random import randint

print(randint(12, 14))

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 14

# 2ND OUTPUT: 
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 12

# NOTES:
# We use the from keyword to target a module and the import keyword to import the specific function from the random module. 
# The randint function takes two arguments which define the range from which to generate a random number. 
# The first argument being the lowest number and the second argument being the highest number.
   
