def print_message(name="World"):
    print("Hello %s" % name)

username = input("What's your name?")
print_message()
print_message(username)

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# What's your name? k
# Hello World
# Hello k
   
   
#  NOTES:
# We can also use optional parameters. Optional parameters will allow us to provide values to a function with some value in case 
# they are not provided when the function is invoked. To do so, we use the assignment operator to set a value to the parameter when 
# we are defining our function. In the example below, we have given the name parameter a default value of World:
    
# We don’t provide an argument when we invoke the function as we do on line 5, the function will just print out Hello World. 
# Notice that we initially stored the value in a variable called username, but inside the function, we’ve called in a name. 
# This is because we’re passing a new variable to the function called name, with the value of username. 
# The name variable cannot be accessed outside of the function. Therefore if we were to try to print name 
# outside of the function, it wouldn’t work. This is known as variable scoping.