from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.

# You can also return a string from your function, and it will be evaluated as a requires string.

def canAccessComet(type):
    if type == 4:
        return "OptOne(|Grand Star (Purple Coins)|)"
    comet_list = {
        0: "Speedy",
        1: "Daredevil",
        2: "Cosmic",
        3: "Fast-Foe"
    }
    return f"{{OptAll(|{comet_list[type]} Comets| AND |Prankster Comets|)}}"
