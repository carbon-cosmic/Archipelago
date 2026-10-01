from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re


def medium_logic():
    return "{YamlCompare(logic_difficulty >= 1)}"
def hard_logic():
    return "{YamlCompare(logic_difficulty == 2)}"
def needs_purple_coins(galaxy):
    return f"{{OptionCount(|{galaxy} Purple Coin|, purple_coin_count)}}"
