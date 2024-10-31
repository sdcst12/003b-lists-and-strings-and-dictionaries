"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to make use of the string.split() method in order to separate the item name from the action that precedes it.
"""

def main():
    inventory = ['helmet', 'sword', 'health potion']

    while True:
        