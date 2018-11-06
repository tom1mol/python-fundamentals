fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0


while counter < len(fruits):
    print(fruits[counter])
    counter += 1
    
    
# OUTPUT:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# apple
# banana
# peach
# pear
# plum
# orange
   
# NOTES:
    
# Here is a slightly more elaborate example using a while loop and list indexes. Firstly, we have our fruits list which is the 
# same list of fruits that we used before. Next we’ve declared a variable called counter. Each time we run this while loop, we’ll 
# increase the value of this by one. After this, we have our while loop. This while loop checks to see if the counter is less than 
# the length of fruits. This way, every time the counter variable is increased, it will map directly to an index that’s contained 
# within the fruits list.

# Let’s take a look at the example below:

# Element      “apple”   “banana”   “peach”   “pear”   “plum”   “orange
# Index               0                1                   2               3               4               5

# Instead of using the actual number inside the square brackets, we can just use the counter variable as the
# index value. After that, we just clock up our counter by using the arithmetic operator to add one to the 
# existing counter variable, and the process starts again, so long as the condition in the while loop is true!    