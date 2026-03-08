from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState
import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def groupTwoUnlock(world: World, state: CollectionState, player: int):
    return state.count_from_list_unique(list(world.item_name_groups["Group 2"]), player) >= 4

def groupThreeUnlock(world: World, state: CollectionState, player: int):
    return state.count_from_list_unique(list(world.item_name_groups["Group 3"]), player) >= 7

def groupFourUnlock(world: World, state: CollectionState, player: int):
    if state.count_from_list_unique(list(world.item_name_groups["Group 4"]), player) >= 11 and state.count_from_list_unique(list(world.item_name_groups["Group Progression"]), player) >= 4:
        return True
    return False

def groupFiveUnlock(world: World, state: CollectionState, player: int):
    return state.count_from_list_unique(list(world.item_name_groups["Group 5"]), player) >= 17

def groupSixUnlock(world: World, state: CollectionState, player: int):
    return state.count_from_list_unique(list(world.item_name_groups["Group 6"]), player) >= 22
