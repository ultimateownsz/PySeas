"""
inventory class for the players
this file contain types of items, like Chest
"""


class Chest:
    """ contain loot, and worth """
    def __init__(self, name: str) -> None:
        self.name = name


class Quest:
    """ TODO: make the docstrings """
    def __init__(self) -> None:
        self.completed = False


class Inventory:
    """ contain money, chests, quests """
    def __init__(self) -> None:
        # special attribute
        self.money: int = 0

        # items :
        self.chests: list[Chest] = []
        self.quests: list[Quest] = []

    def add_chest(self, chest: Chest) -> None:
        """ apend a chest to the inventory """
        self.chests.append(chest)

    def get_chests(self) -> list[Chest]:
        """ Return a copy of the chests list """
        return self.chests.copy()

    def add_quest(self, quest: Quest) -> None:
        """ apend a quest to the inventory """
        self.quests.append(quest)

    def get_quests(self) -> list[Quest]:
        """ Return a copy of the quests list """
        return self.quests.copy()
