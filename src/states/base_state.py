"""
Base exemple state
each state shall have an update (that loop throug events)
and and render method (who draw on the given surface).
"""
from abc import ABC, abstractmethod
import pygame


class BaseState(ABC):
    """
    using an abstract class to ensure each state has the right methods
    """
    def __init__(self, game_state_manager) -> None:
        self.game_state_manager = game_state_manager

    @abstractmethod
    def update(self, events): # return self
        """
        update current state
        handel events
        and return current state or another one
        """

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """
        render current state on a given surface
        """
