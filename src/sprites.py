"""custom sprites classes"""

import pygame
from src.settings import TILE_SIZE
from src.GUI.inventory import Inventory


class Player:
    """move tile by tile"""

    def __init__(self):
        # TODO: replace with actual images
        self.image = pygame.Surface(size=(TILE_SIZE, TILE_SIZE))
        self.image.fill("#ff0000")
        self.player_preview = self.image.copy()
        self.player_preview.set_alpha(128)

        self.inventory = Inventory()

        self.rect: pygame.Rect = self.image.get_rect()
        # keep track of the transparent preview of the next move
        self.player_preview_rect = self.rect.copy()
        # this is used to only move once when the mouse is pressed
        self.mouse_have_been_pressed: bool = False

    def update(self) -> None:
        """move the player and show a ghost to preview the move"""

        # gost preview
        mouse_pos = pygame.mouse.get_pos()

        # get the relative pos of the player from the mouse
        # to know on wich axis the player will move
        delta_x = abs(self.rect.centerx - mouse_pos[0])
        delta_y = abs(self.rect.centery - mouse_pos[1])

        #  move the gost on the x axis
        self.player_preview_rect = self.rect.copy()
        if delta_x > delta_y:
            if delta_x < (TILE_SIZE / 2):
                # don't move the gost if the mouse is on the player hitbox
                self.player_preview_rect.x = self.rect.x
            elif mouse_pos[0] > self.rect.centerx:
                # go right
                self.player_preview_rect.x = self.rect.x + TILE_SIZE
            else:
                # go left
                self.player_preview_rect.x = self.rect.x - TILE_SIZE
        # move the gost on the y axis
        else:
            if delta_y < (TILE_SIZE / 2):
                # don't move if the mouse is on the player hitbox
                self.player_preview_rect.y = self.rect.y
            elif mouse_pos[1] > self.rect.centery:
                # go down
                self.player_preview_rect.y = self.rect.y + TILE_SIZE
            else:
                # go up
                self.player_preview_rect.y = self.rect.y - TILE_SIZE

        # move the player
        if not pygame.mouse.get_pressed()[0]:
            self.mouse_have_been_pressed = False
            return None
        if self.mouse_have_been_pressed:
            return None

        self.mouse_have_been_pressed = True

        # move on the x axis
        if delta_x > delta_y:
            if delta_x < (TILE_SIZE / 2):
                # don't move if the mouse is on the player hitbox
                return None
            if mouse_pos[0] > self.rect.centerx:
                # go right
                self.rect.x += TILE_SIZE
            else:
                # go left
                self.rect.x -= TILE_SIZE
        # move on the y axis
        else:
            if delta_y < (TILE_SIZE / 2):
                # don't move if the mouse is on the player hitbox
                return None
            if mouse_pos[1] > self.rect.centery:
                # go down
                self.rect.y += TILE_SIZE
            else:
                # go up
                self.rect.y -= TILE_SIZE

        return None

    def render(self, surface: pygame.Surface) -> None:
        """blit player image  and gost preview to a given surface"""
        surface.blit(source=self.player_preview, dest=self.player_preview_rect)
        surface.blit(source=self.image, dest=self.rect)


class Tile(pygame.sprite.Sprite):
    """Handle tiles for the map"""

    def __init__(
        self,
        *groups: pygame.sprite.Group,
        pos: tuple[float, float],
        surf: pygame.Surface,
        name: str | None = None,
    ) -> None:
        r"""
        Initialize a Tile instance.

        Args:
            *groups (pygame.sprite.Group): One or more sprite groups that this tile will belong to.
            pos (Tuple[float, float]): The top-left position where the tile will be placed on the screen.
            surf (pygame.Surface): The surface (image) that will be drawn for this tile.
            name (Optional[str]): An optional name for the tile.

        Note:
            There is a known typing error related to missing type parameters for the generic type 'Group' in pygame.
            You may see warnings like:
            - src\\sprites.py:107: error: Missing type parameters for generic type 'Group' [type-arg]
            - src\\GUI\\gameloop.py:45: error: Missing type parameters for generic type 'SpriteGroup' [type-arg]

            These errors can be ignored for now, as they are related to type annotations in pygame's codebase.
        """
        super().__init__(*groups)

        self.pos = pos
        self.surf = surf
        self.name = name

        self.image: pygame.Surface = self.surf
        self.rect: pygame.FRect = self.image.get_frect(topleft=self.pos)

    def draw(
        self, display_surface: pygame.Surface, offset: tuple[float, float] = (0, 0)
    ) -> None:
        """Could be useful for a camera?"""
        offset_rect = self.rect.move(offset)
        display_surface.blit(self.image, offset_rect)
