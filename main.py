"""Project Name: PySeas
Description: PySeas is an open-source project to create an engaging board game in Python,
inspired by Sea of Thieves. Ideal for game development enthusiasts and Python programmers
Author(s): Danilo Saiu (https://www.github.com/ultimateownsz),
Davit Alsemgeest (https://www.github.com/davidek523)
Date: 2024-09-08

Python Version: 1.0.0
Pygame Version: 0.0.1"""

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
from os.path import join
import sys

# import dataclasses and typchecking
from dataclasses import dataclass, field
from typing import List

# import pygame related
import pygame
from pytmx.util_pygame import load_pygame

# import Python specific objects, functions and functionality
# from src.py_version.board import Board
# from src.py_version.player import Player
from button import Button

# import Pygame specific objects, functions and functionality
from src.GUI.gameloop import GUI


class Launcher:
    def __init__(self) -> None:
        pass
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
import src.sprites


# @dataclass
# class CLI:
#     """ Command Line Interface, only using print statements """

#     players: List[Player] = field(init=False)
#     board: Board = field(init=False)
#     current_player_index: int = 0
#     running: bool = False

#     def __post_init__(self):
#         self.clear_screen()
#         self.players = [
#             Player(name_of_player="player 1", player_id=0),
#             Player(name_of_player="player 2", player_id=1),
#         ]
#         self.board = Board(self.players)

#     # logic which players turn it is
#     def toggle_player_index(self):
#         if self.current_player_index == 0:
#             self.current_player_index = 1
#         else:
#             self.current_player_index = 0

#     @staticmethod
#     def clear_screen():
#         """A function made to clear the screen in the Python boardgame.
#         Could be used or altered in Pygame if needed."""

#         os.system("cls" if os.name == "nt" else "clear")

#     def run(self):
#         self.initialize_game()
#         self.running = True
#         while self.running:
#             start_the_game = input(
#                 "Would you like to start the game? Press enter to continue. "
#             )
#             if start_the_game == "":
#                 self.clear_screen()
#                 break
#         self.board.print()
#         self.player_switch(self.players)

#     def player_switch(self, players):
#         """This decides what the current player pos is and then switch to the other player, when the player gets asked to end the turn"""

#         while True:
#             current_player = players[self.current_player_index]
#             print(
#                 f"\nIt's {current_player.name_of_player.capitalize()}'s turn! Current position is {self.board.players[self.current_player_index]}"
#             )

#             # end_turn = False

#             while True:
#                 roll_dice = input("\nDo you want to roll the dice? (yes/y) \n")
#                 if roll_dice.lower() in ["yes", "y"]:
#                     # current_player.dice_roll()
#                     current_player.move_player(self.board)
#                     if current_player:
#                         current_player.perform_action(
#                             self.board,
#                             new_position=self.board.players[self.current_player_index],
#                         )
#                     break
#                 else:
#                     print(
#                         "You made a mistake, you can only answer yes to roll the dice!"
#                     )
#                     continue

#             stop_turn = input("\nDo you want to end your turn? (yes/no) \n")
#             if stop_turn.lower() in ["yes", "y"]:
#                 self.toggle_player_index()
#                 Board(players).print()
#             elif stop_turn.lower() in ["no", "n"]:
#                 print("\nYou must continue your turn.")
#                 self.toggle_player_index()
#                 Board(players).print()
#             else:
#                 print("Input error. Please answer yes or no.")

#     def initialize_game(self):
#         print("Ahoy Mateyy To PySeas!\n")

#         for player in self.players:
#             while True:
#                 name = input(f"Enter player {player.player_id+1} name: ").strip()
#                 if 2 <= len(name) <= 10 and name.isalpha():
#                     player.name_of_player = name
#                     break
#                 else:
#                     print(
#                         "Input error. Player name should be between two characters and maximum ten characters containing only alphabets."
#                     )
#                     continue

#         # print(f"\nAhoy {self.players[0].name_of_player.capitalize()} & {self.players[1].name_of_player.capitalize()} to the start of the game!\n")
#         for player in self.players:
#             player.print_info()
#         return self.players


