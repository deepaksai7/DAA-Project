import numpy as np
#importing table from csv file to 2d numpy array
distancegraph = np.loadtxt('data.csv', delimiter=',')

#initializing the required variables
speedgraph = np.zeros(shape=(14,14))
timegraph = np.zeros(shape=(14,14))
a=0
a=np.float64(a)
b=9999
b=np.float64(b)

#inserting random numbers in speedgraph
for i in range(0,14):
    for j in range(0,14):
        speedgraph[i][j]=np.random.uniform(low=30, high=55, size=None)
        
#variables used in algorithm

temp=np.zeros(shape=(14))
final_path=np.zeros(shape=(14))
for i in range(len(final_path)):
    final_path[i]=99999
solution=[]



#implementing floyd warshall alorithm
def algorithm(source,destination,graph):
    shortest = np.zeros(shape=(14, 14))
    pathgraph = np.zeros(shape=(14, 14))
    for i in range(0,14):
        for j in range(0,14):
            shortest[i][j]=graph[i][j]

    for i in range(0,14):
        for j in range(0,14):
            if graph[i][j] != b and i != j:
                pathgraph[i][j]=i
            else:
                pathgraph[i][j]=-1

    for k in range(0,14):
        for i in range(0,14):
            for j in range(0,14):
                if shortest[i][j]>shortest[i][k]+shortest[k][j]:
                    shortest[i][j]= shortest[i][k]+shortest[k][j]
                    pathgraph[i][j]=pathgraph[k][j]
    for i in range(0,14):
        temp[i]=pathgraph[source][i]

    final_path[13]=destination
    z=12
    while final_path[z+1] != source:

        final_path[z]=int(temp[int(final_path[z+1])])
        z=z-1
    for i in range(len(final_path)):
        if final_path[i] != 99999:
            solution.append(final_path[i])
    return solution,shortest[source][destination]




#generating time graph
def generate_timegraph(source,destination,factor):
    
    for i in range(len(speedgraph)):
        for j in range(len(speedgraph)):
            speedgraph[i][j]=speedgraph[i][j]+factor
            
    for i in range(len(timegraph)):
        for j in range(len(timegraph)):
            if distancegraph[i][j] != a and distancegraph[i][j] != b:
                timegraph[i][j]= distancegraph[i][j]/speedgraph[i][j]
            else:
                timegraph[i][j]=distancegraph[i][j]
    solution,t=algorithm(source,destination,timegraph)
    return solution,distancegraph,t









