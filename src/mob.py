from dataclasses import dataclass as component

class Facing:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

@component
class Inventory:
    items: list[int] = field(default_factory=list)
    cash: int = 0

@component
class Pos:
    x: float = 0.0
    y: float = 0.0
    facing: int = Facing.DOWN

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

class ItemKind:
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

@component
class Armor:
    value: int = 1

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
