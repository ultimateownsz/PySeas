""" custom sprites classes """
import pygame
from src.settings import TILE_SIZE


class Player:
    """ move tile by tile """
    def __init__(self):
        # TODO: replace with actual images
        self.image = pygame.Surface(size=(TILE_SIZE, TILE_SIZE))
        self.image.fill('#ff0000')

        self.rect: pygame.Rect = self.image.get_rect()

    def update(self) -> None:
        """ move the player """

    def render(self, surface: pygame.Surface) -> None:
        """ blit player image to a given surface """
        surface.blit(source=self.image, dest=self.rect)


class Tile(pygame.sprite.Sprite):
    """ Handle tiles for the map """
    def __init__(self,
        *groups: pygame.sprite.Group,
        pos: tuple[float, float],
        surf: pygame.Surface,
        name: str | None = None
    ) -> None:
        super().__init__(*groups)

        self.pos = pos
        self.surf = surf
        self.name = name

        self.image: pygame.Surface = self.surf
        self.rect: pygame.FRect = self.image.get_frect(topleft=self.pos)


    def draw(self, display_surface: pygame.Surface, offset: tuple[float, float]=(0, 0)) -> None:
        """Could be useful for a camera?"""
        offset_rect = self.rect.move(offset)
        display_surface.blit(self.image, offset_rect)
