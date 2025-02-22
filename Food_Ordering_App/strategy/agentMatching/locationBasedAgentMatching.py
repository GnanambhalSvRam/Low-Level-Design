from strategy.agentMatching.agentMatchingStrategy import AgentMatchingStrategy
from deliveryManager import DeliveryAgentManager

class LocationBasedAgentMatching(AgentMatchingStrategy):
    def getDeliveryAgent(self, metaData):
        #Implement logic to find the available agent near the chosen restaurant
        #for now, return someone
        deliveryManager = DeliveryAgentManager()
        agents = deliveryManager.getDeliveryAgents()
        if agents is None:
            return None
        for agent in agents.values():
            if agent.getAvailability():
                return agent