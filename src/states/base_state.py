import pygame
from abc import ABC, abstractmethod


class BaseState(ABC):
    """
    using an abstract class to ensure each state has the right methods
    """
    def __init__(self, GameStateManager) -> None:
        self.GameStateManager = GameStateManager

    @abstractmethod
    def update(self, events): # return self
        # update current state
        # handel events
        # and return current state or another one
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        # render current state on a given surface
        pass
