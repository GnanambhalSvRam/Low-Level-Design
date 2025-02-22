from customer import Customer
from location import LOCATION
from typing import List

from restaurant import Restaurant

from strategy.payment.paymentStrategy import PaymentStrategy

class MetaData:

    def __init__(self,customer: Customer,location: LOCATION, paymentMethod: PaymentStrategy, restaurant: Restaurant, cart: List):
        self.customer = customer
        self.location = location
        self.paymentMethod = paymentMethod
        self.restaurant = Restaurant
        self.cart = cart
