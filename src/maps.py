from dataclasses import dataclass as component
from base import Sprite, Pos
from esper import esper
import menu
import pyxel

MOVE_SPEED = 8

def clamp(min_value, x, max_value):
    if x < min_value:
        return min_value
    if x > max_value:
        return max_value
    return x

@component
class Map:
    tilemap: int = 0
    x: int = 0
    y: int = 0
    w: int = 256
    h: int = 256

    def draw(self):
        pyxel.bltm(0, 0, self.tilemap, self.x, self.y, self.w, self.h)


class MapMode:
    def __init__(self, map_entity, player_entity):
        self.map_entity = map_entity
        self.player_entity = player_entity
        self.tm = pyxel.tilemap(esper.component_for_entity(map_entity, Map).tilemap)

    def update(self, app):
        charpos = esper.component_for_entity(self.player_entity, Pos)
        m = esper.component_for_entity(self.map_entity, Map)
        if pyxel.btn(pyxel.KEY_DOWN):
            charpos.y += MOVE_SPEED
        if pyxel.btn(pyxel.KEY_UP):
            charpos.y -= MOVE_SPEED
        if pyxel.btn(pyxel.KEY_LEFT):
            charpos.x -= MOVE_SPEED
        if pyxel.btn(pyxel.KEY_RIGHT):
            charpos.x += MOVE_SPEED
        if pyxel.btn(pyxel.KEY_ESCAPE):
            app.push_mode(menu.pause_menu())
        charpos.x = clamp(m.x, charpos.x, m.w + m.x - 8)
        charpos.y = clamp(m.y, charpos.y, m.h + m.y - 8)
        pyxel.camera(
                clamp(m.x, charpos.x - pyxel.width // 2, m.w - pyxel.width),
                clamp(m.y, charpos.y - pyxel.height // 2, m.h - pyxel.height))

    def draw(self):
        esper.component_for_entity(self.map_entity, Map).draw()
        for ent, (pos, sprite) in esper.get_components(Pos, Sprite):
            if pos.map == self.map_entity:
                sprite.draw(pos)
