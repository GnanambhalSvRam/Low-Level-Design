from typing import List
class PriceCalculator:

    @staticmethod
    def calculate_price(cart : List[List]):
        total = 0
        for item,quantity,rate in cart:
            total = total + rate * quantity

        return total
    
    def __new__(cls, *args, **kwargs):
        raise TypeError("PriceCalculator class cannot be instantiated.")
