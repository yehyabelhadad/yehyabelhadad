#from Node import Node
import string
#from Ant import Ant 
class Edge:
    IpSource: string 
    IpDestination : string  
    Prediction : float 
    MessageNumber : int
    Pheromone : float 

    def __init__(self, IpSource , IpDestination , Prediction , MessageNumber , Pheromone ):
        self.IpSource = IpSource 
        self.IpDestination   = IpDestination
        self.Prediction = Prediction 
        self.MessageNumber = MessageNumber
        self.Pheromone = Pheromone

    def print(self):
        print("Ip source : " + self.IpSource.IpAdress)
        print("Ip destination : " + self.IpDestination.IpAdress)
        print("Prediction : " + str(self.Prediction))
        print("Message Exchanged : " + str(self.MessageNumber))
        print("Pheromone: " + str(self.Pheromone))

    def IncrementMessageNumber(self):
        self.MessageNumber += 1
    #Pheromone Update Function 
    def UpdatePheromone(self ,  Evaporation , Trust):
        if self.MessageNumber >0:
            self.Pheromone = (1-Evaporation) * self.Pheromone + (self.Prediction + Trust)/self.MessageNumber

    def UpdatePrediction(self , Prediction):
        self.Prediction = Prediction 

"""    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o , Edge) : 
            return False
        return __o.IpSource == self.IpSource and __o.IpDestination == self.IpDestination
"""