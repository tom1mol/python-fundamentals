#When working with collections, one of the main reasons to use a list would be if you are storing pieces of information 
# about many different things, and you would use tuples for storing different aspects of a single thing. For example, 
# we might want to use a list to store a list of usernames:

usernames = ["tombombadil", "BilboBaggins", "Frodo_Baggins"]

for username in usernames:
    print(username)
    
# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# tombombadil
# BilboBaggins
# Frodo_Baggins
   
user = ("tombombadil", "Tom", "Bombadil")

print("Username: %s" % user[0])
print("First Name: %s" % user[1])
print("Last Name: %s" % user[2])

# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Username: tombombadil
# First Name: Tom
# Last Name: Bombadil
   