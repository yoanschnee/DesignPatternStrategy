from strategy import Strategy

class Context():
    """
    The Context defines the interface of interest to the client
    """

    def __init__(self, strategy : Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy : Strategy) -> None:
        self._strategy = strategy

    def processStrategy(self) -> str:
        print("This is a default process")
        self._strategy.process()

