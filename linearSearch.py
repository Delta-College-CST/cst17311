# Demonstrate searching using the linear (sequential) search

# The Linear Search
def search(alist, item):
    pos = -1
    i = 0
    found = False

    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
            pos = i 
        else:
            i = i + 1

    return pos

# - - - - - - - - -  MAIN ROUTINE  - - - - - - - - - #

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

targetIndex = search(fruit,"kiwi")
if targetIndex >= 0:
    print("kiwi found at index:",targetIndex)
else:
    print("kiwi not found")

targetIndex = search(fruit,"grapes")
if targetIndex >= 0:
    print("grapes found at index:",targetIndex)
else:
    print("grapes not found")

