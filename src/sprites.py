from src.settings import pygame
from dataclasses import dataclass


@dataclass
class Sprite(pygame.sprite.Sprite):
    pos: tuple[int | float, int | float]
    surf: pygame.Surface
    groups: tuple[pygame.sprite.Group, ...] | pygame.sprite.Group
    # name: str | None = None

    def __post_init__(self):
        super().__init__(self.groups)
        self.image: pygame.Surface = self.surf
        self.rect: pygame.FRect = self.image.get_frect(topleft=self.pos)

    def draw(self, display_surface, offset=(0, 0)):
        """Could be useful for a camera?"""
        offset_rect = self.rect.move(offset)
        display_surface.blit(self.image, offset_rect)
