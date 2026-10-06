from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re


def medium_logic():
    return "{YamlCompare(logic_difficulty >= 1)}"
def hard_logic():
    return "{YamlCompare(logic_difficulty == 2)}"
def needs_purple_coins(world: World, galaxy:str):
    return f"{{ItemValue({galaxy} PC:{world.options.purple_coin_count})}}"
def can_access_comet(world: World, type: int, galaxy: str):
    comet_list = {
        0: "Speedy",
        1: "Daredevil",
        4: "Purple",
        5: "Clone",
        6: "Double Time",
        7: "Romp",
        8: "Green",
        9: "Purple Comets| and |Has Clone"
    }
    if world.options.comet_medal_items:
        return f"(|Has {comet_list[type]} Comets| and |{galaxy} Comet Medal|)"
    else:
        return f"|Has {comet_list[type]} Comets|"