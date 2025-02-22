from location import LOCATION

class Restaurant:
    def __init__(self, id, name, location, menu = []):
        self.id = id
        self.name = name
        self.location = location
        self.menu = menu

    def addToMenu(self,item):
        self.menu.append(item)

    def getName(self):
        return self.name
    
    def getDetails(self):
        print(f'\n{self.name} @ ({self.location.x},{self.location.y}). We serve {self.menu}.')
