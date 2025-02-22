from restaurant import Restaurant

class RestaurantManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(RestaurantManager, cls).__new__(cls)
            cls.__instance.restaurants = {}  
        return cls.__instance
        
    def addRestaurant(self, restaurant: Restaurant):
        self.restaurants[restaurant.id] = restaurant

    def printRestaurant(self):
        for id, res in self.restaurants.items():
            res.getDetails()

    def getRestaurants(self):
        return self.restaurants
