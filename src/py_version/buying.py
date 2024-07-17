from dataclasses import dataclass

@dataclass
class Buying:
    '''There are some problems with how the game perceives buying items. it needs to be fixed or it needs to be reworked entirely.'''
    name: str
    quest_type: str
    quest_worth:int

basic_quest = Buying(name="Quest for the burried treasure",
                      quest_type="Basic Quest",
                      quest_worth=200)

medium_quest = Buying(name="Quest to the Lost Treasure",
                             quest_type="Medium Quest",
                             quest_worth=1000)

drunken_quest = Buying(name="Quest for the Drunken Sailor",
                        quest_type="Drunken Quest",
                        quest_worth=1250)

hard_quest = Buying(name="Quest for the Secret Vault",
                     quest_type="Hard Quest",
                     quest_worth=1750)