import random
from Colony import Colony 
from TestController import Controller
from Edge import Edge

HostList = ["H1","H2","H3","H4","H5"]
TestController = Controller("Test11.csv")
for i in range(10000):
    Source = random.choice(HostList)
    Destination = random.choice(HostList)
    while Source == Destination : 
        Destination = random.choice(HostList)
    RandomPrediction = random.randint(0,100)/100
    print("Source = " + Source + " Destination = " + Destination + " Random Prediction  : " + str(RandomPrediction))
    TestController.HandleMessage(Source,Destination, RandomPrediction)

"""E = Edge("H1","H2",0,0,0)
A = Edge("H1","H2",0,0,0)
C= Colony(0.5,0.5,0.1)
C.AddAnt("H1")
C.AddAnt("H2")
C.AddAnt("H3")
C.AddAnt("H4")
for i in range(100):
    print("test"+str(i)+":")
    Link = C.FindEdge("H1","H2")
    print("Edge Found: "+ Link.IpSource + " To: "+ Link.IpDestination)
"""    

"""
TestController = Controller()
for i in range(100):
    for j in range(5):
        randomPrediction = random.randint(0,100)/100
        H = random.randint(0,100)
        if H > 5: 
            randomDestination = random.randint(0,5)
            while randomDestination != j :
                randomDestination = random.randint(0,5)
            SourceHost = "H"+str(j)
            DestinationHost = "H"+str(randomDestination)
            print("Handle Message "+ str(i)+"  from : " + SourceHost + " To : " + DestinationHost + " Random Prediction: " + str(randomPrediction ))
            TestController.HandleMessage(SourceHost,DestinationHost,randomPrediction)





        
"""