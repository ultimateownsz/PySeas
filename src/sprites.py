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

        # this is used to only move onec when the mouse is pressed
        self.mouse_have_been_pressed: bool = False

    def update(self) -> None:
        """ move the player """
        if not pygame.mouse.get_pressed()[0]:
            self.mouse_have_been_pressed = False
            return None
        if self.mouse_have_been_pressed:
            return None

        self.mouse_have_been_pressed = True
        mouse_pos = pygame.mouse.get_pos()

        delta_x = abs(self.rect.centerx - mouse_pos[0])
        delta_y = abs(self.rect.centery - mouse_pos[1])

        if delta_x > delta_y:
            # move on the x axis
            if delta_x < (TILE_SIZE / 2):
                # don't move if the mouse is on the player hitbox
                return None
            if mouse_pos[0] > self.rect.centerx:
                # go right
                self.rect.x += TILE_SIZE
            else:
                # go left
                self.rect.x -= TILE_SIZE
        else:
            # move on the y axis
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
