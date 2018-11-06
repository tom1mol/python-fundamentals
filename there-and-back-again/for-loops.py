for item in range(5):
    print(item)
    


# OUTPUT:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 0
# 1
# 2
# 3
# 4
   
   
# NOTES:
    
# Firstly, we’ll look at the range function. The range function will generate a sequence of numbers. 
# By passing through an argument of 5, we’re saying that we wish for that sequence to be comprised of 5 numbers. 
# Most programming languages, including Python, are zero-based. Therefore they start counting at 0 instead of 1. 
# When we use the range function to generate a sequence of 5 numbers, it will create a series ranging from 0-4. 
# Those numbers are 0, 1, 2, 3 and 4. We use the for loop to iterate each of the numbers in this sequence. 
# The way in which we build up a for loop is by first using the for keyword. After the for keyword we have item.
# item is a variable name. This variable will act as a placeholder. After item, we have in. 
# It just tells Python what sequence of data we wish to iterate over. For each iteration of the for loop, 
# Python will get the next item from the series and store it in the item variable so we can use it inside 
# the for loop. Then inside the for loop we simply print out each item of the sequence, starting at 0 and 
# working up to 4.