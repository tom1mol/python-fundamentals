# If we wish to access the values contained within the dictionary, we use a similar syntax to indexing in lists and tuples; 
# only we use the string that we use for the key instead of a numeric value. For example, if we wanted to access the user’s age, then we would use the following 
# syntax:

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user["age"])

# OUTPUT:
#100

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user["username"])
print(user["first_name"])
print(user["last_name"])
print(user["age"])


# OUTPUT:
# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# tombombadil
# Tom
# Bombadil
# 100
   