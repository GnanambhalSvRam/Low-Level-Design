from abc import ABC, abstractmethod
from location import LOCATION
from metaData import MetaData

class AgentMatchingStrategy:
    @abstractmethod
    def getDeliveryAgent(self, metaData: MetaData):
        pass