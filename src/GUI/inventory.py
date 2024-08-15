"""
inventory class for the players
this file contain types of items, like Chest
"""


class Chest:
    """ contain loot, and worth """
    def __init__(self, name: str) -> None:
        self.name = name


class Inventory:
    """ contain money, chests """
    def __init__(self) -> None:
        self.money: int = 0

        # items :
        self.chests: list[Chest] = []

    def add_chest(self, chest: Chest) -> None:
        self.chests.append(chest)

    def get_chests(self) -> list[Chest]:
        return self.chests.copy()
