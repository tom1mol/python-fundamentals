#If we needed access to both, keys, and values, we’d have to use a dictionary method called .items().

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    print("Key: %s" % key)
    print("Value: %s" % value)
    print("------------------")
    
    
# OUTPUT:
# Key: username
# Value: tombombadil
# ------------------
# Key: first_name
# Value: Tom
# ------------------
# Key: last_name
# Value: Bombadil
# ------------------
# Key: age
# Value: 100
# ------------------

# NOTE:
# Now we have defined to new variables in our for loop, key and value. These variables don’t need to be called
# key and value, but as the first variable will be the key and the second variable will the value, it’s 
# considered to be a good convention. Then after that, we just print out the key and the value, with some 
# nice formatting to denote each key/value with which we’re working.
   