def print_message():
    my_local_variable = "World"
    print("Hello %s" % my_local_variable)

print_message()
print(my_local_variable)


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Hello World
# Traceback (most recent call last):
#   File "python", line 6, in <module>
# NameError: name 'my_local_variable' is not defined
   





# As we can see, Python will throw an error when we try to use my_local_variable outside of the function. We should 
# generally avoid using a global variable. In the examples that we’re covering here, it’s a little more challenging to avoid them, 
# plus we’re only writing simple scripts to help provide an understanding of how the language works. There are some techniques that 
# a developer would use to help build a better, more scalable application using design patterns, but that’s outside the scope of this #
# lesson. For now, though, we’ll use the global scope and avoid it where possible.