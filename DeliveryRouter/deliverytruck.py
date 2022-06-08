import packages as ps
import hashmap as hm

#################### #############################
# Linear Time O(n) # Worst case time complexity. #
#################### #############################

class Truck(object):

    def __init__(self, name):
        self.name = name
        self.packageLimit = 16
        self.mph = 18
        self.time = 480
        self.distance = 0
        self.packages = []
        self.orderedMileage = []
        self.orderedRoute = []

    def getName(self):
        return self.name
    def getMPH(self):
        return self.mph
    def getTime(self):
        return self.time
    def getDistance(self):
        return self.distance
    def getPackageLimit(self):
        return self.packageLimit
    def getPackageAmount(self):
        return len(self.packages)
    def getPackages(self):
        return self.packages
    def getPoints(self):
        addresses = [] 
        for p in self.packages:
            addresses.append(p.getAddress())
        return addresses     
    def getDistance(self): 
        return self.distance


    def loadPackage(self, package):
        # adding instances of Packages class to self.packages array
        self.packages.append(package)
    def setTime(self, time):
        self.time = time
    def setRoute(self, stopData):
        self.orderedRoute = stopData
    def setOrderedMiles(self, mileage):
        self.orderedMileage = mileage
    def setOrderedRoute(self, route):
        self.orderedRoute = route
    def deliverPackages(self):
        for i in range(len(self.orderedRoute)):
            stop = self.orderedRoute[i]
            milesto = self.orderedMileage[i]
            timer = (milesto / self.mph) * (60 / 1)
            self.time += timer
            self.distance += milesto
            for p in self.packages:
                if p.getAddress() == stop:
                    p.setTimeDelivered(self.time)

# Get true distance between 2 points (using proportional weighted distances to optomize)
# This operates in constant time: where as index() operates in linear time. 
def getDistance(matrixMap, start, fin):
    return float(matrixMap.get(matrixMap.get(start))[int(matrixMap.get(fin))])

#################### ########################################################
# Linear Time O(n) # Ordering route and setting true mileage between stopss #
#################### ########################################################
def orderRoute(matrixMap, addresses, truck):
    hub = addresses.index('HUB')
    orderedRoute = []
    orderedMileage = [0.0]

    for a in range(hub, len(addresses) + hub):
        if a > hub:
            ix = (a % len(addresses))
            orderedRoute.append(addresses[ix])
        else:
            orderedRoute.append(addresses[a])

    for i in range(len(orderedRoute)):
        if i < (len(orderedRoute) - 1):
            orderedMileage.append(getDistance(matrixMap, orderedRoute[i], orderedRoute[i+1]))
        else: 
            orderedMileage.append(getDistance(matrixMap, orderedRoute[i], orderedRoute[0]))
    orderedRoute.append(orderedRoute[0])

    truck.setOrderedMiles(orderedMileage)
    truck.setRoute(orderedRoute)

def TruckLoader(packages, truck1, truck2, truck3):
    
# With special notes and an algorithm to visualize full optomized routes: *assuming human interaction to physically load trucks*
# Switched from automated loading to manual 
# Lazy loading strategy for showcasing algorithm. 
# Loading based on zip code and visual proximity on plotted graph with special notes in mind. 

    t1 = [packages.get(1), packages.get(2), packages.get(14),  packages.get(22),
          packages.get(15), packages.get(16), packages.get(19), packages.get(20),
          packages.get(21), packages.get(27), packages.get(33), packages.get(34),
          packages.get(35), packages.get(40)]
    t2 = [packages.get(3), packages.get(5), packages.get(8), packages.get(7),
          packages.get(10), packages.get(11), packages.get(12), packages.get(13),
          packages.get(18), packages.get(23), packages.get(29),packages.get(30),
          packages.get(36), packages.get(37), packages.get(38), packages.get(39)]
    t3 = [packages.get(4), packages.get(6), packages.get(17),
          packages.get(24), packages.get(25), packages.get(26), packages.get(28),
          packages.get(31), packages.get(32), packages.get(9)]

    p = packages.get(9)
    p.setAddress('410 S State St')
    pg = [6, 25, 28, 32]

    # Loading Truck 1
    for p in t1:
        truck1.loadPackage(p)
        p.setTruck('Truck 1')
        p.setStatus('On Truck 1: Enroute')
    for p in t2:
        truck2.loadPackage(p)
        p.setTruck('Truck 2')
        p.setStatus('On Truck 2: Enroute')
    for p in t3:
        truck3.loadPackage(p)
        p.setTruck('Truck 3')
        p.setStatus('At the Hub')
    for i in pg:
        p = packages.get(i)
        p.setStatus('Delayed on flight')

