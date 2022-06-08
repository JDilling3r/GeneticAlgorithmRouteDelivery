################################################
## Author:      Johnathan C. Benge            ##
## StudentID:   001386358                     ##
## Date:        April 2022                    ##
################################################

import geneticalgorithm as ga
import datareader as dr
import hashmap as hm
import visualization as vz
import packages as pk
import deliverytruck as dt

def Main():

    # Initializing three instances of the Truck class, one for each truck.
    truck1, truck2, truck3 = dt.Truck("Truck 1"), dt.Truck("Truck 2"), dt.Truck("Truck 3")

    # Initializing 3 instances of HashMaps:
    # One holding package data, one holding distance matrix for each address, and one to hold XY coordinates based on the datance matrix
    # HashMap sizes: 40, 54, 27
    packageMap, matrixMap, pointsMap  = hm.HashMap(40), hm.HashMap(54), hm.HashMap(27)

    # Ingesting data from CSVs with "datareader.py" and adding distances, addresses and package data to arrays
    distanceMatrix, addressList = dr.DistanceMatrixUpload(".\\WGUPS_DistanceTable.csv")
    packageData = dr.PackageDataUpload(".\\WGUPS_Packages.csv")

    # Using Multidimensional Scaling to create proportional 2D graph from distanceMatrix
    # Euclidean Distance creates proportional XY coordinates from spacing between points
    # calculated from the Cartesian coordinates of the points using the Pythagorean theorem
    # Linear Time O(n): where n is each address
    points = vz.MDSGraph(distanceMatrix)

    # Adding packageData ingested from WGUPS_Packages.csv to packageMap HashMap: Linear O(n) where n is packages
    # HashMap Key: Package ID
    for i in range(len(packageData)):
        p = packageData[i] 
        packageMap.update(int(p[0]), pk.Packages(int(p[0]), p[1], p[2], p[4], p[5], int(p[6]), p[7]))

    # Adding XY coordinates 'points' to HashMap - pointsMap. Key: address name
    # matrix map holds references to key:address -> index number  and Key: index -> specific address Distance array
    # This allows for Costant O(1) lookup time, but doubles the space needed (addresses/stops * 2)
    for i in range(len(points)):
        pointsMap.update(addressList[i], ga.Points(points[i], addressList[i]))
        matrixMap.update(addressList[i], int(i))
        matrixMap.update(int(i), distanceMatrix[i])

    # DeliveryTruck.py Truck loader function: virtually loading each truck respectively
    # Operates at Constant O(1)
    dt.TruckLoader(packageMap, truck1, truck2, truck3)

    # Initializing each Truck route array with starting point as the 'HUB' 
    route1, route2, route3 = [pointsMap.get('HUB')], [pointsMap.get('HUB')], [pointsMap.get('HUB')]

    #############################################################################
    #   Population size of 50, 20% elitism, 1% mutation rate, 201 generations   #
    #############################################################################
    # Genetic Algorithm Function                                                #
    # Utilizing all working parts to use psuedo evolution for optimizaiton.     #
    # virtualEvolution Function: Cubic Time O(n**3)                             #
    # Cubic time seems bad: numGens is not likely to exceed 1k (statically set) #
    #############################################################################  

    # Adding each 2D graph point to route array for each truck. 
    for p in truck1.getPoints():
            route1.append(pointsMap.get(p))
    for p in truck2.getPoints():
            route2.append(pointsMap.get(p))
    for p in truck3.getPoints():
            route3.append(pointsMap.get(p))

    # Utilizing the Genetic Algorithm to optomize truck route: Code found in geneticalgorithm.py
    print("Using Genetic Algorithm to Optomize Route for Truck 1 \n")
    t1route, t1addresses = ga.virtualEvolution(route1, 50, 10, 0.01, 201)
    print("\nUsing Genetic Algorithm to Optomize Route for Truck 2 \n")
    t2route, t2addresses = ga.virtualEvolution(route2, 50, 10, 0.01, 201)
    print("\nUsing Genetic Algorithm to Optomize Route for Truck 3 \n")
    t3route, t3addresses = ga.virtualEvolution(route3, 50, 10, 0.01, 201)

    # Odering routes for trucks # Linear O(n)  #
    dt.orderRoute(matrixMap, t1addresses, truck1)
    dt.orderRoute(matrixMap, t2addresses, truck2)
    dt.orderRoute(matrixMap, t3addresses, truck3)

    # Driver #1 and #2 Driving truck1 and truck2 delivering packages 
    truck1.deliverPackages()
    truck2.deliverPackages()

    # Driver #1 returns and delivers packages on truck3 
    truck3.setTime(truck1.getTime())
    truck3.deliverPackages()

    # If package #9 is delivered too quickly, the route is reversed 
    # If it is in the middle or later, it is always delivered on the correct time
    p = packageMap.get(9)
    if p.getTimeDelivered() < 620:
        truck3.distance = 0.0
        truck3.orderedMileage.append(0.0)
        truck3.setOrderedMiles(list(reversed(truck3.orderedMileage)))
        truck3.setOrderedRoute(list(reversed(truck3.orderedRoute)))
        truck3.setTime(truck1.getTime())
        truck3.deliverPackages()

    # Setting all packages delivered and trucks back at hub time
    finTime = max(truck1.getTime(), truck2.getTime(), truck3.getTime())
    # Setting time for first truck returning 
    tReturn = min(truck1.getTime(), truck2.getTime(), truck3.getTime())

    # Output for all delivered packages
    print("\n\n")
    vz.deliverPackages(packageMap, finTime, tReturn)
    totalMileage = truck1.getDistance() + truck2.getDistance() + truck3.getDistance()
    print("_________________________________________________")
    print("All trucks returned to Hub at:", (vz.TimeFormatter(truck3.getTime())))
    print("Truck 1 total Mileage:", round(truck1.getDistance(), 2), "miles")
    print("Truck 2 total Mileage:", round(truck2.getDistance(), 2), "miles")
    print("Truck 3 total Mileage:", round(truck3.getDistance(), 2), "miles")
    print("Total Mileage after returning to HUB: ", round(totalMileage, 2), "miles")
    print("All Packages delivered on-time to correct Address")
    print("_________________________________________________")

    #print("\n\nClose Visualization for query abilities...")
    #vz.vzroute(t1route, t2route, t3route, t1addresses, t2addresses, t3addresses)

    # Query Function for console output
    while(True):
        print("\n\n")
        userin = input("\nEnter time to view packages status (EX: 0845) or type exit \n")
        if userin == 'exit':
            break
        else:
            print("\n\n\n")
            vz.deliverPackages(packageMap, userin, truck2.getTime())

Main()