#In Python 2, we would have:

def get_user_input(prompt):
    return raw_input(prompt)


def print_out_to_console(value_to_be_printed):
    print value_to_be_printed

name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

print_out_to_console("Your name is %s" % name)
print_out_to_console("You are %s years old" % age)


# OUTPUT:
    
# Python 2.7.10 (default, Jul 14 2015, 19:46:27)
# [GCC 4.8.2] on linux
   
# Input your name: joe
# Input your age: 7
# Your name is joe
# You are 7 years old
   
#  NOTES:
#   Abstraction allows us to hide complex or monotonous actions or pieces of code that are prone to 
#   change into functions.change
#   Using functions to abstract pieces makes it easier to reuse code and concepts. One of the perks of this
#   is that we only need to update our code in one place and those changes will be propagated throughout a 
#   more extensive system
#   Or, what we could do is hide the actual input and output in functions, which means that we’ll only need to update them once. 