from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re


def medium_logic():
    return "{YamlCompare(Logic_Difficulty >= 1)}"
def hard_logic():
    return "{YamlCompare(Logic_Difficulty == 2)}"
