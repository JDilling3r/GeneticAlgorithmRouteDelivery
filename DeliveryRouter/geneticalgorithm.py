######                                                  ######
######   Optomization utilizing the Genetic Algorithm   ######
######                Benge Johnathan C.                ######

import random
import math as m

###############################################
# Instances of graph coordinates.             #
# Class Functions: Time Space Complexity O(1) # 
###############################################

class Points:

    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        # Added to keep track of address names
        self.name = name

    def getDistance(self, nextPoint):
        xPoints = pow(self.coordinates[0] - nextPoint[0], 2)
        yPoints = pow(self.coordinates[1] - nextPoint[1], 2)
        return m.sqrt(xPoints + yPoints);

######################################################
# Instances of routes using given Points.            # 
# Class Functions: Linear Time Space Complexity O(n) #
######################################################

class Route:
    def __init__(self, route):
        self.route = route
        self.mileage = 0.0
        self.fitness = 0.0

    # Calculates and Returns complete mileage for full route.
    def getMileage(self):
        if self.mileage == 0.0 : 
            miles = 0.0
            numStops = len(self.route)
            for i in range(numStops):
                currentPoint = self.route[i]
                nextPoint = None
                if i + 1 < numStops:
                    nextPoint = self.route[i + 1]
                else:
                    nextPoint = self.route[0]
                                            # Function getDistance: Constant Time O(1) 
                betweenPoints = currentPoint.getDistance(nextPoint.coordinates)
                miles += betweenPoints
            # Calculating for return back to first point.
            miles += self.route[-1].getDistance(self.route[0].coordinates)
            self.mileage = miles
        return self.mileage
    
    # Setting "Fitness score" (survival of the fittest function) to inverse of total mileage.
    def getFitness(self):
        if self.fitness == 0.0: 
            self.fitness = (self.getMileage())**-1
        return self.fitness

    # Return array of point coordinates for given route: Linear O(n)
    def getPoints(self):
        pointArray = []
        for point in self.route:
            pointArray.append(point.coordinates)
        return pointArray

    # Return array of point address names: Linear O(n)
    def getPointNames(self):
        pointNames = []
        for point in self.route:
            pointNames.append(point.name)
        return pointNames

###################################################################
# Function to randomly generate popSize number of routes.         #
# Generating the first generation of routes.                      #
# firstGen Function: Quadratic Time O(n**2) Space Complexity O(n) #
###################################################################

def firstGen(popSize, addresses):
    population = []
    for i in range(popSize):
                               # random.sample Function: Linear Time O(n)
        population.append(Route(random.sample(addresses, len(addresses))))
    return (population)

###########################################################################
# Function to sort by least to greatest total mileage (fittest to worst)  #
# Utilizing a bubble sort                                                 #
# Rank Function: Quadratic Time O(n**2)                                   #
###########################################################################

def Rank(population):
    #Bubble Sort
    for i in range(len(population)):
        alreadySorted = True
        for p in range(0, len(population) - i - 1):
            if population[p].getMileage() > population[p + 1].getMileage():
                population[p], population[p + 1] = population[p + 1], population[p]
                alreadySorted = False
        if alreadySorted: 
            break
    #rankedPopulation
    return population

####################################################################
# Function used to mathematically cause 'natural selection.'       #
# The least amount of mileage routes (elites) in a population full #
# of routes are more likeley to carry on to the next generation.   #
# natSelection Function: Quadratic Time O(n**2)                    #
####################################################################

def natSelection(ranked, numElites):
    selected = [] 
    sumFitness = 0.0
    cumSumFitness = []
    for route in ranked:
        sumFitness += route.getFitness()
        cumSumFitness.append(sumFitness)
    for i in range (0, numElites):
        selected.append(ranked[i])
    for i in range(0, (len(ranked) - numElites)):
                       # random.random() Function: Constant Time O(1) (Utilizes Mersenne twister algorithm)
        choose = 100 * random.random()
        for i in range(len(ranked)):
            if choose <= (100 * cumSumFitness[i] / sumFitness):
                selected.append(ranked[i])
                break
    return selected

##############################################################################################
# Crossover function for breeding population to create 1 child from 2 parents.               #
# Function is used as a recombination of two 'parents' 'genetics'                            # 
# mixing and matching point positions in two different routes to create a new route 'child'  #
# breed Function: Linear Time O(n)                                                           #
##############################################################################################

