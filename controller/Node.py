from numpy import isin


class Node :
    IpAdress = str 
    def __init__(self, IpAdress):
        self.IpAdress = IpAdress
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,Node):
            return False
        return self.IpAdress==__o.IpAdress