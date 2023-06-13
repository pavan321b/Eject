##########
# TASK 2 #
##########

# push your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = ""

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = "task2"
# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of each
# method below that currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# DO NOT CHANGE the names or parameters of any of these methods
# DO NOT CHANGE the names of the four fields
# Make sure you read the method descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a class definition and a program that can
# be used to test its behaviour
#
# To run the program type  play_game()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

class stick_game () :
    # A class of objects that capture the state of a game that involves
    # pushing sticks into slots in a board until all slots are full
    # The winner is the person who fills up the last empty slot(s)
    # Each stick_game, SG, has four fields:
    #  SG.slots   the total number of slots
    #             SG.slots is a positive int
    #  SG.sticks  the current number of sticks in slots
    #             SG.sticks is a non-negative int
    #  SG.max_one_turn
    #             the absolute maximum number of sticks that a
    #             player is allowed to add in one move
    #             SG.max_one_turn is a positive int
    #  SG.next    the identity of the next player to play
    #             SG.next is either 'A' or 'B'

    def __init__ (self,slots,max_one_turn) :
        # Creates a new stick_game object, using the parameters
        # slots and max_one_turn, and initialises the identity of the
        # player whose turn it is to play next to player 'A'
        # This method already works correctly
        self.slots         = slots  # remains constant throughout the game
        self.sticks        = 0
        self.max_one_turn  = max_one_turn
        self.player        = 'A'


# Method 1: 1 mark
    def all_slots_full (self) :
        # Returns True if all slots are full
        # returns False otherwise

        return None   # code stub


# Method 2: 1 mark   
    def next_player_ID (self) :
        # Returns the identity of the player whose turn
        # it is to play next (either 'A' or 'B')

        return 'Z'   # code stub


# Method 3: 2 marks
    def previous_player_ID (self) :
        # Returns the identity of the player who played
        # the last turn (either 'A' or 'B')

        return 'Z'   # code stub


# Method 4: 3 marks
    def max_sticks_this_turn (self) :
        # Returns the limit on the number of sticks that
        # can be inserted on the current turn. This will depend
        # on max_one_turn and on how many slots are empty

        return 99999   # code stub


# Method 5: 1 mark
    def empty_slots (self) :
        # Returns the number of empty slots on the board
        # When this number is reached the game is over

        return 99999   # code stub


# Method 6: 3 marks
    def add_sticks (self,sticks_to_add) :
        # Adds the number of sticks specified by the parameter
        # sticks_to_add and switches to the next player

        pass   # code stub (currently does nothing)


    def __str__ (self) :
        # Returns a string-based representation of the playing board
        # in a stick_game object so that it can be displayed using Python's
        # built-in print function
        # This method already works correctly
        game_as_string = "Total slots in board = " + str(self.slots) + "\n"
        game_as_string += "Currently " + str(self.sticks) + " slots are full:\n"
        game_as_string += ("!" * self.sticks) + ("." * (self.slots-self.sticks))
        return game_as_string


# ----------------------------------------------------------------------------------------------------------------------------
# DO NOT CHANGE any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------
# GAME PLAY


def play_game() :
    # Sets up and runs a stick game
    # Once you have got the stick_game class working you should
    # test it by setting up games with different numbers of slots
    # in the board and a different number of sticks that can be
    # added on each turn
    # For example    game = stick_game(10,3)
    print ("Welcome to the stick game")
    slot_count = int(input("What is the total number of slots in the playing board? "))
    max_sticks = int(input("What is the maximum number of sticks that can be added on each turn? "))
    game = stick_game(slot_count,max_sticks)
    print ("Players take it in turns to push sticks into slots in a board")
    print ("until all " + str(game.empty_slots()) + " slots are full\n")
    print ("You may push between 1 and " + str(game.max_sticks_this_turn()) + " sticks into the board")
    print ("The player who fills up the board is the winner\n")
    playing = True
    while playing :
        print (game,"\n")
        next_player = game.next_player_ID()
        print ("It's player",next_player,"to play next")
        while True :
            prompt = "There are currently " + str(game.empty_slots()) + " empty slots. "
            prompt += "How many sticks do you want to push?\n"
            prompt += "(maximum possible on this turn is " + str(game.max_sticks_this_turn()) + "): "
            n = int(input(prompt))
            if n >= 1 and n <= game.max_sticks_this_turn() :
                print ()
                break
        game.add_sticks(n)
        if game.all_slots_full() :
            print ("Congratulations player",game.previous_player_ID(),"you win")
            playing = False
    print ("Thank you for playing")
