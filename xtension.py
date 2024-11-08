#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""


#Added spellcheck autocorrection autofill
from spellchecker import SpellChecker

spell = SpellChecker()

inventory = {'armor': 1, 'helmet': 1, 'potion': 4, 'dagger': 1}

def showInv():
    print("\n" + "=" * 40)
    print("|        INVENTORY                     |")
    print("=" * 40)
    if inventory:
        for item, quantity in inventory.items():
            print(f"|        {quantity} x {item.capitalize()[:15]:<25} |")
    else:
        print("|        Your inventory is empty       |")
    print("=" * 40 + "\n")


while True:
    #input
    print("\n" + "=" * 40)
    print("|        COMMANDS                      |")
    print("|------------------------------------  |")
    print("|        get <item>                    |")
    print("|        drop <item>                   |")
    print("|        show inventory (show)         |")
    print("|        quit (q)                      |")
    print("=" * 40)
    i = input("\n>>>")
    i = i.split()

    action = i[0].lower()

    if action == "q":
        print("Exiting the game... Goodbye!")
        break
    elif action in 'show':
        showInv()
    elif action in 'get' or action in 'drop' and len(i) > 1:
        item = spell.correction(i[1].lower())
        if action in 'get':
            inventory[item] = inventory.get(item, 0) + 1
            print(f"\nAdded {item.capitalize()} to your inventory.\n")
        elif action in 'drop':
            if item in inventory:
                inventory[item] -= 1
                if inventory[item] <= 0:
                    del inventory[item]
                print(f"\nDropped {item.capitalize()} from your inventory.\n")
            else:
                print(f"\n{item.capitalize()} is not in your inventory.\n")
    else:
        print("\nInvalid input. Try again.\n")