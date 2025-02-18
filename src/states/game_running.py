"""
Represents the GameRunning state, where the player controls a ship and interacts with the game world.
"""

import os
import json
import pygame
from pytmx.util_pygame import load_pygame  # type: ignore
from typing import List
import random

from src.states.base_state import BaseState
from src.states.paused import Paused
from src.inventory import Inventory
from src.support import import_folder, coast_importer, all_character_import
from src.sprites import AnimatedSprites

from src.settings import TILE_SIZE, WORLD_LAYERS
import src.sprites


class GameRunning(BaseState):
    """
    Represents the GameRunning state, where the player controls a ship and interacts with the game world.

    Responsibilities:
      - Loads the game map and player starting position.
      - Manages player inventories.
      - Updates game entities.
      - Renders the game world on the screen.
      - Handles player switching.
    """

    def __init__(self, game_state_manager) -> None:
        super().__init__(game_state_manager)

        self.players = []
        self.current_player_index = 0
        self.all_sprites = src.sprites.AllSprites()

        # store dice rolls and turn order
        self.dice_rolls = None
        self.turn_order = None
        
        # Initialize player inventory
        self.clock = pygame.Clock()
        self.player_inventory = Inventory()
        self.load_inventory_from_json("data/inventory.json")


        # The start positions will be one of the 4 islands in the corners of the board
        self.setup(player_start_positions=["top_left_island", "bottom_right_island"])

        # Roll dice to determine turn order
        self.roll_dice(self.game_state_manager.screen)

    def setup(self, player_start_positions: List[str]) -> None:
        """
        setup the map and player from the tiled file
        """
        self.tmx_map = {
            "map": load_pygame(os.path.join(".", "data", "new_maps", "100x100_map.tmx"))
        }

        self.world_frames = {
            "water": import_folder(".", "images", "tilesets", "temporary_water"),
            "coast": coast_importer(6, 6, ".", "images", "tilesets", "coast"),
            "ships": all_character_import(".", "images", "tilesets", "ships")
        }

        # Sea
        for x, y, surface in self.tmx_map["map"].get_layer_by_name("Sea").tiles():
            src.sprites.Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, WORLD_LAYERS["bg"])

        # Water animated
        for obj in self.tmx_map["map"].get_layer_by_name("Water"):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    AnimatedSprites((x, y), self.world_frames["water"], self.all_sprites, WORLD_LAYERS["water"])

        # Shallow water
        for x, y, surface in self.tmx_map["map"].get_layer_by_name("Shallow Sea").tiles():
            src.sprites.Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, WORLD_LAYERS["bg"])

        # Islands
        islands = self.tmx_map["map"].get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            src.sprites.Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, WORLD_LAYERS["bg"])

        # Enitites
        for obj in self.tmx_map["map"].get_layer_by_name("Ships"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                self.player = src.sprites.Player(
                    pos = (obj.x, obj.y), 
                    frames = self.world_frames["ships"]["player_test_ship"], 
                    groups = self.all_sprites)

        # Coast
        for obj in self.tmx_map["map"].get_layer_by_name("Coast"):
            terrain = obj.properties["terrain"]
            side = obj.properties["side"]
            AnimatedSprites((obj.x, obj.y), self.world_frames["coast"][terrain][side], self.all_sprites, WORLD_LAYERS["bg"])

    def load_inventory_from_json(self, file_path: str):
        """Load initial inventory items from JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                items = json.load(f)
                for item_name, properties in items.items():
                    quantity = properties.get("quantity", 1)  # Default to 1 if missing
                    for player in self.players:
                        player.player_inventory.add_item(item_name, quantity)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error: The file at {file_path} does not exist.")

    def roll_dice(self, screen) -> None:
        """Roll dice for each player and determine turn order."""
        self.dice_rolls = {player.name: random.randint(1, 6) for player in self.players}

        # sort players by their dice rolls (highest roll goes first)
        sorted_players = sorted(
            self.dice_rolls.items(), key=lambda player: player[1], reverse=True
        )

        # display the dice rolls using placeholders
        self.display_dice(screen, self.dice_rolls)

        font = pygame.font.Font(None, 48)
        screen.fill((0, 0, 0))  # Clear the screen

        # show the player who goes first
        starting_player = font.render(
            f"{sorted_players[0][0]} goes first!", True, (255, 255, 255)
        )
        screen.blit(starting_player, (10, 300))

        pygame.display.update()

        # return sorterd players for turn order
        return [p[0] for p in sorted_players]
    
    def display_dice(self, screen, dice_rolls):
        """Display rectangles as placeholders for dice results."""
        font = pygame.font.Font(None, 48)

        x_offset = 100
        y_offset = 100

        for idx, (player_name, roll) in enumerate(dice_rolls.items()):
            # draw rectancle placeholder
            pygame.draw.rect(screen, (255, 0, 0), (x_offset, y_offset, 100, 100))

            # display the dice roll inside the rectangle
            text = font.render(str(roll), True, (255, 255, 255))
            screen.blit(text, (x_offset + 30, y_offset + 30))

            # display the player's name below the rectangle
            name_text = font.render(player_name, True, (255, 255, 255))
            screen.blit(name_text, (x_offset, y_offset + 120))

            x_offset += 150 # shift to the right for the next player

        pygame.display.update()

    def display_turn_indicator(self, screen: pygame.Surface) -> None:
        """Display the current player's turn indicator."""
        font = pygame.font.Font(None, 36)
        current_player_name = self.players[self.current_player_index].name
        text = font.render(f"{current_player_name}'s turn", True, (255, 255, 255))
        screen.blit(text, (10, 10)) # position the text at the top-left corner

    def switch_player(self):
        """
        switch to the next player
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.dice_rolls = None  # reset dice rolls when switching players
    
    def update(self, events) -> None:
        """
        update each sprites and handle events
        """
        dt = self.clock.tick() / 1000
        self.all_sprites.update(dt)

        # get events like keypress or mouse clicks
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:  # Toggle inventory with "I" key
                    self.game_state_manager.enter_state(
                        Paused(self.game_state_manager, self.player_inventory)
                    )
                elif event.key == pygame.K_SPACE:  # trigger dice roll with space key
                    turn_order = self.roll_dice(self.game_state_manager.screen)
                    # self.players = [player for player in self.players if player.name in turn_order]
                elif event.key == pygame.K_RETURN:  # switch player with enter key
                    self.switch_player()

    def render(self, screen) -> None:
        """draw sprites to the canvas"""
        screen.fill("#000000")
        self.all_sprites.draw(
            self.player.rect.center
        )
        self.display_turn_indicator(screen) # display turn indicator

        # display the dice rolls using placeholders
        if self.dice_rolls:
            self.display_dice(screen, self.dice_rolls)

        pygame.display.update()
