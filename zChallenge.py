#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)


"""
imports the 'random' module
creates a list 'x'
loops 40 times
selects either 0 or 1
if 1 then add an integer from 1 to 10 to the list 'x'
if 0 then add a decimal from 1.0 to 10.9 to the list 'x'
print list 'x'
"""