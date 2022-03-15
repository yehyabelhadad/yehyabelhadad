#from operator import index
from Edge import Edge
#from Node import Node 
#from Colony import Colony

class Graph:
    Edges : list[Edge]
    #Ants : list[Ant]
    #GraphColony : Colony
    def __init__(self):
        self.Edges = list()
        #self.Nodes = list()
    """def __init__(self, Colony: Colony ) :
        self.Edges = list()
        self.GraphColony = Colony"""
    def printNodes(self ):
        for N in self.GraphColony.Ants :
            print(N.Address)

    """def AddNode(self, Ant: Ant ):
        self.Nodes.append(Node)
"""
    def AddEdge(self , Edge ): 
        self.Edges.append(Edge)

    def GetNodesNumber(self) -> int:
        return len(self.GraphColony.Ants)
    def GetEdgesNumber(self) -> int:
        return len(self.Edges)
    
    """def IndexNode(self, Node:Node ) -> int : 
        for node in self.Nodes:
            if node.IpAdress == Node.IpAdress:
                return self.Nodes.index(node)
        return -1
    """

    def IndexEdge(self, Edge : Edge) -> int :
        for edge in self.Edges : 
            if edge == Edge:
                return self.Edges.index(edge)
        return -1
        