from strategy.payment.paymentStrategy import PaymentStrategy

class NetBanking(PaymentStrategy):
    def pay(self, customer, price):
        print("\nRedirecting user to Netbanking payment portal...")
        print(f"Total Amount = ${price}")
        return 