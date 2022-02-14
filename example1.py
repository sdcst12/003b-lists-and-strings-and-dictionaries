#!python

'''
Using the "in" operator to search tuples, lists and dicts
'''

a = (3,4,5,6,7)
b = [3,4,5,6,7]
c = {
    "a" : 3,
    "b" : 4,
    "c" : 5,
    "d" : 6,
    "e" : 7
}

if 3 in a:
    print("found in tuple")
if 3 in b:
    print("found in list")
if 3 in c:
    print("value found in dict")
if "c" in c:
    print("key found in dict")

