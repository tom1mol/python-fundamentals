word = input("Input a word:")

print(word[0])


    # OUTPUT:
    # Python 3.6.1 (default, Dec 2015, 13:05:11)
    # [GCC 4.8.2] on linux
       
    # Input a word: shite
    # i
   
   
#   Here we’re asking the user to enter a word. Then we use [0] to get the first letter of the word, and then we print it out. 
#   However, if the user just hits the enter without typing in a word, the string will be empty, and 
#   Python will say “IndexError: string index out of range.” The reason for this is the list doesn’t have any indices because 
#   it’s empty.