from os.path import join
import json

# import pygame related
import pygame
from pytmx.util_pygame import load_pygame  # type: ignore

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
import src.sprites

# import states
from src.states.game_running import GameRunning

class GUI:
    """Graphial User Interface vertion of the game, using pygame-ce"""


    def __post_init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PySeas")
        self.clock = pygame.Clock()

        # Initialize player inventory
        self.player_inventory = Inventory()
        self.inventory_gui = InventoryGUI(self.screen, self.player_inventory)

        # Load initial inventory items from JSON file
        self.load_inventory_from_json("data/inventory.json")

        # Players list currently commented out; keeping for potential future use
        # self.players: list[src.sprites.Player] = [src.sprites.Player()]

        self.all_sprites = src.sprites.AllSprites()
        self.running = True
        self.import_assets()
        self.setup(
            tmx_maps=self.tmx_map["map"], player_start_pos="top_left_island"
        )  # The start positions will be one of the 4 islands in the corners of the board

        # instanciate the initial state
        self.state = GameRunning()

    def import_assets(self):
        """load the map"""
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

    def setup(self, tmx_maps, player_start_pos):
        """create tiles"""

        self.tmx_map = {
            "map": load_pygame(join(".", "data", "maps", "100x100_map.tmx"))
        }

        # Islands
        islands = tmx_maps.get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            src.sprites.Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

        # Objects
        for obj in tmx_maps.get_layer_by_name("Ships"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                self.player = src.sprites.Player((obj.x, obj.y), self.all_sprites)

    def toggle_inventory(self):
        """Toggle the inventory overlay."""
        self.inventory_gui.running = not self.inventory_gui.running

        while self.inventory_gui.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    self.inventory_gui.running = False  # Close the inventory
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                ):  # Left click
                    self.inventory_gui.handle_mouse_click(event.pos)
                elif event.type == pygame.MOUSEWHEEL:
                    self.inventory_gui.handle_events(event)

            self.inventory_gui.draw()
            pygame.display.flip()  # Update the display

    def load_inventory_from_json(self, file_path: str):
        """Load initial inventory items from JSON file."""
        try:
            with open(file_path, "r") as f:
                items = json.load(f)
                for item_name, properties in items.items():
                    quantity = properties.get("quantity", 1)  # Default to 1 if missing
                    self.player_inventory.add_item(item_name, quantity)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error: The file at {file_path} does not exist.")


class GameStateManager:
    def __init__(self):

        # init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PySeas")

        self.clock = pygame.Clock()
        self.running = True

        # instanciate the initial state
        self.state = GameRunning()


    def run(self) -> None:
        """main loop of the game"""
        while self.running:
            self.state.handle_events()
            # state.update() return self or a new state
            self.state = self.state.update()
            self.state.render(self.screen)
