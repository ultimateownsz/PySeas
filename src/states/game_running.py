import sys
import os
import pygame
from pytmx.util_pygame import load_pygame  # type: ignore
from src.states.base_state import BaseState
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
import src.sprites


class GameRunning(BaseState):
    def __init__(self) -> None:
        super().__init__()

        # Initialize player inventory
        # self.player_inventory = Inventory()
        # self.inventory_gui = InventoryGUI(self.screen, self.player_inventory)

        # Load initial inventory items from JSON file
        # self.load_inventory_from_json("data/inventory.json")

        self.all_sprites = src.sprites.AllSprites()

        # The start positions will be one of the 4 islands in the corners of the board
        self.setup(player_start_pos="top_left_island")

    def setup(self, player_start_pos):

        self.tmx_map = {
            "map": load_pygame(os.path.join(".", "data", "maps", "100x100_map.tmx"))
        }

        # Islands
        islands = self.tmx_map['map'].get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            src.sprites.Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

        # Objects
        for obj in self.tmx_map['map'].get_layer_by_name("Ships"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                self.player = src.sprites.Player((obj.x, obj.y), self.all_sprites)

    def update(self) -> BaseState:
        return self

    def render(self, screen) -> None:
        """draw sprites to the canvas"""
        screen.fill("#000000")
        self.all_sprites.update()
        self.all_sprites.draw(self.player.rect.center, self.player.player_preview, self.player.player_preview_rect)

        pygame.display.update()

    def handle_events(self) -> None:
        """get events like keypress or mouse clicks"""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_i:  # Toggle inventory with "I" key
                        # TODO : use a paused state to access inventory
                        pass
                        # self.toggle_inventory()
