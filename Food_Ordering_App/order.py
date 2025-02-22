from typing import List
from location import LOCATION
from customer import Customer
from delivery_agent import DeliveryAgent
from restaurant import Restaurant
from status import STATUS

class Order:
    def __init__(self, order_id, customer: Customer, deliveryAgent: DeliveryAgent, 
                restaurant: Restaurant, price: float, paymentStrategy, deliveryLocation: LOCATION,
                items: List[List]):
        
        self.order_id = order_id
        self.customer = customer
        self.deliveryAgent = deliveryAgent
        self.restaurant = restaurant
        self.price = price
        self.deliveryLocation = deliveryLocation
        self.items = items
        
        self.paymentStrategy = paymentStrategy.name

        self.status = STATUS.PENDING

    def printOrderDetails(self):
        print(f'\nOrder Details:\n{self.customer.getName()} ordered {self.items} from {self.restaurant.getName()}.')
        print(f'STATUS: {self.status}')
        print(f'Delivered by: {self.deliveryAgent.getName()}')
        print(f'Total price = ${self.price}')
        print(f'Payment Method: {self.paymentStrategy}')
        print('\n\nThanks for ordering with us!')

    def setStatus(self,status):
        self.status = status
        