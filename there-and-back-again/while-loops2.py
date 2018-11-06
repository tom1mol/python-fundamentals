play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n")
    
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")



# OUTPUT:
#     Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Would you like to continue playing the game? y/n y
# You have decided to continue playing the game.
# Would you like to continue playing the game? y/n q
# That is not a valid option. Please try again.
# Would you like to continue playing the game? y/n n
# Now closing the game...
# Thanks for playing

# NOTES:
#     Here we’ve declared a variable called play_game which is set to true. 
#     While play_game is true, we do the following. First, we ask the user if they wish to continue playing the game. 
#     We indicate the answer should be yes or no (“y/n”). We then store this value in a variable called continue_playing. 
#     We then check to see if continue_playing is equal to “y”. If it is, then we tell them that they’ve decided to continue playing.

# NOTE: We’ve used the .lower() method, just in case a user uses an uppercase input. When working with uppercase and lowercase, 
# it’s important to note that, while they are the same letter, they are not the same string.

# If this is the case, then the while loop will begin its next cycle, and the user will be prompted again. 
# Else if continue_playing is equal to “n”, then we inform them that they’ve decided to quit the game, 
# and we set the play_game variable to false. Now that the play_game variable is no longer true, 
# the program will exit the loop and print out, “Thanks for playing.” Lastly, 
# if the user enters something other than y or n, then they’ll be informed that their decision was invalid 
# and they need to try again.
   