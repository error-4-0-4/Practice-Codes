# import math
# from heapq import *
# def build_graph(v, edges):
#     graph={}

#     for vertex in range (1, v+1):
#         graph[vertex]=[]

#     for edge in edges:
#         graph[edge[0]].append(edge[1])

#     return graph

# def build_cost(v, edges):
#     cost= {}
#     for edge in edges:
#         cost[(edge[0], edge[1])] = edge[2]
#     return cost


# def djikstra(v, edges):
#     src=1
#     graph= build_graph(v, edges)
#     cost=build_cost(v,edges)

#     distance=[math.inf]*(v+1)
#     parent= [-1]* (v+1)
#     visited=[False]*(v+1)

#     min_heap=[]

#     heappush(min_heap, (0,src))
#     distance[src]=0

#     while min_heap:
#         curr_distance, curr_node = heappop(min_heap)
        

#         if visited[curr_node] is False:
#             visited[curr_node]= True

#             for nbr in graph[curr_node]:
#                 if curr_distance+ cost[(curr_node, nbr)]< distance[nbr]:
#                     distance[nbr] =curr_distance + cost[(curr_node, nbr)]
#                     parent[nbr] = curr_node
#                     heappush(min_heap, (distance[nbr], nbr))

#     return distance[1:]

# if __name__=='__main__':
#     edges=[]
#     v, e= tuple(map(int, input().split()))
#     for i in range (e):
#         src, dest, wt = tuple (map(int, input().split()))
#         edges.append([src, dest, wt])

#     print (djikstra(v, edges))


# ------------------------------------------------------
import math
from heapq import *
# def build_graph(v, edges):
#     graph={}

#     for vertex in range (1, v+1):
#         graph[vertex]=[]

#     for edge in edges:
#         graph[edge[0]].append(edge[1])

#     return graph

# def build_cost(v, edges):
#     cost= {}
#     for edge in edges:
#         cost[(edge[0], edge[1])] = edge[2]
#     return cost

def build_graph(v, edges):
    graph =[[-1 for i in range (v+1)] for j in range(v+1)]
    for edge in edges:
        src, dest, wt= edge[0], edge[1], edge[2]
        graph[src][dest] = wt
    return graph


def djikstra(v, edges, src, dest):
    cost_graph= build_graph(v, edges)

    distance=[math.inf]*(v+1)
    parent= [-1]* (v+1)
    visited=[False]*(v+1)

    min_heap=[]

    heappush(min_heap, (0,src))
    distance[src]=0

    while min_heap:
        curr_distance, curr_node = heappop(min_heap)
        if curr_node==dest:
            return curr_distance

        if visited[curr_node] is False:
            visited[curr_node]= True

            for nbr in range(1, v+1):
                if cost_graph[curr_node][nbr] != -1 and curr_distance +cost_graph[curr_node][nbr]< distance[nbr]:
                    distance[nbr] =curr_distance + cost_graph[curr_node][nbr]
                    parent[nbr] = curr_node
                    heappush(min_heap, (distance[nbr], nbr))

    return distance[dest] if curr_distance != math.inf else -1

if __name__=='__main__':
    edges=[]
    v, e= tuple(map(int, input().split()))
    for i in range (e):
        src, dest, wt = tuple (map(int, input().split()))
        edges.append([src, dest, wt])

    print (djikstra(v, edges,3,4))