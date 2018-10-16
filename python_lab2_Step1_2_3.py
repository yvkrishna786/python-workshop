# lab LISTS using .append() - list can be change (mutated)
l = ['a', 1, 18.2]
print(l[0])
print(l[1])
print(l[2])
l.append("new")
print(l)
print(l[3])

# lab TUPLES - A tuple is immutable
t = ('a', 1, 18.2)
print(t[0])

# Dictionaries
d = {"apples": 5, "pears": 2, "oranges": 9}
print(d["pears"])
d["pears"] = 6
d["bananas"] = 24
print(d)

#OrderedDict Collection
from collections import OrderedDict
od = OrderedDict()
od["apples"] = 5
od["pears"] = 2
od["oranges"] = 9
print(od["pears"])
od["bananas"] = 12
print(od)

# Python for Loop Syntax
for i in range(7):
    print(i)

# for loop - Choosing Variable Names
names = ["Venkat", "Vinay", "Satya"]
for name in names:
    print(name)

# for loop - Iterating Through a Dictionary
Car_inventory = {"Maruthi": 7, "Ford": 2, "Audi": 9}
for Car in Car_inventory:
    print(Car)

list(Car_inventory.items())
for bike in Car_inventory.items():
    print(Car)

# assign a collection of items to a collection of variables - this is called unpacking.
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

#Conditional Loops
i = 0
while i < 9:
    print(i)
    i += 1

from time import sleep
while True:
    try:
        print("Polling.")
        # Poll some resource
        sleep(1)
    except KeyboardInterrupt:
        break
        