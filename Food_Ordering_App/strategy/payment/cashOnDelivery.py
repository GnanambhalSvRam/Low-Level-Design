from strategy.payment.paymentStrategy import PaymentStrategy

class CashOnDelivery(PaymentStrategy):
    def pay(self, customer, price):
        print("\nPayment Mode: Cash on Delivery.")
        return 