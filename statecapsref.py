# This program offers a simple reference for states and their
# capitals.  If the user enters a two-character state code,
# the program identifies the state and the capital.

# -------------------------------------------------------- #

statecode = []   # Declare arrays to store state code
statename = []   # state code and state capital 
statecap  = []   # in parallel.
  
NUMBER_OF_STATES = 50

# Load state info into three parallel arrays.  Note the "strip"
# function used to remove extraneous "white space" characters.
datafile = open("statecaps.txt", "r")   
for stateline in datafile:
    code, name, capital = stateline.split(",")
    code = code.strip()
    name = name.strip()
    capital = capital.strip()
    statecode.append(code)
    statename.append(name)
    statecap.append(capital)

continueStatus = True   # Initialize continuation status

# Begin primary program loop
while continueStatus == True:

    stateCodeInput = input("Enter state code: ")

    # Test state code read in by user.  If it exists, search for its
    # index.  Retain the index and use to get the related state name
    # and state capital stored at the same index.
    if stateCodeInput in statecode:
        
        stateIndex = statecode.index(stateCodeInput)
        targetState = statename[stateIndex]
        targetCap  = statecap[stateIndex]

        # Print successful search results
        print(stateCodeInput,"is",targetState,"with capital",targetCap)

    else:
        print("Invalid state code")   # Write message for invalid input

    # Manage continuation opiton
    userContinuation = input("Do you wish to try again (y or n)? ")
    if userContinuation != "y":
        continueStatus = False
        
