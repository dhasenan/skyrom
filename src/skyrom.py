import pyxel
import palette

from datetime import *

MOVE_SPEED = 8

def clamp(min_value, x, max_value):
    if x < min_value:
        return min_value
    if x > max_value:
        return max_value
    return x

class App:
    def __init__(self):
        self.color = 0
        self.tilemap = 0
        self.charpos = (76, 46)
        pyxel.init(160, 100, title="Skyrom", fps=10, quit_key=pyxel.KEY_NONE)
        pyxel.load("../res/game.pyxres")
        self.tm = pyxel.tilemap(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.charpos = (self.charpos[0], self.charpos[1] + MOVE_SPEED)
        if pyxel.btn(pyxel.KEY_UP):
            self.charpos = (self.charpos[0], self.charpos[1] - MOVE_SPEED)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.charpos = (self.charpos[0] - MOVE_SPEED, self.charpos[1])
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.charpos = (self.charpos[0] + MOVE_SPEED, self.charpos[1])
        self.charpos = (
                clamp(0, self.charpos[0], self.tm.width - 8),
                clamp(0, self.charpos[1], self.tm.height - 8))
        pyxel.camera(
                clamp(0, self.charpos[0] - pyxel.width // 2, self.tm.width - pyxel.width),
                clamp(0, self.charpos[1] - pyxel.height // 2, self.tm.height - pyxel.height))

    def draw(self):
        pyxel.bltm(0, 0, self.tilemap, 0, 0, 256, 256)
        pyxel.blt(self.charpos[0], self.charpos[1], 2, 0, 0, 10, 10, 14)

App()
