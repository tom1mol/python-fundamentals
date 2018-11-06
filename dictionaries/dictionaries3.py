# When working with dictionaries, instead of just getting each element, as we would with a list or tuple, we can get 
# both keys and values from a dictionary. Unfortunately, creating the same kind of for loop that we would use to iterate over 
# a list would just give us each key:

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for item in user:
    print(item)
    
# OUTPUT:
# username
# first_name
# last_name
# age


   