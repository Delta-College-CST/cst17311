# This reads parallel arrays containing user IDs and passwords.
# It then uses these to validate a login.

# Declare list variables globally
userid   = []    
password = []

# Load state info into two parallel arrays.  Be sure to strip
# off the password field for excess whitespace characters.
def loadFiles():
    loginfile = open("idpass.txt", "r")   
    for infoline in loginfile:
        inid, inpass = infoline.split(",")
        inpass = inpass.strip()
        userid.append(inid)
        password.append(inpass)

# Determine if login ID is valid (i.e. in list)
def loginExists(login):
    if login in userid:
        return True
    else:
        return False

# Given a valid login and candidate password, scan
# lists to determine if a valid match
def passwordMatchesLogin(login,testpass):

    listLength = len(userid)    # Get limit for searching

    # Seek index of login ID
    index = -1
    for i in range(listLength):
        if userid[i] == login:
            index = i

    # Use index to access/test password stored in parallel
    if password[index] == testpass:
        outcome =  True
    else:
        outcome = False
    return outcome

# -------------------------------------------------------- #

loadFiles()   # Read data files and populate lists

# Validate existence of user ID
loginid = input("User ID: ")
while loginExists(loginid) == False:
    print("Invalid user ID - Please re-enter")
    loginid = input("User ID: ")

# Prompt user for password. Validate userId/password pair
# from password list 
inputpass = input("Enter password for user " + loginid + ": ")
while passwordMatchesLogin(loginid,inputpass) == False:
    print("Invalid password - Please re-enter")   
    inputpass = input("Enter password for user " + loginid + ": ")

# Notify of successful login
print("Logged in OK")



