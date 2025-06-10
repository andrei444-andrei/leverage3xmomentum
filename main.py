from AlgorithmImports import *
# Импортируешь свои собственные файлы:
from strategy import *
from indicators import *
from execution import *
class MyAlgorithm(QCAlgorithm):

    def Initialize(self):
        # Инициализация алгоритма и стратегии
        self.strategy = MyStrategy(self)
        self.strategy.Initialize()

    def OnData(self, data):
        # Обработка новых данных (делегируется стратегии)
        self.strategy.OnData(data)

    def OnOrderEvent(self, orderEvent):
        # Обработка событий по ордерам (делегируется стратегии)
        self.strategy.OnOrderEvent(orderEvent)
