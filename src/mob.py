from dataclasses import dataclass as component
from map import Pos

@component
class Status:
    sneaking: bool
    poisoned: bool

@component
class Inventory:
    items: list[int] = field(default_factory=list)
    cash: int = 0

@component
class Equipment:
    right_hand: int = 0
    left_hand: int = 0
    armor: int = 0
    legs: int = 0
    boots: int = 0
    helmet: int = 0
    ring: int = 0
    amulet: int = 0

class ItemKind(Enum):
    ARMOR = 1
    MISC = 2
    WEAPON = 3
    CONSUMABLE = 4
    INGREDIENT = 5
    KEY = 6

@component
class Item:
    name: str = "an item"
    image: str = ""
    value: int = 0
    kind = ItemKind.MISC

class Slot(Enum):
    HEAD = 1
    TORSO = 2
    HANDS = 3
    FEET = 4
    NECK = 5
    RING = 6

@component
class Armor:
    value: int = 1
    slot: Slot = Slot.HEAD

@component
class Weapon:
    damage: int = 1
    uses_arrows: bool = False
    max_soul: int = 0
    current_soul: int = 0
    charge_usage: int = 0

@component
class TalkScript:
    name: str = "scripts/talk/default"
