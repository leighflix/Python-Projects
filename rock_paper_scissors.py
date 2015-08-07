__author__ = 'leigh'

import random

def gen_pc_item():
    """ Generates a random number to determine What choice the PC makes.

    1 - rock, 2 - paper, 3 - scissors (returns a str of one of the 3)
    """
    pc_item = "None" # fire starter for pc_item (while loop)

    # basically, if pc_item get's an actual number, it is assigned a value, else reloops.
    while pc_item == "None":
        number_item = random.randint(1, 3) # generates a number 1-3 (1, 2, 3)

        if number_item == 1:       pc_item = "rock"
        elif number_item == 2:     pc_item = "paper"
        elif number_item == 3:     pc_item = "scissors"
    return pc_item


def compare(item1, item2):
    """ Compares the 2 items, based on what they are, returns a str

    Tie - "tie", Win - True, Lose - False (returns either "tie, True, or False")
    """
    if item1 == "rock" and item2 == "paper": return "False"
    elif item1 == "rock" and item2 == "rock": return "tie"
    elif item1 == "rock" and item2 == "scissors": return "True"

    if item1 == "paper" and item2 == "rock": return "True"
    elif item1 == "paper" and item2 == "paper": return "tie"
    elif item1 == "paper" and item2 == "scissors": return "False"

    if item1 == "scissors" and item2 == "paper": return "True"
    elif item1 == "scissors" and item2 == "rock": return "False"
    elif item1 == "scissors" and item2 == "scissors": return "tie"


def main():
    PC, Player = 0, 0 # scores
    quiter = "None" # starter variable for the while loop and program quiter.

    print("\n--First One To 10 Points First Wins")

    # This while loop basically asks player for input, and according to what's inputed, it does something
    while(quiter == "None"):

        materail = input("Rock, Paper, Scissors! -> ")

        # quit game switch
        if materail == "quit":
            quiter = "true"

        # print score
        if materail == "score":
            print("Player:", Player, "- PC:", PC)

        # start the "judging"
        if materail == "rock" or "scissors" or "paper":
            # returned_pc_item shouuld be a str of either "rock", "paper", or "scissors" (easier for me to do this)
            returned_pc_item = gen_pc_item()

            # if you won the current "duel"
            if(compare(materail, returned_pc_item)) == "True":
                Player += 1
                print("You won!\n" + "Player:", Player, "- PC:", PC)

            # if you tied the current "duel"
            elif(compare(materail, returned_pc_item)) == "tie": print("Tie!")

            # if you lost the current "duel"
            elif(compare(materail, returned_pc_item)) == "False":
                PC += 1
                print("You lost!\n" + "Player:", Player, "- PC:", PC)

        # checks to see if anyone has gotten 10 points yet.
        if PC >= 10:
            print("Game Over, You Lost!")
            quiter = "true"
        if Player >= 10:
            print("Game Over, You Win!")
            quiter = "true"

        # if the 'str': [materail] doesn't equal any of the listed string above, reloop
    print("-=GAME OVER=-")
main()
