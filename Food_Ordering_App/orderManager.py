from customerManager import CustomerManager
from deliveryManager import DeliveryAgent
from restaurantManager import RestaurantManager
from strategyManager import StrategyManager

from customer import Customer
from delivery_agent import DeliveryAgent
from restaurant import Restaurant
from order import Order

from status import STATUS
from location import LOCATION
from metaData import MetaData
from priceCalculator import PriceCalculator

from payment import PAYMENT_MODE

from typing import List

class OrderManager:
    __instance = None
    __next_order_id = 0

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(OrderManager, cls).__new__(cls)
            cls.__instance.orders = {}
            cls.__instance.ordersMetaData = {}
            cls.__instance.strategyManager = StrategyManager()
        return cls.__instance
    
    def displayRestaurants(self,deliveryLocation: LOCATION):
        restaurants_strategy = self.strategyManager.determineRestaurantStrategy(deliveryLocation)
        return restaurants_strategy.getRestaurants(deliveryLocation)
    
    def create_order(self, customer: Customer, deliveryLocation: LOCATION, paymentMode: PAYMENT_MODE, restaurant: Restaurant, cart: List[List]):
        metaData = MetaData(customer, deliveryLocation, paymentMode, restaurant, cart)

        agentMatchingStrategy = self.strategyManager.determineAgentMatchingStrategy(metaData)  
        agent = agentMatchingStrategy.getDeliveryAgent(metaData)    
        agent.setAvailability = False

        price = PriceCalculator.calculate_price(cart)
        paymentStrategy = self.strategyManager.determinePaymentStrategy(paymentMode)
        paymentStrategy.pay(customer,price)

        order = Order(self.__next_order_id, customer, agent, restaurant, price, paymentMode, deliveryLocation, cart)
        self.__next_order_id += 1 #this is not thread safe!!!

        return order

