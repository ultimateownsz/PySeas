""" hold the invotory of the players """
from dataclasses import dataclass, field
from typing import List


@dataclass
class Inventory:
    """The inventory has some problems with appending the right items,
    also because we use lists it can become a bit disorganised to store those items"""

    items: List[str] = field(default_factory=list)

    def extension(self, new_item: str) -> None:
        """ add item to the inventory """
        self.items.append(new_item)

    def remove_item(self, sell_item: str) -> None:
        """ remove sell_item from inventory """
        if sell_item in self.items:
            self.items.remove(sell_item)
        else:
            print("There is no such item in your inventory!")

    def show_eq(self) -> None:
        """ print the content of the inventory """
        if not self.items:
            print("Your inventory is empty!")
        else:
            print("Your inventory:")
            for item in self.items:
                print(item)
