"""
Represents the GameRunning state, where the player controls a ship and interacts with the game world.
"""

import os
import json
import pygame
from pytmx.util_pygame import load_pygame  # type: ignore
from typing import List

from src.states.base_state import BaseState
from src.states.paused import Paused
from src.inventory import Inventory

from src.settings import TILE_SIZE
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
        
        # Initialize player inventory
        self.player_inventory = Inventory()
        self.load_inventory_from_json("data/inventory.json")


        # The start positions will be one of the 4 islands in the corners of the board
        self.setup(player_start_positions=["top_left_island", "bottom_right_island"])

    def setup(self, player_start_positions: List[str]) -> None:
        """
        setup the map and player from the tiled file
        """
        self.tmx_map = {
            "map": load_pygame(os.path.join(".", "data", "maps", "100x100_map.tmx"))
        }

        # Islands
        islands = self.tmx_map["map"].get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            src.sprites.Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

        # Objects
        ships_layer = self.tmx_map["map"].get_layer_by_name("Ships")
        for obj in ships_layer:
            print(f"Object name: {obj.name}, Properties: {obj.properties}")
            for starting_position in player_start_positions:
                if obj.name == "Player" and obj.properties["pos"] == starting_position:
                    player = src.sprites.Player(name=obj.name, pos=(obj.x, obj.y), groups=self.all_sprites)
                    self.players.append(player)
        
        if not self.players:
            raise ValueError("No player starting positions found in the map.")

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

    def switch_player(self):
        """
        switch to the next player
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def update(self, events) -> None:
        """
        update each sprites and handle events
        """

        self.active_player = self.players[self.current_player_index]

        self.all_sprites.update()

        # get events like keypress or mouse clicks
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:  # Toggle inventory with "I" key
                    self.game_state_manager.enter_state(
                        Paused(self.game_state_manager, self.player_inventory)
                    )
                elif event.key == pygame.K_TAB:  # placeholder for switching players
                    self.switch_player()

    def render(self, screen) -> None:
        """draw sprites to the canvas"""
        screen.fill("#000000")
        self.all_sprites.draw(
            self.active_player.rect.center,
            self.active_player.player_preview,
            self.active_player.player_preview_rect,
        )

        pygame.display.update()
