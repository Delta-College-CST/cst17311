# This program plays a state capital game.  It randomly picks a
# state and prompts the user for the capital.  A counter keeps
# track of correct answers.
import random

# -------------------------------------------------------- #

statename = []   # Declare arrays to store state name
statecap  = []   # and state capital in parallel.
  
NUMBER_OF_STATES = 50

# Load state info into two parallel arrays.  Note the "strip"
# function used to remove extraneous "white space" characters.
datafile = open("statecaps.txt", "r")   
for stateline in datafile:
    code, name, capital = stateline.split(",")
    name = name.strip()
    capital = capital.strip()
    statename.append(name)
    statecap.append(capital)

# Begin game loop
continueStatus = True
numGames   = 0
numCorrect = 0

while continueStatus == True:

    numGames = numGames + 1   # Incerement number games played
    
    # Randomly select index 0..49
    randchoice = random.randrange(NUMBER_OF_STATES)

    # Using index, select random state name and capital
    targetstate = statename[randchoice]
    targetstatecap = statecap[randchoice]

    # Prompt for user choice
    prompt = "What is the capital of " + targetstate + "?  "
    usercap = input(prompt)

    # Test user solution
    if usercap == targetstatecap:
        numCorrect = numCorrect + 1   # Incerement number correct answers
        print("CORRECT"   + "\n")
    else:
        print("Incorrect, it is " + targetstatecap + "\n")

    userContinuation = input("Do you wish to try again (y or n)? ")
    if userContinuation != "y":
        continueStatus = False

print("You answered",numCorrect,"out of",numGames,"state capitals.")
        



