#from matplotlib import pyplot as plt
#from adjustText import adjust_text
#import numpy as np
from sklearn.manifold import MDS
import tabulate 

# Multidimensional Scaling of weighted distance matrix -> 2D graph 
def MDSGraph(matrix):
    distMatrix = matrix
    mds = MDS(dissimilarity='precomputed', random_state=0)
    X = mds.fit_transform(distMatrix)
    return X

# Constant time: 0(1)
# Function to take minutes and turn into human readable time. 
def TimeFormatter(time):
    hours = int(time / 60)
    minutes = int(time) % 60
    if minutes < 10:
        if minutes == 0:
            minutes = '00'
        else:
            minutes = '0' + str(minutes)
    return (str(hours) + ":" + str(minutes) + ' AM')

# Delivering package function: returns packages table
# Quadratic Time Complexity O(n**2)
def deliverPackages(packageMap, time, tReturn):

    tabledata = []
    cheaders = ['PID', 'Address', 'Deadline', 'City', 'Zip', 'Weight', 'Status']
    timer = None

    # Checking if time variable is a string
    # If a string its user input if not its the program
    # Setting statuses of packages based on time for clean output
    if isinstance(time, str):
        x = [6, 25, 28, 32]
        ix = [4, 6, 17, 24, 25, 26, 28, 31, 32, 29]
        hours = int(time[0]+time[1]) * 60
        minutes = int(time[2]+time[3])
        timer = hours + minutes
        if timer < 620:
            p = packageMap.get(9)
            p.setAddress('300 State St')
        for i in range(1, 41):
            p = packageMap.get(i)
            if i in ix:
                p.setStatus('At the Hub')
            else: 
                p.setStatus("On {}".format(p.getTruckName()))
            if i in x:
                p.setStatus('Delayed on Flight until 9:05 AM')
        if int(tReturn) <= timer:
            ix = [4, 6, 9, 17, 24, 25, 26, 28, 31, 32, 29]
            for i in ix:
                p = packageMap.get(i)
                p.setStatus('On Truck 3')
        elif 545 <= timer:
            ix = [6, 25, 28, 32]
            for i in ix:
                p = packageMap.get(i)
                p.setStatus('At the Hub')
    else:
        timer = int(time)

    st = 480
    
    # Delivering packages and changing statuses based on time
    while st <= timer: 
        for i in range(1, 41):
            p = packageMap.get(i)
            if int(p.getTimeDelivered()) == st:
                p.setStatus("Delivered Package: {}".format(TimeFormatter(p.getTimeDelivered())))
        st += 1

    # Grabbing data for every package 
    for i in range(1, 41):
        p = packageMap.get(i)
        tabledata.append([p.getPID(), p.getAddress(), p.getDeadline(), p.getCity(), p.getZip(), p.getWeight(), p.getStatus()])

    # Using tabulate to print clean table format of data
    print(tabulate.tabulate(tabledata, headers=cheaders))

#def vzroute(route1, route2, route3, addresses1, addresses2, addresses3): 

#    x1, x2, x3 = [], [], []
#    y1, y2, y3 = [], [], []

#    for p in route1:
#        x1.append(p[0])
#        y1.append(p[1])
#    for p in route2:
#        x2.append(p[0])
#        y2.append(p[1])
#    for p in route3:
#        x3.append(p[0])
#        y3.append(p[1])
    
#    ###############################
#    # linear time complexity o(n) #
#    ###############################

#    # visualize return to start address
#    x1.append(x1[0])
#    y1.append(y1[0])
#    x2.append(x2[0])
#    y2.append(y2[0])
#    x3.append(x3[0])
#    y3.append(y3[0])

#    plt.axes().set(facecolor = "lightgrey")
#    plt.title("wgups routes truck routes")
#    plt.xlabel("miles")
#    plt.ylabel("miles")
    
#    plt.scatter(x1, y1, color='y', marker='o')
#    plt.plot(x1, y1, linestyle="-", color='b', label="truck-1 route")
#    plt.scatter(x2, y2, color='y', marker='o')
#    plt.plot(x2, y2, linestyle="-", color='y', label="truck-2 route")
#    plt.scatter(x3, y3, color='y', marker='o')
#    plt.plot(x3, y3, linestyle="-", color='r', label="truck-3 route")

#    plt.legend()
#    labels1 = [plt.text(np.array(route1)[i, 0], np.array(route1)[i, 1],addresses1[i], ha='center', va='center', fontsize=5, weight='bold')for i in range(len(addresses1))]
#    labels2 = [plt.text(np.array(route2)[i, 0], np.array(route2)[i, 1],addresses2[i], ha='center', va='center', fontsize=5, weight='bold')for i in range(len(addresses2))]
#    labels3 = [plt.text(np.array(route3)[i, 0], np.array(route3)[i, 1],addresses3[i], ha='center', va='center', fontsize=5, weight='bold')for i in range(len(addresses3))]
    
#    adjust_text(labels1)
#    adjust_text(labels2)
#    adjust_text(labels3)

#    fig = plt.gcf()
#    fig.canvas.manager.set_window_title('wgups genetic algorithm route optomization visualiztion')
#    plt.show()



