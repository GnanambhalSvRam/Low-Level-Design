from strategy.payment.cashOnDelivery import CashOnDelivery
from strategy.payment.creditCard import CreditCard
from strategy.payment.netBanking import NetBanking
from strategy.payment.paymentStrategy import PaymentStrategy

from strategy.restaurantListing.locationBased import LocationBasedRestaurantsStrategy

from strategy.agentMatching.locationBasedAgentMatching import LocationBasedAgentMatching

from location import LOCATION
from metaData import MetaData
from restaurant import Restaurant
from payment import PAYMENT_MODE

from restaurantManager import RestaurantManager
from deliveryManager import DeliveryAgentManager

class StrategyManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StrategyManager, cls).__new__(cls)
            cls.__instance.restaurantManager = RestaurantManager()
        return cls.__instance
    
    def determineRestaurantStrategy(self, metaData: MetaData): #this function determines the strategy to be used for displaying restaurants
        #assume some decision is being made here:
        DECISION = 1
        if DECISION == 1:
            return LocationBasedRestaurantsStrategy()
        
    def determineAgentMatchingStrategy(self, restaurant: Restaurant):  #this function has the logic to choose the appropriate delivery agent
        DECISION = 1
        if DECISION == 1:
            return LocationBasedAgentMatching()
        if DECISION == 2: #return another AgentMatching Strategy
            return None
        
    def determinePaymentStrategy(self, mode: PAYMENT_MODE) -> PaymentStrategy:
        if mode == PAYMENT_MODE.CASH_ON_DELIVERY:
            return CashOnDelivery()
        if mode == PAYMENT_MODE.CREDIT_CARD:
            return CreditCard()
        if mode == PAYMENT_MODE.NET_BANKING:
            return NetBanking()
        raise ValueError(f"Invalid payment mode: {mode}")
        
