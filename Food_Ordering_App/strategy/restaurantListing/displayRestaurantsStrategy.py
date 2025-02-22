from abc import ABC, abstractmethod
from location import LOCATION

class DisplayRestaurantsStrategy:
    @abstractmethod
    def getRestaurants(self, location: LOCATION):
        pass