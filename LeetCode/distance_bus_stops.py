def distance_bus_stops(dist,start,dest):
    if start>dest:
        start,dest = dest,start
    return min(sum(dist[start:dest]),sum(dist[:start])+sum(dist[dest:]))

distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 2
print(distance_bus_stops(distance,start,destination))