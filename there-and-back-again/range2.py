for item in range(1, 10):
    print(item)
    
    
# OUTPUT:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# NOTES:
#     In this example, we’ve provided two arguments. This time we’ve presented both a start argument and a stop argument. 
#     The start argument is 1, and the stop argument is 10. This time around our sequence will look like – 1, 2, 3, 4, 5, 6, 7, 8 and 9.
#     The stop argument is the number at which we wish to stop our sequence. In Python range() will stop the progression before the 
#     number that we provide as the stop argument. Instead of stopping at 10, it will stop at 9. Similarly, 
#     if we changed the stop argument to 15, then it would end at 14: