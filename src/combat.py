# Turn-based combat with a menu
from esper.esper import component_for_entity as comp


class CombatMode:
    def __init__(self, player, friendlies, enemies):
        self.player = player
        self.friendlies = friendlies
        self.enemies = enemies
        self.round = 0
        # do we have a surprise round?
        self.have_surprise_round = False
        # do we have a getting-into-range round?
        self.have_range_round = False

    def process_turn(self):
        if self.round == 0:

    def update(self, app):
        pass

    def draw(self):
        pass
