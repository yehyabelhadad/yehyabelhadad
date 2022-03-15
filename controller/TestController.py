import random
import string
from Colony  import Colony 
from CSVLogger import Logger
from Ant import Ant 
class Controller :
    NetColony : Colony
    ControllerLogger : Logger
    def __init__(self,FileName:string):
        self.NetColony = Colony(0.5,0.5,0.01)
        self.ControllerLogger = Logger(FileName)
        self.ControllerLogger.Log("Source ;Destination ;Trust ;MessageNumber ;Pheromone ;Prediction ;Decision; Algorithm\n")

    
    def HandleMessage(self,Source: string , Destination : string , Prediction : float):
        Heuristic = random.randint(0,100)
        ColonyDecision = self.NetColony.HandleMessage(Source,Destination)
        if Heuristic<80:
            if  ColonyDecision: 
                Link = self.NetColony.FindEdge(Source,Destination)
                MessageNumber = Link.MessageNumber
                Pheromone = Link.Pheromone
                AntSource =  self.NetColony.GetAnt(Source)
                Trust =AntSource.GetTrustLevel()
                Decision = self.NetColony.AuthoriseMessage(Source,Destination)
                print("Decision Colony with prediction = " + str(Prediction))
                self.ControllerLogger.Log(Source+";"+Destination+";"+str(Trust)+";"+str(MessageNumber)+";"+str(Pheromone)+";"+str(Prediction)+";"+str(Decision)+";"+"Colony \n")
            else :
                Link = self.NetColony.FindEdge(Source,Destination)
                MessageNumber = Link.MessageNumber
                Pheromone = Link.Pheromone
                AntSource =  self.NetColony.GetAnt(Source)
                Trust = AntSource.GetTrustLevel()
                self.NetColony.UpdatePrediction(Source,Destination,Prediction)
                print("Decision ML with prediction = " + str(Prediction))
                self.ControllerLogger.Log(Source+";"+Destination+";"+str(Trust)+";"+str(MessageNumber)+";"+str(Pheromone)+";"+str(Prediction)+";"+str(0)+";"+"ML \n")
        else :
            #self.NetColony.HandleMessage(Source,Destination)
            self.NetColony.UpdatePrediction(Source,Destination,Prediction)
            print("Decision ML with prediction = " + str(Prediction))
            Link = self.NetColony.FindEdge(Source,Destination)
            MessageNumber = Link.MessageNumber
            Pheromone = Link.Pheromone
            AntSource =  self.NetColony.GetAnt(Source)
            Trust = AntSource.GetTrustLevel()
            self.ControllerLogger.Log(Source+";"+Destination+";"+str(Trust)+";"+str(MessageNumber)+";"+str(Pheromone)+";"+str(Prediction)+";"+str(0)+";"+"ML \n")
    