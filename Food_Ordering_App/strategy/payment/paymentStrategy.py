from abc import ABC, abstractmethod
from customer import Customer

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, customer: Customer, price: float):
        pass