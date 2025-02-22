from delivery_agent import DeliveryAgent

class DeliveryAgentManager():
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(DeliveryAgentManager, cls).__new__(cls)
            cls.__instance.agents = {}
        return cls.__instance
    
    def addDeliveryAgent(self, agent:DeliveryAgent):
        self.agents[agent.getDeliveryAgentID()] = agent

    def getDeliveryAgent(self,id) -> DeliveryAgent:
        return self.agents.get(id,None)
    
    def getDeliveryAgents(self):
        return self.agents
    
    def printDeliveryAgents(self):
        for agent in self.agents.values():
            agent.getDetails()

    def printMap(self):
        for key in self.agents:
            print(key)
