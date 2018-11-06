for number in range(99, 0, -1):
    line_one = "{0} bottle(s) of beer on the wall. {0} bottle(s) of beer"
    line_two = "Take one down, pass it around. {0} bottle(s) of beer on the wall\n"

    print(line_one.format(number))
    print(line_two.format(number - 1))
    
    
    
# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 99 bottle(s) of beer on the wall. 99 bottle(s) of beer
# Take one down, pass it around. 98 bottle(s) of beer on the wall

# 98 bottle(s) of beer on the wall. 98 bottle(s) of beer
# Take one down, pass it around. 97 bottle(s) of beer on the wall
# ....
# 1 bottle(s) of beer on the wall. 1 bottle(s) of beer
# Take one down, pass it around. 0 bottle(s) of beer on the wall

# NOTES:

# First, we just need a for loop. Our for loop will iterate through the range of numbers between 99 and 0, stepping in -1. 
# Each iteration of the loop will get closer to 0. On the following two lines we just declare two string variables 
# (line_one and line_two). Instead of including the number of bottles of beer in the string, we’ve used placeholders ({0}). 
# And line_two has the newline escape character at the end so we’ll have a clear line break between the verse. 
# Then we just print out line_one, which is formatted to include the number from the current iteration of the loop.

# On the first cycle, this will give us:
# 99 bottles of beer on the wall, 99 bottles of beer.

# Then we print out the line_two, which will contain the current number of the iteration – 1 which, on the first iteration, 
# will give us:
# Take one down, pass it around, 98 bottles of beer on the wall…

# This pattern will then continue all the way down to 0. See if you change this to print an alternative last verse if the number is 
# equal to zero –
# No more bottles of beer on the wall, no more bottles of beer. We’ve taken them down and passed them around; now we’re drunk and 
# passed out!