def print_message(name):
    print("Hello %s" % name)

username = input("What's your name?")
print_message(username)


# output:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# What's your name? fuck off
# Hello fuck off


# NOTES:
# The function that we created in the last example was called print_message, which then prints out Hello World. 
# That’s all well and good, but what if we wanted to say hello to a user instead of saying Hello World. The problem is 
# that our function doesn’t allow for that level of flexibility. One way around this would be to create a function for every name, 
# but that would get very unwieldy, and the codebase would end up being massive! Instead we can use parameters. Parameters allow us 
# to provide a function with input data that we want it to use. Let’s update our previous example to use a parameter to greet a user 
# with:
    
    
# Now we’ve updated our function to take a parameter of name, and we use that name to greet the user. 
# At line 5 we call the print_message function by passing through an argument.

# A function's parameters are the special variables used by a function to handle this input, whereas the 
# arguments are the values provided for the parameters when we run the function. For example, on line 1,
# we create a function that has a parameter named name, and then on line 5 we run that function and pass in 
# the value of the variable username as the argument for that parameter