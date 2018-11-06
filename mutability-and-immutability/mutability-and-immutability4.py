# Although strings are lists, they are also immutable. Therefore strings cannot be mutated as lists can. If we wanted 
# to change a string, we’d have to store it in another variable. For example, if we had a string that contained the word ‘Hello’, 
# and we wanted an uppercase version of it, we’d have to use the .upper() method and store the value returned in a new variable.


my_word = "Hello"

my_uppercase_word = my_word.upper()

print(my_uppercase_word)


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# HELLO

# NOTES:
# In this respect, strings are much more like tuples in Python, but in most programming languages, strings as immutable descendants 
# of some list. But it is much easier to think of strings as a list of characters.
    