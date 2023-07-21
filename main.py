
from strategy import Strategy, ConcreteStrategyA, ConcreteStrategyB, ConcreteStrategyC
from context import Context



if __name__ == "__main__":

    context = Context(ConcreteStrategyA())
    context.processStrategy()
    print(context.strategy)

    context.strategy = ConcreteStrategyB()
    context.processStrategy()
    print(context.strategy)

    context.strategy = ConcreteStrategyC()
    context.processStrategy()
    print(context.strategy)


    