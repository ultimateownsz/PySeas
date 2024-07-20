class Selling:
    def __init__(self, name: str, chest_worth: str) -> None:
        self.name = name
        self.chest_worth = chest_worth

    def __str__(self):
        return f"{self.name}"


chest_wealth = Selling(name="Chest of Wealth", chest_worth='9500')
chest_legend = Selling(name="Legendary Chest", chest_worth='8600')
chest_captain = Selling(name="Captain's Chest", chest_worth='560')
chest_cursed = Selling(name="Chest of the Cursed One", chest_worth='1160')
chest_greg = Selling(name="Chest of the drunken Greg", chest_worth='2500')
chest_mermaid = Selling(name="Mermaid's Chest", chest_worth='910')
chest_volcanic = Selling(name="Volcanic Chest", chest_worth='520')
chest_strong = Selling(name="Stronghold Chest", chest_worth='2000')
chest_rage = Selling(name="Chest of Doom", chest_worth='3500')
chest_ancient = Selling(name="Chest of the Ancients", chest_worth='3000')
