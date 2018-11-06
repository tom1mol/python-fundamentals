# Allows us to create sub-lists from lists
# How do you use it?
# Sometimes we may only need a subset of a list, instead of a full list. In this case, we would use slice notation to chop up the list

"""
Lists are a great way of storing a collection of variables and objects, but what if you want to have more than just have a 
collection of strings? What if you wanted a list of lists? We can also create dictionaries and tuples. We can also create lists 
and dictionaries dynamically in a single line of code using list and dictionary comprehensions, respectively. And we’ll take a look
at how to access values stored in each of the different types of collections and how to work with them with looping constructs.

We can slice up lists to get subsets of a list. For example, if we wanted to get the first two items in a list, then we would do
the following:

"""

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# ['apple', 'banana']

#SECOND EXAMPLE:
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[:2])

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# ['apple', 'banana']    
       
       
# NOTES:
# Here we’ve added [0:2] to the end of our list which is called slice notation. It works like a combination
# of indexing and range. First, we indicate the index at which we wish to start. Then after the colon (:),
# we use the index at which we want to stop. Similar to the range function, the stop value is the everything 
# up to, but not including, that value. Here it will, therefore, include everything up to index 2, 
# except for index two itself. If we wanted to start at the very beginning of a list, we could just say [:2].



