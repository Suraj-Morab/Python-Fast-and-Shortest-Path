# Inputs given for this assignment
##Mysore to Mandya =          66
##Mysore to Chennapatna =     28
##Mysore to Nanjangud =       60
##Mysore to Bandipur =        34
##Mysore to Nagarhole =       34
##Mysore to Somnathpur =      3
##Mysore to Bylakuppe =       108
##
##Mandya to Chennapatna =     22
##Mandya to Nanjangud =       12
##Mandya to Bandipur =        91
##Mandya to Nagarhole =       121
##Mandya to Somnathpur =      111
##Mandya to Bylakuppe =       71
##
##Chennapatna to Nanjangud =  39
##Chennapatna to Bandipur =   113
##Chennapatna to Nagarhole =  130
##Chennapatna to Somnathpur = 35
##Chennapatna to Bylakuppe =  40
##
##Nanjangud to Bandipur =     63
##Nanjangud to Nagarhole =    21
##Nanjangud to Somnathpur =   57
##Nanjangud to Bylakuppe =    83
##
##Bandipur to Nagarhole =     9
##Bandipur to Somnathpur =    50
##Bandipur to Bylakuppe =     60
##
##Nagarhole to Somnathpur =   27
##Nagarhole to Bylakuppe =    81
##
##Somnathpur to Bylakuppe =   90


# single source shortest 
# The program is for adjacency matrix representation of the Travel 
  
from collections import defaultdict 
  
#Class to represent a Travel 
class Travel: 
  
    # A utility function to find the point with minimum dist value  
    # from the set of vertices still in queue 

    def minDistance(self,dist,queue): 

        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist List,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
  
    # Function to print shortest path 
    # from source to j 
    # using origin array 
    def shorestPath(self, origin, j): 
          
        #Base Case : If j is source 
        if origin[j] == -1 :  
            print(j,) 
            return
        self.shorestPath(origin , origin[j]) 
        print(j,) 
          
  
    # A utility function to print 
    # the constructed distance List 
    def ChartTable(self, dist, origin):
        cityList = ['Mysore', 'Mandya','Chennapatna','Nanjangud','Bandipur','Nagarhole','Somnathpur','Bylakuppe']
        
        # This is src means source,you can not change your source
        startPoint = str(input("Enter Your Source as Mysore only: \n(because this is Single Source Shortest Path, \n if you want to change the source go to \n Tourist(tour,0) and change integer value): "))
        src = startPoint 
        print("Path \t\t\t Journey \t\t\t Distance from Source")
        for i in range(0, len(dist)) or cityList[i] < 8:
            print("\n \t\t {} ---> {} --> {} \t\t\t {} ".format(src, i, cityList[i], dist[i])),
            self.shorestPath(origin,i)
  
    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''
    def Tourist(self, tour, src): 
  
        row = len(tour) 
        col = len(tour[0]) 
  
        # The output List. dist[i] will hold 
        # the shortest distance from src to i 
        # Initialize all distances as Infinite  
        dist = [float("Inf")] * row 
  
        # Orign List to store  
        # shortest path tree 
        origin = [-1] * row 
  
        # Distance of source point  
        # from itself is always 0 

        dist[src] = 0
      
        # Add all points in queue 
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        #Find shortest path for all points 
        while queue: 
  
            # Pick the minimum dist vertex  
            # from the set of points still in queue 
            u = self.minDistance(dist,queue)  
  
            # remove min element      
            queue.remove(u) 
  
            # Update dist value and parent  
            # index of the adjacent points of 
            # the picked vertex. Consider only  
            # those points which are still in queue 
            for i in range(col): 
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if tour[u][i] and i in queue: 
                    if dist[u] + tour[u][i] < dist[i]: 
                        dist[i] = dist[u] + tour[u][i] 
                        origin[i] = u 
  
  
        # print the constructed distance List 
        self.ChartTable(dist,origin) 

  
Res= Travel()
  
tour = [[0,66,28,60,34,34,3,108],
        [66,0,22,12,91,121,111,71],
        [28,22,0,39,113,130,35,40],
        [60,12,39,0,63,21,57,83],
        [34,91,113,63,0,9,50,60],
        [34,121,130,21,9,0,27,81],
        [3,111,35,57,50,27,0,90],
        [108,71,40,83,60,81,90,0]]
 
# Print the solution
# change the dist[src] you will get different paths
Res.Tourist(tour,0)
  
# This code is for finding shorest path and distance
# Technical Assignment Hence Proved. if any mistake or an error occured please let me know so I can Improve my skills.
# Thanks for assigining the assignment.
# Suraj N Morab
# PH No : 7406800042
