import pyxel
import palette
import menu
import maps
from base import *

from datetime import *
from esper import esper

def clamp(min_value, x, max_value):
    if x < min_value:
        return min_value
    if x > max_value:
        return max_value
    return x

class App:
    def __init__(self):
        pyxel.init(160, 100, title="Skyrom", fps=10, quit_key=pyxel.KEY_NONE)
        pyxel.load("../res/game.pyxres")
        self.map_entity = esper.create_entity()
        esper.add_component(self.map_entity, maps.Map())
        self.player_entity = esper.create_entity()
        esper.add_component(self.player_entity, Pos(self.map_entity, 47, 18))
        esper.add_component(self.player_entity, Sprite(2, 0, 0, 10, 10, 14))
        self.mode = maps.MapMode(self.map_entity, self.player_entity)
        self.mode_stack = [self.mode]
        self.popup_message = ""
        self.popup_timeout = 0
        pyxel.run(self.update, self.draw)

    def push_mode(self, mode):
        self.mode_stack.append(mode)
        self.mode = mode

    def pop_mode(self):
        if len(self.mode_stack) < 2:
            raise Exception("no more modes to pop")
        self.mode_stack = self.mode_stack[:-1]
        self.mode = self.mode_stack[-1]

    def show_popup(self, message, timeout = 10):
        self.popup_message = message
        self.popup_timeout = timeout

    def update(self):
        self.mode.update(self)

    def draw(self):
        for mode in self.mode_stack:
            mode.draw()
        if self.popup_timeout > 0:
            self.popup_timeout -= 1
            pyxel.rect(10, 10, pyxel.width - 20, 10, 2)
            pyxel.rect(11, 11, pyxel.width - 22, 8, 0)
            pyxel.text(12, 12, self.popup_message, 15)

App()

