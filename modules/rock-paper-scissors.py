# Let’s combine some of the aspects programming that we’ve learned up until now. To do that, we’ll create a game of rock,
# paper, scissors. This game will cover everything from declaring variables, using conditionals, getting user input, lists,
# while loops, functions, and the random module. The idea of rock, paper, scissors is that there are two players. 
# Each player picks either rock, paper, or scissors. In a game of rock, paper, scissors:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# For this to work, we need our two players. Firstly we’ll have a user, and then we’ll have the computer. Then we need a way for a 
# user to choose whether they want rock, paper, or scissors. Then we’ll need to generate a random selection by the computer. 
# Let’s have a look:
    
    
from random import randint


def compare(user, computer):
    if user.lower() == computer.lower():
        print("It's a tie!")
    elif user.lower() == 'rock':
        if computer.lower() == 'scissors':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'scissors':
        if computer.lower() == 'paper':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'paper':
        if computer.lower() == 'rock':
            print("You win!")
        else:
            print("The computer wins!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")


def get_computers_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice


def game_loop():
    play_game = True
    
    while play_game:
        user = input("Rock, paper, or scissors?")
        computer = get_computers_choice()
        
        victor = compare(user, computer)
        
        play_again = input("Woud you like to play again? y/N:")
        
        if play_again.lower() == "n":
            play_game = False
            
    print("Thanks for playing!")

game_loop()


# Python 3.6.1 (default, Dec 2015, 13:05:11)
# [GCC 4.8.2] on linux
   
# Rock, paper, or scissors? rock
# You win!
# Woud you like to play again? y/N: y
# Rock, paper, or scissors? paper
# The computer wins!
# Woud you like to play again? y/N: 


# NOTES:
# First of all, we import randint. Next, we define some functions (compare, get_computers_choice and game_loop). 
# The first function that we’ll invoke is going to be game_loop. Inside game_loop, we have a bool called play_game, 
# and we set that value to true. Next, we create a while loop which will run so long as play_game is true. Then we 
# ask a user to select rock, paper, or scissors. After a user makes their choice, we then need the computer to make a choice. 
# To generate a choice for the computer, we created a new function called get_computers_choice. Inside this function, we declare 
# a list of strings containing the elements Rock, Paper, and Scissors called choices. Next, we need a to get a random number between
# 0 and 2 that will represent the index that we’ll be accessing from the list of choices; therefore, we’ve named it choice_index. 
# Lastly, we use the choice_index variable to access the relevant item in the choices list. Then we simply return the choice.

# Once both the user and computer have made their choices, we need to determine which of them is the victor. We then need to create 
# a function called compare, which will compare the two choices. This function takes two parameters, user 
# and computer. These will represent the choices made by each participant. Inside this function, we have a pretty elaborate if-else 
# ladder. First, we simply check to see if both choices are the same. If this is the case, then we just print out "It’s a tie".
# Next, we check to see if the user’s choice was rock. If it is, then we have a nested condition to check if the computer’s choice
# was scissors. If it is scissors, then we need to tell the user that they’ve won by printing out "You win!". Otherwise print 
# "The computer wins!"

# We repeat this logic until we’ve checked each possible outcome, and if none of them evaluates to true, then that means that 
# you’ve made an incorrect choice when selecting rock, paper, or scissors. Then we just ask the user if they wish to play again. 
# If their decision is n, then we say, “Thanks for playing!” and set the value of play_game to false, which will exit out of the 
# loop.







