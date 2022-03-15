import string
from Ant import Ant
from Graph import Graph 
from Edge import Edge 
class Colony:
    Ants : list[Ant]
    Network : Graph
    Alpha : float 
    Beta : float
    Evaporation : float
    def __init__(self):
        self.Ants = list()
        self.Network  = Graph()
        self.Alpha = 0.5
        self.Beta = 0.5
        self.Evaporation = 0.01

    def __init__(self, Alpha , Beta , Evaporation):
        self.Ants = list()
        self.Network  = Graph()
        self.Alpha = Alpha
        self.Beta = Beta 
        self.Evaporation = Evaporation 

    def AddAnt(self, Ip: string ):
        if not(self.FindAnt(Ip)) : 
            NewAnt = Ant(0,Ip)
            NewAnt.SetParameters(self.Alpha,self.Beta,self.Evaporation)
            self.Ants.append(NewAnt)
            self.DrawEdges(NewAnt)

    def DrawEdges(self, NewAnt: Ant ):
        for CurrentAnt in self.Ants:
            if CurrentAnt.Address != NewAnt.Address:
                NewEdge = Edge(NewAnt.Address,CurrentAnt.Address,0,0,0)
                self.Network.AddEdge(NewEdge)
                NewEdge = Edge(CurrentAnt.Address, NewAnt.Address, 0,0,0)
                self.Network.AddEdge(NewEdge)

    def FindAnt(self, Address: string) -> bool:
        for AntCurrent in self.Ants : 
            if(AntCurrent.Address == Address):
                return True
        return False

    def GetAnt(self, Address: string ) : 
        for AntCurrent in self.Ants : 
            if(AntCurrent.Address == Address):
                return AntCurrent
        return False

    def FindEdge(self, Source, Destination ): 
        for CurrentEdge in self.Network.Edges:
            if (CurrentEdge.IpSource == Source and CurrentEdge.IpDestination==Destination):
                return CurrentEdge
        return -1

    def HandleMessage(self, Source: string , Destination : string) -> bool:
        self.AddAnt(Source)
        self.AddAnt(Destination)
        Link = self.FindEdge(Source,Destination)
        Link.IncrementMessageNumber()
        AntSource  = self.GetAnt(Source)
        #AntDestination = self.GetAnt(Destination)
        if AntSource.GetTrustLevel()==0 and Link.MessageNumber == 0 and Link.Prediction == 0 and Link.Pheromone == 0:
            return False
        else:
            return True

    def AuthoriseMessage(self, Source: string , Destination : string) -> bool :
        Link = self.FindEdge(Source,Destination)
        AntSource  = self.GetAnt(Source)
        AntDestination = self.GetAnt(Destination)
        AntDecision = AntDestination.AuthoriseMessage(Link,AntSource)
        if AntDecision >0.0003 :
            AntSource.IncrementTrust()
        else: 
            AntSource.DecrementTrust()
        Link.UpdatePheromone(self.Evaporation,AntSource.GetTrustLevel())
        return AntDecision
    
    def UpdatePrediction(self,Source: string ,Destination:string ,Prediction: float ): 
        Link = self.FindEdge(Source,Destination)
        if Link != -1:
            Link.UpdatePrediction(Prediction)
            AntSource  = self.GetAnt(Source)
            if Prediction>0.8:
                AntSource.IncrementTrust()
            else:
                AntSource.DecrementTrust()
            Link.UpdatePheromone(self.Evaporation,AntSource.GetTrustLevel())

"""
        if AntDestination.HandleMessage(Edge,AntSource):
            return AntDestination.AuthoriseMessage(Edge, AntSource)
        else:
            return False"""     


"""    def Authorise(self, Source: Node, Destination : Node) -> bool : 
        # based on certain condition in the graph and based on ants decide whether the colony can decide if Source is hostile to the destination and to others 
        return True
"""