def breed(dParent, mParent):
    child = []
    dad = []
    mom = []
                  # random.random() Function: Constant Time O(1) (Utilizes Mersenne twister algorithm)
    chromosome = [(random.random() * len(dParent.route)),
                (random.random() * len(dParent.route))]
    fChromo = int(min(chromosome[0], chromosome[1]))
    lChromo = int(max(chromosome[0], chromosome[1]))
    for i in range(fChromo, lChromo):
        dad.append(dParent.route[i])
    mom = [item for item in mParent.route if item not in dad]
    child = dad + mom
    return Route(child)

############################################################################
# Function to iterate over entire population and 'breed' selected routes.  #
# reproduce Function: Quadratic Time Space Complexity O(n**2)              #
############################################################################

def reproduce(selected, numElites):
    offspring = []
    poolSize = len(selected) - numElites
           # random.sample Function: Linear Time O(n)
    pool = random.sample(selected, len(selected))
    for i in range(0, numElites):
        offspring.append(selected[i])
    for i in range(0, poolSize):
                # breed Function: Linear Time O(n)
        child = breed(pool[i], pool[len(selected)-i-1])
        offspring.append(child)
    return offspring

########################################################################
# Function used to mutate child routes before being accessed.          #
# This introduces 'random' and slightly mitigates local optima issues. #
# mutate Function: Linear Time Space Complexity O(n)                   #
########################################################################

def mutate(mutatee, mRate):
    for swapped in range(len(mutatee.route)):
        if(random.random() < mRate):
            swap = int(random.random() * len(mutatee.route))
            address1 = mutatee.route[swapped]
            address2 = mutatee.route[swap]
            mutatee.route[swapped] = address2
            mutatee.route[swap] = address1
            mutatee.mileage = 0.0
        else: 
            break
    return mutatee

############################################################################
# Function to iterate over entire population and 'mutate' random routes.   #
# reproduce Function: Quadratic Time Space Complexity O(n**2)              #
############################################################################

def mutateAll(population, mRate):
    mutated = []
    for i in range(len(population)):
                       # mutate Function: Linear Time O(n)
        mutated.append(mutate(population[i], mRate))
    return mutated

#######################################################################################
# Function to create next generation, utilizing all functions above for optimization. #
# nextGen Function: Quadratic Time O(4n**2)                                           #
#######################################################################################

def nextGen(currGen, numElites, mRate):
              # Rank Function: Quadratic Time O(n**2)  
    ranked = Rank(currGen)
              # natSelection Function: Quadratic Time O(n**2)
    selected = natSelection(ranked, numElites)
              # reproduce Function: Quadratic Time O(n**2)
    offspring = reproduce(selected, numElites)
              # reproduce Function: Quadratic Time O(n**2)      
    nextGen = mutateAll(offspring, mRate)
    return nextGen

#############################################################################
# Genetic Algorithm Function                                                #
# Utilizing all working parts to use psuedo evolution for optimizaiton.     #
# virtualEvolution Function: Cubic Time O(n**3)                             #
# Cubic time seems bad: numGens is not likely to exceed 1k (statically set) #
#############################################################################

def virtualEvolution(population, populationSize, numElites, mRate, numGens):

    mileageCheck = [None, None]
    population = firstGen(populationSize, population)

    for i in range(numGens):
                   # nextGen Function: Quadratic Time O(4n**2)  
        population = nextGen(population, numElites, mRate)
        # Linear increase to mutation rate with each generation to mitigate being stuck local optima
        mRate += 0.0001

        if i % 50 == 0:
            print("Generation number ", i, ": ", round(Rank(population)[0].getMileage(), 2), "Miles Driven")

        # Lazy implementation of introducing more randomness to explore other paths different than current optimum. 
        # A better way to implement this would be to add weight to explored routes, where most explored are less likely to move onto next generation and least explored are more likely.
        if (i % 35 == 0):
            mileageCheck[0] = population[0].getMileage()
        elif (i != 1 and i % 35 == 1): 
            mileageCheck[1] = population[0].getMileage()
            if (mileageCheck[0] == mileageCheck[1]):
                population = [population[0]] + firstGen(int(populationSize - 1), population[0].route)

    bestRoute = population[0].getPoints()
    routeByName = population[0].getPointNames()
    return bestRoute, routeByName