import pyxel
import palette
import menu

from datetime import *

MOVE_SPEED = 8

def clamp(min_value, x, max_value):
    if x < min_value:
        return min_value
    if x > max_value:
        return max_value
    return x

class MapMode:
    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.charpos = (76, 46)
        self.tm = pyxel.tilemap(0)

    def update(self, app):
        if pyxel.btn(pyxel.KEY_DOWN):
            self.charpos = (self.charpos[0], self.charpos[1] + MOVE_SPEED)
        if pyxel.btn(pyxel.KEY_UP):
            self.charpos = (self.charpos[0], self.charpos[1] - MOVE_SPEED)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.charpos = (self.charpos[0] - MOVE_SPEED, self.charpos[1])
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.charpos = (self.charpos[0] + MOVE_SPEED, self.charpos[1])
        if pyxel.btn(pyxel.KEY_ESCAPE):
            app.push_mode(menu.pause_menu())
        self.charpos = (
                clamp(0, self.charpos[0], self.tm.width - 8),
                clamp(0, self.charpos[1], self.tm.height - 8))
        pyxel.camera(
                clamp(0, self.charpos[0] - pyxel.width // 2, self.tm.width - pyxel.width),
                clamp(0, self.charpos[1] - pyxel.height // 2, self.tm.height - pyxel.height))

    def draw(self):
        pyxel.bltm(0, 0, self.tilemap, 0, 0, 256, 256)
        pyxel.blt(self.charpos[0], self.charpos[1], 2, 0, 0, 10, 10, 14)
        pyxel.rect(4, 4, 20, 10, 0)
        pyxel.text(5, 5, "text!", 5)

class App:
    def __init__(self):
        pyxel.init(160, 100, title="Skyrom", fps=10, quit_key=pyxel.KEY_NONE)
        pyxel.load("../res/game.pyxres")
        self.mode = MapMode(0)
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
        self.mode.draw()
        if self.popup_timeout > 0:
            self.popup_timeout -= 1
            pyxel.rect(10, 10, pyxel.width - 20, 10, 2)
            pyxel.rect(11, 11, pyxel.width - 22, 8, 0)
            pyxel.text(12, 12, self.popup_message, 15)

App()

