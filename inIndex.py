# This example demonstrates the use of:
#  - the 'in' operator for lists
#  - the list index() function

fruit = ["orange", "mango", "watermelon", "kiwi", "pineapple", "banana"]

if "kiwi" in fruit:
	print("true")
else:
	print("false")

if "grapefruit" in fruit:
	print("true")
else:
	print("false")


i = fruit.index("kiwi")
print(i)

i = fruit.index("orange")
print(i)

i = fruit.index("grapefruit")
print(i)
