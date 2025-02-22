from customer import Customer

class CustomerManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CustomerManager, cls).__new__(cls)
            cls.__instance.customers = {}  
        return cls.__instance
        
    def addCustomers(self, customer: Customer):
        self.customers[customer.id] = customer

    def printCustomers(self):
        for id, customer in self.customers.items():
            customer.getDetails()

    def getCustomerDetails(self,id) -> Customer:
        return self.customers[id]
