#Then when we update to Python 3, we would have:

def get_user_input(prompt):
    return raw_input(prompt)


def print_out_to_console(value_to_be_printed):
    print value_to_be_printed

name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

print_out_to_console("Your name is %s" % name)
print_out_to_console("You are %s years old" % age)


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Input your name: JIM
# Input your age: #9
# Your name is JIM
# You are #9 years old
   