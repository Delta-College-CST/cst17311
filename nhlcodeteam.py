# This program allows a user to input NHL team codes.  It returns the
# associated team name.

nhlcodeList = []   # NHL code array (str)
nhlteamList = []   # NHL team array (str)

nhlfile = open("nhlteams.txt", "r") # Open file for reading

for line in nhlfile:
    line = line.strip()                 # Clean input line - remove newline
    inputLine = line.split(",")         # Read/split one line into array 
    nhlcodeList.insert(0,inputLine[0])  # Add to respective lists
    nhlteamList.insert(0,inputLine[1])

# Primary interaction - embed within continuation loop
endProgram = False
while endProgram == False:

    # Input prompt
    nhlcodeChoice = input("Enter code for NHL team: ")

    # Test if input code in code list.  If so, identify its index.
    # Use index to seek team name parallel in other array.
    # If NHL team code invalid, provide error message.
    if nhlcodeChoice in nhlcodeList:
        targetTeamIndex = nhlcodeList.index(nhlcodeChoice)
        print(nhlteamList[targetTeamIndex])
    else:
        print("Team not found.")

    # Prompt for continuation
    continueAnswer = input("Seek another team (y or n)? ")
    if continueAnswer != 'y':
        endProgram = True

                        
                           
