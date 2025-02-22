from location import LOCATION

class Customer:
    def __init__(self,userID,name,phone,location):
        self.id = userID
        self.name = name
        self.phone = phone
        self.location = location

    def getDetails(self):
        print(f'\nCustomer\'s Details: ')
        print(f'UserID: {self.id}\nName: {self.name}\nPhone: {self.phone}')

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getLocation(self) -> LOCATION:
        return self.location