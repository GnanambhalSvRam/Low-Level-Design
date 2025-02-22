import location as lc

class DeliveryAgent:
    def __init__(self,userID,name,phone):
        self.id = userID
        self.name = name
        self.phone = phone
        self.isAvailable = True
        self.location = lc.LOCATION(0,0)

    def getDetails(self):
        print(f'\nDelivery Agent\'s Details: ')
        print(f'UserID: {self.id}\nName: {self.name}\nPhone: {self.phone}\nCurrent Location = ({self.location.x},{self.location.y})')

    def setAvailability(self,availability):
        self.isAvailable = availability

    def getAvailability(self):
        return self.isAvailable
    
    def setLocation(self,x,y):
        self.location.x = x
        self.location.y = y
        
    def getDeliveryAgentID(self):
        return self.id
    
    def getName(self):
        return self.name

    