from dataclasses import dataclass as component
from typing import Optional
import pyxel

@component
class Pos:
    map: int = 0
    x: int = 0
    y: int = 0

@component
class Sprite:
    image: int = 0
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0
    transparent: Optional[int] = None

    def draw(self, pos: Pos):
        pyxel.blt(pos.x, pos.y, self.image, self.x, self.y, self.w, self.h, self.transparent)

