from src.buying import *

class Money:
    '''The money class should be called something else perhaps, we should '''
    def __init__(self, currency: str, worth: int, max_worth: int = 1500000) -> None:
        self.currency = currency
        self.worth = worth
        self.max_worth = max_worth
        # self.purchase = basic_quest

   
    def buy(self, purchase_amount) -> None:
        self.worth -= purchase_amount
        self.worth = max(self.worth, 0)

    def buy_quest(self, quest) -> None:
        if self.worth >= quest.quest_worth:
            print(f"You have purchesed {quest.name} for {quest.quest_worth} {self.currency}")
            self.buy(quest.quest_worth)
        else:
            print("You don't have enough gold to buy a quest!")

    def sell(self, sell_amount) -> None:
        self.worth += sell_amount

    def sell_chest(self, chest) -> None:
        if self.worth <= chest.chest_worth and self.worth >= chest.chest_worth:
            print(f"You sold {chest.name} for {chest.chest_worth} {self.currency}")
            self.sell(chest.chest_worth)
        else:
            ("You don't have the items to sell!")

    def show_money(self) -> None:
        print(f"You have now an impressive amount of {self.worth} {self.currency}")

    # def extract_item(self, extract) -> None:
    #     if self.sell_chest:
    #         extract.inventory = Inventory.remove_item(chest)
        #     print(f"You sold {item} for {selling_price} {self.currency}")
        # else:
        #     print("Nothing like that is in your inventory!")

    # def minus(self, pocket: int) -> None:
    #     self.pocket = pocket
    #     self.buy_quest(pocket)

    # def plus(self) -> None:
        
                # self.item = Inventory.remove_item(item)
        # if self.item:
            
# self.worth <= chest.chest_worth and self.worth >= chest.chest_worth