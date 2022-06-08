# Class to manipulate and store package data. #
# all function time complexity: Constant O(1) #
class Packages(object):

    # Init for packages class 
    def __init__(self, PID, address, city, zip, deadline, weight, notes):
        self.PID = int(PID) 
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = None
        self.truck = None
        self.timeDelivered = 0

    # Get functions
    def getPID(self):
        return self.PID
    def getAddress(self):
        return self.address
    def getDeadline(self):
        return self.deadline
    def getCity(self):
        return self.city
    def getZip(self):
        return self.zip
    def getWeight(self):
        return self.weight
    def getStatus(self):
        return self.status
    def getNotes(self):
        return self.notes
    def getTimeDelivered(self):
        return self.timeDelivered
    def getTruckName(self):
        return self.truck

    # Set functions
    def setAddress(self, newAddress):
        self.address = newAddress
    def setDeadline(self, newDeadline):
        self.deadline = newDeadline
    def setCity(self, newCity):
        self.city = newCity
    def setZip(self, newZip):
        self.zip = newZip
    def setWeight(self, newWeight):
        self.weight = newWeight
    def setStatus(self, newstatus):
        self.status = newstatus
    def setNotes(self, newNotes):
        self.notes = newNotes
    def setTimeDelivered (self, time):
        self.timeDelivered = time
    def setTruck(self, truck):
        self.truck = truck
