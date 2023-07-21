from __future__ import annotations
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def process(self) -> None:
        pass


class ConcreteStrategyA(Strategy):
    def process(self) -> None:
        print("This is process from Strategy A")

class ConcreteStrategyB(Strategy):
    def process(self) -> None:
        print("This is process from Strategy B")

class ConcreteStrategyC(Strategy):
    def process(self) -> None:
        print("This is process from Strategy C")