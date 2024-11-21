from os.path import join
import sys

# import dataclasses and typchecking
from dataclasses import dataclass, field

# import pygame related
import pygame
from pytmx.util_pygame import load_pygame  # type: ignore

# import Pygame specific objects, functions and functionality
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
import src.sprites

# import inventory related classes
from src.GUI.inventory_gui import InventoryGUI
from src.GUI.inventory import Inventory


@dataclass
class GUI:
    """Graphial User Interface vertion of the game, using pygame-ce"""

    screen_size: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen: pygame.Surface = field(init=False)

    # groups
    # all_sprites: pygame.sprite.Group = field(
    #     init=False, default_factory=pygame.sprite.Group
    # )
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()

    def __post_init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PySeas")

        # Initialize player inventory
        self.player_inventory = Inventory()
        self.inventory_gui = InventoryGUI(self.screen, self.player_inventory)
        
        self.players: list[src.sprites.Player] = [src.sprites.Player()]

        self.running = True
        self.import_assets()
        self.setup(
            tmx_maps=self.tmx_map["map"], player_start_pos="Fort"
        )  # The start positions will be one of the 4 islands in the corners of the board

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
        islands = tmx_maps.get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            # print(x * TILE_SIZE, y * TILE_SIZE, surface)
            src.sprites.Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

    def run(self) -> None:
        """main loop of the game"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self) -> None:
        """get events like keypress or mouse clicks"""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_i: # Toggle inventory with "I" key
                        self.toggle_inventory()

    def toggle_inventory(self):
        """Toggle the inventory overlay."""
        self.inventory_gui.running = not self.inventory_gui.running

        while self.inventory_gui.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    self.inventory_gui.running = False # Close the inventory
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left click
                    self.inventory_gui.handle_mouse_click(event.pos)

            self.inventory_gui.draw()
            pygame.display.flip() # Update the display

    def update(self) -> None:
        """update the player"""
        for player in self.players:
            player.update()

    def render(self) -> None:
        """draw sprites to the canvas"""
        self.screen.fill("#000000")
        self.all_sprites.draw(surface=self.screen)

        # draw players on top of the other sprites
        for player in self.players:
            player.render(surface=self.screen)

        pygame.display.update()
