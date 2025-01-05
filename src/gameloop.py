"""
main game loop
structure of the game, using a stack of states
"""


import sys
import pygame

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

# import state for typehint
from src.states.base_state import BaseState
from src.states.game_running import GameRunning


class GameStateManager:
    """
    Initialise pygame
    and the first game state
    """
    def __init__(self) -> None:

        # init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PySeas")

        self.clock = pygame.Clock()
        self.running = True
        self.event: list[pygame.event.Event] = []
        self.states_stack: list[BaseState] = []

        # instanciate the initial state
        self.states_stack.append(GameRunning(self))


    def enter_state(self, state: BaseState) -> None:
        """
        append state to the stack
        """
        self.states_stack.append(state)

    def exit_state(self) -> BaseState:
        """
        pop and return the last state
        """
        return self.states_stack.pop()

    def _handle_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self) -> None:
        """main loop of the game"""
        while self.running:
            self._handle_events()

            # give the pygame events to each states
            # to ensure that pygame.event.get() is only called once per frame
            self.states_stack[-1].update(self.events)

            self.states_stack[-1].render(self.screen)

            # magic value, use a FPS const in settings or delta time
            self.clock.tick(60)
