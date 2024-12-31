from abc import ABC, abstractmethod


class BaseState(ABC):
    """
    using an abstract class to ensure each state has the right methods
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def handle_events(self) -> None:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self) -> None:
        pass
