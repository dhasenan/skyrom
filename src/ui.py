import pyxel


class Widget:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

class Button(Widget):
    def __init__(self, text):
        self.text = text
        self.selected = false

class ButtonPanel(Widget):
    def __init__(self):
        super(self).__init__()
        self.buttons = []
