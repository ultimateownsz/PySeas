from random import randint
from dataclasses import dataclass, field
from typing import List

from .money import Money
from .inventory import Inventory


@dataclass
class Player:

    name_of_player: str
    player_id: int
    inventory: List[str] = field(default_factory=list)
    wallet: int = 0
    board_index: int = 0

    def __post_init__(self):
        self.inventory = Inventory().items
        self.wallet = Money(currency="gold", worth=0).worth

    # self.roll_history_p1 = []
    # self.roll_history_p2 = []

    def print_info(self):
        print(
            f"Arrr.. Mateyy {self.name_of_player.capitalize()} Down below you can see your stats:\n"
        )
        print(
            f"Player: {self.name_of_player.capitalize()}\nInventory: {self.inventory}\nWallet: {self.wallet}\nBoard index: {self.board_index}\n"
        )

    def dice_roll(self):
        roll_results = [randint(1, 6) for _ in range(2)]
        total_roll = sum(roll_results)
        print(
            f"\n{self.name_of_player.capitalize()} throws the dices {roll_results[0]} and {roll_results[1]}. You rolled a total of {sum(roll_results)}\n"
        )
        # if self.player_id == 1:
        #     self.roll_history_p1.append(roll_results)
        # elif self.player_id == 2:
        #     self.roll_history_p2.append(roll_results)
        # print(f"Roll results p1: {self.roll_history_p1}\nRoll results p2: {self.roll_history_p2}")
        return total_roll

    def move_player(self, board):
        """
        This is the logic of the game, it moves the player when dices are throwed,
        and updates the player pos to the new pos
        """
        new_position = board.update_player_position(
            player=self, total_roll=self.dice_roll()
        )
        print(
            f"{self.name_of_player.capitalize()} moves to {board.locations_with_index[new_position]}\n"
        )
        return new_position

    def perform_action(self, board, new_position):
        """Made this function to call the board everytime the player got on a tile to call the function"""
        board.visit_locations_by_index(new_position)
        if new_position in board.locations_actions:
            board.locations_actions[new_position]()
