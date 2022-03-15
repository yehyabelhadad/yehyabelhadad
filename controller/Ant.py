import string
from Edge import Edge
class Ant :
    Address : string
    Trust : int
    Alpha : float 
    Beta : float
    Evaporation : float

    def __init__(self, Trust : int, Address: string):
        self.Trust= Trust         
        self.Address = Address

    def SetParameters(self, Alpha, Beta, Evaporation): 
        self.Alpha = Alpha 
        self.Beta = Beta 
        self.Evaporation = Evaporation

    def IncrementTrust(self):
        if self.Trust < 100 : 
            self.Trust+=1
        
    def DecrementTrust(self):
        if self.Trust > -100:
            self.Trust -=1

    def GetTrustLevel(self) -> float:
        return ((100+self.Trust)/2)/100
    
    """def HandleMessage(self, Link : Edge, AntSource : 'Ant') -> bool:
        if self.Address == Link.IpDestination :
            if AntSource.GetTrustLevel()==0 and Link.MessageNumber == 0 and Link.Prediction == 0 and Link.Pheromone == 0:
                return False
            else:
                return True
        return False"""

    def AuthoriseMessage(self, Link :Edge , AntSource :'Ant') -> float: 
        #Formula for decision 
        DecisionParameter = (self.Alpha * Link.Pheromone + self.Beta * (Link.Prediction + AntSource.GetTrustLevel())) / Link.MessageNumber
        print("Ant decision Link : Source = " + Link.IpSource + "  Destination = " + Link.IpDestination)
        print("Decision parameters = " + str(DecisionParameter) ) 
        
        return DecisionParameter
        """if True : 
            return True
        else : 
            return False                """







        