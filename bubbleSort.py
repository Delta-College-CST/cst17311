# Demonstrate "bubbling" largest element to end of list

# The Bubble Sort
def sort(list):
    for end in range (len(list)-1,0,-1):
        for i in range (end):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

# - - - - - - - - -  MAIN ROUTINE  - - - - - - - - - #

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

print(fruit)

fruit = sort(fruit)

print(fruit)