@dataclass
class GUI:
    """ Graphial User Interface version of the game, using pygame-ce """

    screen_size: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen: pygame.Surface = field(init=False)

    state: str = "main_menu" 

    # groups
    # all_sprites: pygame.sprite.Group = field(
    #     init=False, default_factory=pygame.sprite.Group
    # )
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()

    def __post_init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.org_screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.current_screen_size = self.org_screen_size
        pygame.display.set_caption("PySeas")

        self.players: list[src.sprites.Player] = [src.sprites.Player()]

        self.running = True
        self.import_assets()
        self.play(
            tmx_maps=self.tmx_map["map"], player_start_pos="Fort"
        )  # The start positions will be one of the 4 islands in the corners of the board

    def import_assets(self):
        """ load the map """
        # The map was made as a basic start for the game, it can be changes or altered if it is better for the overall flow of the game
        self.tmx_map = {
            "map": load_pygame(join(".", "data", "maps", "100x100_map.tmx"))
        }

        # # Define the path to the TMX file
        # tmx_path = os.path.join('data', 'maps', '100x100_map.tmx')
        # sprite_group = pygame.sprite.Group()

        # # Check if the file exists
        # if not os.path.exists(self.tmx_maps):
        #     print(f"Error: The file at {self.tmx_maps} does not exist.")
        #     return None

        # # Load the TMX file using load_pygame
        # tmx_data = load_pygame(tmx_path)
        # print(tmx_data.layers)

    # def setup(self, tmx_maps, player_start_pos):
    #     """ create tiles """
    #     islands = tmx_maps.get_layer_by_name("Islands")
    #     for x, y, surface in islands.tiles():
    #         # print(x * TILE_SIZE, y * TILE_SIZE, surface)
    #         src.sprites.Tile(
    #             self.all_sprites,
    #             pos=(x * TILE_SIZE, y * TILE_SIZE),
    #             surf=surface,
    #         )

    def run(self) -> None:
        """ main loop of the game """
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def get_font(self, size):
        return pygame.font.Font("fonts/antiquity-print.ttf", size)
    # font_name: Grand9k Pixel/grand9k_pixel

    def play(self, tmx_maps, player_start_pos):
        # self.screen.fill('white')
        PLAYER_MOUSE_POS = pygame.mouse.get_pos()

        """ create tiles """
        islands = tmx_maps.get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            # print(x * TILE_SIZE, y * TILE_SIZE, surface)
            src.sprites.Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

        back_button_surface = pygame.Surface((100, 100))
        back_button_surface.fill('black')

        BACK_BUTTON = Button(image=back_button_surface, pos=(100, 550), text_input="< Back", 
                                font=self.get_font(40), base_color='white', hovering_color='grey')
        
        for button in [BACK_BUTTON]:
            button.changeColor(PLAYER_MOUSE_POS)
            button.update(self.screen)

        # self.screen.blit(PLAYER_SCREEN_TEXT, PS_RECT)

        return BACK_BUTTON

    def options(self):
        self.screen.fill('white')
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPT_SCREEN_TXT = self.get_font(50).render('''OPTIONS''', True, 'black')
        OPT_RECT = OPT_SCREEN_TXT.get_rect(center=(623, 100))

        # TO DO: Adjust the button surface so it doesnt overlap with the other surfaces (DONE)

        back_button_surface = pygame.Surface((100, 100))
        back_button_surface.fill('white')

        res_button_surface = pygame.Surface((150, 100))
        res_button_surface.fill('white')

        sfx_button_surface = pygame.Surface((150, 100))
        sfx_button_surface.fill('white')

        diff_button_surface = pygame.Surface((150, 100))
        diff_button_surface.fill('white')

        BACK_BUTTON = Button(image=back_button_surface, pos=(100, 650), text_input="< Back", 
                                font=self.get_font(40), base_color='grey', hovering_color='black')
        
        RES_BUTTON = Button(image=res_button_surface, pos=(623, 250), text_input='Resolution',
                            font=self.get_font(40), base_color='grey', hovering_color='black')
        
        SFX_BUTTON = Button(image=res_button_surface, pos=(623, 365), text_input='Sound',
                            font=self.get_font(40), base_color='grey', hovering_color='black')
        
        DIFF_BUTTON = Button(image=res_button_surface, pos=(623, 475), text_input='Difficulty',
                            font=self.get_font(40), base_color='grey', hovering_color='black')
        
        for button in [BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(self.screen)

        self.screen.blit(OPT_SCREEN_TXT, OPT_RECT)

        return BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON

    def resolution(self):
        self.screen.fill('white')

        RES_MOUSE_POS = pygame.mouse.get_pos()

        RES_TEXT = self.get_font(50).render('RESOLUTION', True, 'black')
        RES_RECT = RES_TEXT.get_rect(center=(623, 100))

        fhd_button_surface = pygame.Surface((200, 100))
        fhd_button_surface.fill('white')
        hd_button_surface = pygame.Surface((200, 100))
        hd_button_surface.fill('white')
        third_button_surface = pygame.Surface((200, 100))
        third_button_surface.fill('white')
        back_button_surface = pygame.Surface((100, 100))
        back_button_surface.fill('white')

        FHD_BUTTON = Button(image=fhd_button_surface, pos=(623, 250), text_input="1920x1080", font=self.get_font(35), base_color='grey', hovering_color='black')
        HD_BUTTON = Button(image=hd_button_surface, pos=(623, 365), text_input="1280x720", font=self.get_font(35), base_color='grey', hovering_color='black')
        THIRD_BUTTON = Button(image=third_button_surface, pos=(623, 475), text_input="800x600", font=self.get_font(35), base_color='grey', hovering_color='black')
        BACK_BUTTON = Button(image=back_button_surface, pos=(100, 650), text_input="< Back", 
                                font=self.get_font(40), base_color='grey', hovering_color='black')

        for button in [FHD_BUTTON, HD_BUTTON, THIRD_BUTTON, BACK_BUTTON]:
            button.changeColor(RES_MOUSE_POS)
            button.update(self.screen)

        self.screen.blit(RES_TEXT, RES_RECT)

        return BACK_BUTTON, FHD_BUTTON, HD_BUTTON, THIRD_BUTTON

    def difficulty(self):
        '''I made this option for now as a idea. Maybe we could implement a sort of difficulty system in the game?'''
        self.screen.fill('white')

        DIFF_MOUSE_POS = pygame.mouse.get_pos()

        DIFF_TEXT = self.get_font(50).render('DIFFICULTY', True, 'black')
        DIFF_RECT = DIFF_TEXT.get_rect(center=(623, 100))

        easy_button_surface = pygame.Surface((200, 100))
        easy_button_surface.fill('white')
        medium_button_surface = pygame.Surface((200, 100))
        medium_button_surface.fill('white')
        hard_button_surface = pygame.Surface((200, 100))
        hard_button_surface.fill('white')
        back_button_surface = pygame.Surface((100, 100))
        back_button_surface.fill('white')

        EASY_BUTTON = Button(image=easy_button_surface, pos=(623, 250), text_input="Easy", font=self.get_font(35), base_color='grey', hovering_color='black')
        MEDIUM_BUTTON = Button(image=medium_button_surface, pos=(623, 365), text_input="Medium", font=self.get_font(35), base_color='grey', hovering_color='black')
        HARD_BUTTON = Button(image=hard_button_surface, pos=(623, 475), text_input="Hard", font=self.get_font(35), base_color='grey', hovering_color='black')
        BACK_BUTTON = Button(image=back_button_surface, pos=(100, 650), text_input="< Back", font=self.get_font(40), base_color='grey', hovering_color='black')

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(DIFF_MOUSE_POS)
            button.update(self.screen)

        self.screen.blit(DIFF_TEXT, DIFF_RECT)

        return BACK_BUTTON

    def main_menu(self):
        self.screen.fill('black')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = self.get_font(100).render('PYSEAS', True, 'white')
        MENU_RECT = MENU_TEXT.get_rect(center=(620, 100))

        # play_button_surface = pygame.Surface((300, 100))
        # play_button_surface.fill("brown")

        play_button_surface = pygame.Surface((370, 100))
        # play_button_surface.fill("brown")
        opt_button_surface = pygame.Surface((370, 100))
        # opt_button_surface.fill("brown")
        quit_button_surface = pygame.Surface((220, 100))
        # quit_button_surface.fill("brown")

        PLAY_BUTTON = Button(image=play_button_surface, 
                                pos=(623, 250), text_input='PLAY', font=self.get_font(45), base_color='white', hovering_color='grey')
        
        OPT_BUTTON = Button(image=opt_button_surface, 
                            pos=(623, 360), text_input='OPTIONS', font=self.get_font(45), base_color='white', hovering_color='grey')
        
        QUIT_BUTTON = Button(image=quit_button_surface, 
                            pos=(623, 470), text_input='QUIT', font=self.get_font(45), base_color='white', hovering_color='grey')
        
        self.screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)

        return PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON
    
    def scale_content(self, new_resolution):
        width_scale = new_resolution[0] / self.org_screen_size[0]
        height_scale = new_resolution[1] / self.org_screen_size[1]

        # Rescale the sprites
        for sprite in self.all_sprites:
            sprite.image = pygame.transform.scale(
                sprite.image, 
                (int(sprite.rect.width * width_scale), int(sprite.rect.height * height_scale))
            )
            sprite.rect.x = int(sprite.rect.x * width_scale)
            sprite.rect.y = int(sprite.rect.y * height_scale)

        # Rescale the players
        # for player in self.players:
        #     player.scale_player(width_scale, height_scale)

        # Update screen size
        self.screen = pygame.display.set_mode(new_resolution)
        self.current_screen_size = new_resolution

    def handle_events(self) -> None:
        """ get events like keypress or mouse clicks """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == 'main_menu':
                    PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON = self.main_menu()
                    if PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'play'
                    elif OPT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'options'
                    elif QUIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

                elif self.state == 'play':
                    BACK_BUTTON = self.play(tmx_maps=self.tmx_map["map"], player_start_pos="Fort")
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'main_menu'

                elif self.state == 'options':
                    BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON = self.options() #SFX_BUTTON is going to be implemented later
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'main_menu'
                    elif RES_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'res'
                    elif DIFF_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'diff'

                elif self.state == 'diff':
                    BACK_BUTTON = self.diff()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'options'

                # TODO: I had no time to correctly set up the resolution change, I will fix it later
                elif self.state == 'res':
                    BACK_BUTTON, FHD_BUTTON, HD_BUTTON, THIRD_BUTTON = self.res()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'options'
                    if FHD_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.scale_content((1920, 1080))
                    if HD_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.scale_content((1280, 720))
                    if THIRD_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.scale_content((800, 600))

        if self.state == 'main_menu':
            self.main_menu()
        elif self.state == 'play':
            self.play(tmx_maps=self.tmx_map["map"], player_start_pos="Fort")
        elif self.state == 'options':
            self.options()
        elif self.state == 'res':
            self.res()
        elif self.state == 'diff':
            self.diff()

        pygame.display.flip()
    pygame.quit()

    def update(self) -> None:
        """ update the player """
        for player in self.players:
            player.update()

    def render(self) -> None:
        """ draw sprites to the canvas """
        self.screen.fill('#000000')
        self.all_sprites.draw(surface=self.screen)

        # draw players on top of the other sprites
        for player in self.players:
            player.render(surface=self.screen)

    # pygame.display.update()


if __name__ == "__main__":
    # version choice is disabled for debugging reasons
    game = GUI()
    game.run()

    # print(
    #     """
    #       Welcome to Pyseas!
    #       Please select a version to play:
    #       1. CLI version
    #       2. GUI version"""
    # )
    # choice: str = input("Enter the number of your choice: ")
    # while choice not in ['1', '2']:
    #     choice = input("Enter the number of your choice: ")

    # if choice == "1":
    #     CLI().run()
    # elif choice == "2":
    #     GUI().run()
