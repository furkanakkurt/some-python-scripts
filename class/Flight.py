class Flight:

    __flightOperatingCost = 150

    def __init__(self, flightNo, destination, departure, capacity):
        self.__flightNo = flightNo
        self.__destination = destination
        self.__departure = departure
        self.__capacity = capacity

    def  setCapacity( self, cap):
        if(cap > 0):
            self.__capacity = cap
        
    def  getCapacity(self):
        return self.__capacity
    
    def  setFlightNo( self, num):
        self.__flightNo = num
    
    def  getFlightNo(self):
        return self.__flightNo

    def  setDeparture( self, dep):
        self.__departure = dep
    
    def  getDeparture(self):
        return self.__departure

    def  setDestination( self, dest):
        self.__destination = dest
    
    def  getDestination(self):
        return self.__destination

    def calculateOperatingCost(self):
        return Flight.__flightOperatingCost * self.__capacity

    def __repr__(self):
        return "\nFlight Number: " + self.__flightNo + "\nDeparting From: " + self.__departure + "\nArrival: " + self.__destination + "\nSeats: " + str(self.__capacity) + "\n"

    def __lt__(self, secondFlight):
        return self.__flightNo < secondFlight.__flightNo 
