from restaurantManager import RestaurantManager
from location import LOCATION
from strategy.restaurantListing.displayRestaurantsStrategy import DisplayRestaurantsStrategy


class LocationBasedRestaurantsStrategy(DisplayRestaurantsStrategy):
    def getRestaurants(self, location : LOCATION):
       
        restaurantManager = RestaurantManager()  #gets a list of restaurants based on the location
        return restaurantManager.getRestaurants() #for now, return all the restaurants