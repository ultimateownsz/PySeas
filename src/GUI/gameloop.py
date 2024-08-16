from os.path import join
import sys

# import dataclasses, typechecking
from dataclasses import dataclass, field
from typing import TypeAlias  # added this to try to fix typechecking at line 42
"""
Typealias is used making it clear that SpriteGroup is just an alias for Group.
"""

# import pygame related
import pygame
from pytmx.util_pygame import load_pygame

# added this for typechecking on all_sprites
from pygame.sprite import Group

# import Pygame specific objects, functions and functionality
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
from src.sprites import Player, Tile


@dataclass
class GUI:
    """ Graphial User Interface vertion of the game, using pygame-ce """

    screen_size: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen: pygame.Surface = field(init=False)

    def __post_init__(self):
        """
        Initialize pygame and set up the main display and sprite groups.

        The all_sprites group is a pygame.sprite.Group instance that will
        hold and manage all the sprites used in the game. This allows for
        collective updates and rendering of all sprites.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PySeas")

        self.players: list[Player] = [Player()]
        
        SpriteGroup: TypeAlias = Group
        self.all_sprites: SpriteGroup = Group()

        self.running = True
        self.import_assets()
        self.setup(
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

    def setup(self, tmx_maps, player_start_pos):
        """ create tiles """
        sea = tmx_maps.get_layer_by_name("Sea")
        shallow = tmx_maps.get_layer_by_name("Shallow Sea")
        islands = tmx_maps.get_layer_by_name("Islands")
        for x, y, surface in islands.tiles():
            # print(x * TILE_SIZE, y * TILE_SIZE, surface)
            Tile(
                self.all_sprites,
                pos=(x * TILE_SIZE, y * TILE_SIZE),
                surf=surface,
            )

    def run(self) -> None:
        """ main loop of the game """
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self) -> None:
        """ get events like keypress or mouse clicks """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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

        pygame.display.update()
