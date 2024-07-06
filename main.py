import os

from board import Board
from player import Player

from validate_inputs import validate_inputs

class Game:

    def __init__(self) -> None:
        self.running = False
        self.player1 = Player(name_of_player="", player_id=0)
        self.player2 = Player(name_of_player="", player_id=1)
        self.players = [self.player1, self.player2]
        self.current_player_index = 0
        self.board = Board(self.players)

    # logic which players turn it is
    def toggle_player_index(self):
        if self.current_player_index == 0:
            self.current_player_index = 1
        else:
            self.current_player_index = 0

    def run(self):
        self.initialize_game()
        self.running = True
        while self.running:
            start_the_game = validate_inputs("Would you like to start the game? Press enter to continue. ", str)
            if start_the_game == "":
                self.clear_screen()
                break
        self.board.print()

    def player_switch(self, players):
        '''This decides what the current player pos is and then switch to the other player when the player gets asked to end the turn'''

        while True:
            current_player = players[self.current_player_index]
            print(f"\nIt's {current_player.name_of_player.capitalize()}'s turn! Current position is {self.board.players[self.current_player_index]}")

            # end_turn = False

            while True:
                roll_dice = validate_inputs("\nDo you want to roll the dice? (yes/y) \n")
                if roll_dice.lower() in ["yes", "y"]:
                    # current_player.dice_roll()
                    current_player.move_player(self.board)
                    if current_player:
                        current_player.perform_action(self.board, new_position=self.board.players[self.current_player_index])
                    break
                else:
                    print("You made a mistake, you can only answer yes to roll the dice!")
                    continue

            stop_turn = validate_inputs("\nDo you want to end your turn? (yes/no) \n")
            if stop_turn.lower() in ["yes", "y"]:
                self.toggle_player_index()
                Board(players).print()  
            elif stop_turn.lower() in ["no", "n"]:
                print("\nYou must continue your turn.")
                self.toggle_player_index()
                Board(players).print()
            else:
                print("Input error. Please answer yes or no.")


    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def initialize_game(self):
        print("Ahoy Mateyy To The Sea of Thieves!\n")

        for player in self.players:
            while True:
                name = validate_inputs(f"Enter player {player.player_id+1} name: ", str).strip()
                if 2 <= len(name) <= 10 and name.isalpha():
                    player.name_of_player = name
                    break
                else:
                    print("Input error. Player name should be between two characters and maximum ten characters containing only alphabets.")
                    continue

        # print(f"\nAhoy {self.players[0].name_of_player.capitalize()} & {self.players[1].name_of_player.capitalize()} to the start of the game!\n")
        for player in self.players:
            player.print_info()
        return self.players


if __name__ == "__main__":
    game = Game()
    game.run()
    game.player_switch(game.players)
