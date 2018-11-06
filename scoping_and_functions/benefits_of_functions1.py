#PYTHON2

name = raw_input("Input your name:")
age = raw_input("Input your age:")

print "Your name is %s" % name
print "You are %s years old" % age


# OUTPUT:
# python 2.7.10 (default, Jul 14 2015, 19:46:27)
# [GCC 4.8.2] on linux
   
# Input your name: jim
# Input your age: 9
# Your name is jim
# You are 9 years old
   
# NOTES:
# Aside from the ability to reuse code over and over again, functions allow us to build layers of abstraction. One of the perks is 
# that we only need to update our code in one place and those changes will be propagated throughout a more extensive system. We can 
# use functions to abstract some tasks into functions, meaning when we wish to change something, we can change it one place 
# (the function definition), instead of everytime we use that piece of code. An example of this would be, in Python 2, they used a 
# print keyword instead of a print function, and the raw_input function instead of the input function. Let’s have a look at what this 
# would have looked like: