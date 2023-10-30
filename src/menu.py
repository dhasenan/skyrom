import pyxel

import collections

from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass
class Button:
    title: str
    action: Callable[[Any], None]

@dataclass
class Color:
    bg: int = 0
    fg: int = 6
    selected: int = 11

@dataclass
class Style:
    color: Color = field(default_factory = Color)
    border_color: Color = field(default_factory = Color)
    width: int = 80
    button_height: int = 10
    button_width: int = 70
    margin: int = 2
    border_size: int = 1
    selected_border_size: int = 1

class MenuMode:
    def __init__(self, title, buttons, style = None):
        self.title = title
        self.buttons = buttons
        self.selected = 0
        self.style = style or Style()

    def update(self, app):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            # which button are we hovering over?
            pass
        if pyxel.btn(pyxel.KEY_DOWN):
            self.selected += 1
            if self.selected >= len(self.buttons):
                self.selected = len(self.buttons) - 1
        if pyxel.btn(pyxel.KEY_UP):
            self.selected -= 1
            if self.selected < 0:
                self.selected = 0
        if pyxel.btn(pyxel.KEY_RETURN):
            self.buttons[self.selected].action(app)

    def draw(self):
        pyxel.cls(self.style.color.bg)
        pyxel.text(self.style.margin, self.style.margin, self.title, self.style.color.fg)
        top_margin = 10
        left = (self.style.width - self.style.button_width) // 2
        button_width = self.style.width - 2 * self.style.margin
        layout_height = self.style.button_height + self.style.margin
        text_offset = (self.style.button_height - 5) // 2
        text_left = left + self.style.margin + self.style.border_size
        for i, button in enumerate(self.buttons):
            top = top_margin + i * layout_height
            border_fg = self.style.border_color.fg
            text_fg = self.style.color.fg
            if i == self.selected:
                border_fg = self.style.border_color.selected
                text_fg = self.style.color.selected
            # first the border
            pyxel.rect(left + 1, top + 1, self.style.button_width, self.style.button_height,
                    self.style.border_color.bg)
            pyxel.rect(left, top, self.style.button_width, self.style.button_height,
                    border_fg)
            # inside
            pyxel.rect(
                    left + 1,
                    top + 1,
                    self.style.button_width - 2,
                    self.style.button_height - 2,
                    self.style.color.bg)
            # text
            pyxel.text(text_left, top + text_offset, button.title, text_fg)

def pause_menu():
    return MenuMode("Main Menu", [
        Button("Quit", lambda app: pyxel.quit()),
        Button("Save", lambda app: app.show_popup("Game saved!")),
        Button("Continue", lambda app: app.pop_mode()),
    ])
