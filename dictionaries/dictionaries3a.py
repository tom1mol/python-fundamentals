# Note: Dictionaries don’t have any order, so the order that the keys get printed in may not match the order in which you defined them.

# But, what if we want the values associated with each of those keys? Then we’d simply use the square brackets like before.

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for item in user:
    print(user[item])
    
# OUTPUT:
# tombombadil
# Tom
# Bombadil
# 100

# NOTES:
# Now we’re passing the item value into the square brackets. Remember, an item is just a temporary variable that’s used within the
# scope of the for loop, and on each iteration, it will retrieve the next string that’s used as a key. It will print out the 
# value for each of the key/value pairs contained in the dictionary.
   