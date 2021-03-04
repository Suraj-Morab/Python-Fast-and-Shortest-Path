from itertools import permutations

# Inputs given for this assignment
# The input with format cityA to cityB = distance
CityToCity = """Mysore to Mandya = 66
Mysore to Chennapatna = 28
Mysore to Nanjangud = 60
Mysore to Bandipur = 34
Mysore to Nagarhole = 34
Mysore to Somnathpur = 3
Mysore to Bylakuppe = 108
Mandya to Chennapatna = 22
Mandya to Nanjangud = 12
Mandya to Bandipur = 91
Mandya to Nagarhole = 121
Mandya to Somnathpur = 111
Mandya to Bylakuppe = 71
Chennapatna to Nanjangud = 39
Chennapatna to Bandipur = 113
Chennapatna to Nagarhole = 130
Chennapatna to Somnathpur = 35
Chennapatna to Bylakuppe = 40
Nanjangud to Bandipur = 63
Nanjangud to Nagarhole = 21
Nanjangud to Somnathpur = 57
Nanjangud to Bylakuppe = 83
Bandipur to Nagarhole = 9
Bandipur to Somnathpur = 50
Bandipur to Bylakuppe = 60
Nagarhole to Somnathpur = 27
Nagarhole to Bylakuppe = 81
Somnathpur to Bylakuppe = 90"""

#list of cities
places=list({ line.split(' = ')[0].split(' to ')[0] for line in CityToCity.split('\n')} | { line.split(' = ')[0].split(' to ')[1] for line in CityToCity.split('\n')})

#dictionary of distances
CityDist = {sub.split(" = ")[0]: int(sub.split(" = ")[1]) for sub in CityToCity.split('\n')}

#get distance from CityDist
def distance(cityA,cityB):
    
    if(cityA + ' to ' + cityB in CityDist):
        return CityDist[cityA + ' to ' + cityB]
    
    elif(cityB + ' to ' + cityA in CityDist):
        return CityDist[cityB + ' to ' + cityA]



def shortestPath(cities):
    
    mindist = -1
    minpath = ''
    
    #get all permutations
    ShortPathSolutn = permutations(cities) 
    for i in list(ShortPathSolutn):
        
        dist = 0
        path=''
        
        for x in range(len(i)-1):
            path = path+i[x]+' => '
            if(x == len(i)-2):
                path = path+i[x+1]
            dist = dist + int(distance(i[x],i[x+1]))
            
        if mindist == -1:
            mindist = dist
            minpath = path
        
        elif (mindist > dist):
            mindist = dist
            minpath = path

        else:
            pass
        
    #print('\n\nAnswer:\n'+minpath,mindist)
    return ('\n**Congratulations** \n\t\t\t City To City Shortest Path:\n\n' + minpath + ' = ' + str(mindist) + '\n\n\t\t\t\t --*The End*--')
print('-' * 80)
print('\n\t\t\t\t --**Assingment**-- \n')
print('-' * 80)
print(CityToCity)
print(shortestPath(places))
print('-' * 80)



