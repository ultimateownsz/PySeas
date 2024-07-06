class Inventory:
    '''The inventory has some problems with appending the right items, also because we use lists it can become a bit disorganised to store those items'''
    def __init__(self,):
        self.inventory = []

    def extension(self, new_item: str) -> None:
        self.inventory.append(new_item)

    def remove_item(self, sell_item: str) -> str:
        if sell_item in self.inventory:
            self.inventory.remove(sell_item)
            return sell_item
        else:
            print("There is no such item in your inventory!")

    def show_eq(self) -> None:
        if not self.inventory:
            print("Your inventory is empty!")
        else:
            print("Your inventory:")
            for item in self.inventory:
                print(item)