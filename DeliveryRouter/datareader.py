import argparse
import csv

##########################
# Quadratic Time O(n**2) #
##########################

def PackageDataUpload (packageFile):

    packageData = []

    # Description and Parameters for Code
    parser = argparse.ArgumentParser(description='WGUPS Delivery Truck Route Package Data CSV parser.')
    parser.add_argument("-f", "--file", help="CSV file containing package data in format that follows: packageID, address, city, state, zip, deliveryDeadline, massKilo, specialNotes, status", default="WGUPS_Packages.csv")
    args = parser.parse_args()

    with open(packageFile) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: 
            packageData.append(row + [])
    
    # Return packageData Array
    return packageData
            

def DistanceMatrixUpload (distanceTable):

    # Initializing a 2d array to create a matrix for graph and later calculations
    w, h = 27, 28
    distanceMatrix = [[0 for x in range(w)] for y in range(h)] 
    matrixLength = len(distanceMatrix) - 1

    # Initializing array for storage of addresses to correspond to matrix
    addressList = []

    parser = argparse.ArgumentParser(description='WGUPS Delivery Truck Route Distance Table parser.')
    parser.add_argument("-f", "--file", help="CSV file containing Matrix of distances.", default="WGUPS_DistanceTable.csv")
    args = parser.parse_args()

    # Reading data from distance matrix CSV and inputting into an array 
    with open(distanceTable) as csvfile:
        r = 0
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: 
            c = 0
            for col in row:
                # Collecting only distrance in miles for matrix from csv
                if len(col) > 0 and col[0].isdigit():
                    distanceMatrix[r][c] = float(col)
                    c = c + 1
                # Collecting specific Addresses and stripping '\n(ZIP CODE)' off of string as well as leading empty space
                elif len(col) > 0 and col[0]==' ':
                    col = (col).split("\n")[0].lstrip(" ")
                    addressList.append(col)
            r = r + 1

    # Last row in csv is an empty array - this pops that off 
    distanceMatrix.pop(matrixLength)

    # Filling in empty values with corresponding distance to complete matrix
    for i in range(matrixLength):
        for c in range(matrixLength):
            if distanceMatrix[i][c] == 0:
                distanceMatrix[i][c] = distanceMatrix[c][i]

    # Retrun distance matrix and address list
    return(distanceMatrix, addressList)
