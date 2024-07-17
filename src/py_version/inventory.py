from dataclasses import dataclass, field
from typing import List

@dataclass
class Inventory:
    '''The inventory has some problems with appending the right items, also because we use lists it can become a bit disorganised to store those items'''
    items: List = field(default_factory=list)

    def extension(self, new_item: str) -> None:
        self.items.append(new_item)

    def remove_item(self, sell_item: str) -> str:
        if sell_item in self.items:
            self.items.remove(sell_item)
            return sell_item
        else:
            print("There is no such item in your inventory!")

    def show_eq(self) -> None:
        if not self.items:
            print("Your inventory is empty!")
        else:
            print("Your inventory:")
            for item in self.items:
                print(item)