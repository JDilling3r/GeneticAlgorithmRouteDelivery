# Genetic Algorithm with Python: TSP
Data Structures and Algorithms II - C950 - PRFA - NHP2

# Scenario
* The WGUPS needs to determine an efficient route and delivery distribution solution for their daily local deliveries. 
* There are 3 Trucks and 2 Drivers
* There is an average of 40 packages per day
  - Each package has specific criteria and delivery deadlines
* Any self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”) can be used to create the program to deliver packages. 

# Assumptions
* Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
* The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
* There are no collisions.
* Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
* Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
* The delivery and loading times are instantaneous, i.e., no time passes while at delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
* There is up to one special note associated with a package.
* The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
* The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
* The day ends when all 40 packages have been delivered.

# Why I chose the Genetic Algorithm
While other algorithms may have a more efficient worst case time-space complexity, I feel the genetic algorithm is an 'outside of the box' approach to this Multi Travelling Salesman problem. I chose it due to its elusiveness and for the stochastic behavior it employs (rather than pure deterministic optimization). There is an added ability to escape locally optimal solutions. 

# What is the Genetic Algorithm
The genetic algorithm is a heuristic solving algorithm. It borrows characteristics from Charles Darwin's theory of natural evolution. The genetic algorithm yields the best 'individual' from the last 'population' where multiple generations, each containing a population, produce offspring that populate the next. There are crossover functions, mutation functions, and natural selection functions that aid in emulating evolution. 

# What is provided by Western Governors University
An excel spreadsheet containing a weighted distance table. (WGUPS_DistanceTable.xlsx)
![image](https://user-images.githubusercontent.com/39090435/172508281-8c108485-e757-4fab-a118-28ad39136c7c.png)
An excel spreadsheet containing all package data for one day. (WGUPS_Packages.xlsx)
![image](https://user-images.githubusercontent.com/39090435/172508460-76042294-f086-40ea-bda5-3e8430df59b3.png)

# Route Optimization Program and Generated Visualization
<img width="1833" alt="WGUPS Delivery Router 1" src="https://user-images.githubusercontent.com/39090435/172508593-aebeff0c-e55f-495e-90d6-9434907e8b9a.PNG">

