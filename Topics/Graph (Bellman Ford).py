import math


def bellman_ford (vertices, edges, src):

    distance=[math.inf] *(vertices+1)
    distance[src]=0
    for i in range (vertices-1):
        for edge in edges:
            src, dest, weight =edge[0], edge[1], edge[2] 
            if distance[src]+weight <distance[dest]:
                distance[dest]= distance[src] + weight
    
    is_cycle= False
    for edge in edges:
        src, dest, weight =edge[0], edge[1], edge[2] 
        if distance[src]+weight <distance[dest]:
            is_cycle=True
            break
    if is_cycle:
        return -1
    else:
        return distance[1:]


if __name__ =="__main__":
    # vertices=6
    # edges=[[1,2,6], [1,3,4] , [1,4,5], [2,5,-1], [3,2,-2], [3,5,3], [4,3,-2], [4,6,-1], [5,6,3]]
    vertices=4
    edges=[[1,2,4],[1,3,5], [2,4,7], [3,2,7], [4,3,-15]]   
    print(bellman_ford(vertices, edges,1))