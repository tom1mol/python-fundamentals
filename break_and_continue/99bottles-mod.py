for number in range(99, 0, -1):
    line_one = "{0} bottle(s) of beer on the wall. {0} bottle(s) of beer"
    line_two = "Take one down, pass it around. {0} bottle(s) of beer on the wall\n"
    print(line_one.format(number))
    print(line_two.format(number - 1))
    continue
for number in range(0, -1, -1):
    line_three = "No more bottles of beer on the wall, no more bottles of beer. "
    line_four = "We’ve taken them down and passed them around; now we’re drunk and passed out!\n"

    
    
    print(line_three.format(number))
    print(line_four.format(number - 1))
    
    
# OUTPUT:
# 99 bottle(s) of beer on the wall. 99 bottle(s) of beer
# Take one down, pass it around. 98 bottle(s) of beer on the wall

# 98 bottle(s) of beer on the wall. 98 bottle(s) of beer
# Take one down, pass it around. 97 bottle(s) of beer on the wall
# ..............

# 1 bottle(s) of beer on the wall. 1 bottle(s) of beer
# Take one down, pass it around. 0 bottle(s) of beer on the wall

# No more bottles of beer on the wall, no more bottles of beer. 
# We’ve taken them down and passed them around; now we’re drunk and passed out!