""" custom sprites classes """
import pygame


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
