from strategy.payment.paymentStrategy import PaymentStrategy

class CreditCard(PaymentStrategy):
    def pay(self, customer, price):
        print("\nRedirecting user to Credit Card payment portal...")
        print("\nTotal Amount = ${price}")
        return 