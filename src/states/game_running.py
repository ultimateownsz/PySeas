from src.states.base_state import BaseState


class GameRunning(BaseState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        pass

    def render(self) -> None:
        pass

    def handle_events(self) -> None:
        pass
