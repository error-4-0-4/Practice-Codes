# from time import time


# def dfs(node, parent, visited, graph):
#     visited[node] = True
#     for nbr in graph[node]:
#         if visited[nbr] is not True:
#             dfs(nbr, node, visited,graph)
#         elif nbr != parent:
#             print(node, "-->", nbr)

# def print_backedges(edges, num_vertices, num_edges):
#     graph= dict()
#     for i in range (num_vertices):
#         graph[i] = []
#     for edge in edges:
#         u,v = edge[0], edge[1]
#         graph[u].append(v)
#         graph[v].append(u)
#     visited =[False]* num_vertices
#     dfs(0, -1, visited,graph)

# if __name__ == '__main__':
#     num_vertices = int(input())
#     num_edges = int(input())
#     edges=[]

#     for i in range (num_edges):
#         u, v = tuple(map(int, input().split()))
#         edges.append([u, v])

#     print_backedges(edges, num_vertices, num_edges)

# from termios import VT0


# def dfs(node, parent):
#     visited[node] = True
#     discovered[node]=time
#     lowest[node]= time
#     time+=1
#     for nbr in graph[node]:
#         if visited[nbr] is not True:
#             dfs(nbr, node)
#         elif nbr != parent:
#             lowest[]

# num_vertices=int(input())
# num_edges=int(input())

# edges=[]
# for i in range (num_edges):
#     u,v = tuple(map(int, input().split()))
#     edges.append([u,v])

# graph=dict()

# time=1

# for i in range (num_vertices):
    
def dfs(node, parent, vis, dis, low, graph, ap, timer):
    vis[node]=True
    dis[node]= timer
    low[node]= timer
    timer+=1

    for nbr in graph[node]:
        if nbr == parent:
            continue
        elif vis[nbr] is not True:
            dfs(nbr, node, vis, dis, low, graph, ap, timer)
            low[node] = min(low[node], low[nbr])

            if low[nbr]>= dis[node] and parent!= -1:
                ap.add(node)
            child+=1
        else:
            low[node]= min(low[node], dis[nbr])
    if child>=2 and parent==-1:
        ap.add(node)

def find_articulation_points(edges, vertices):
    visited =[False]*vertices
    discovery_time = [0]*vertices
    lowest_time = [0]*vertices

    articulation_points= set()
    graph= {}
    timer=0

    for i in range (vertices):
        graph[i]=[]

    for edge in edges:
        u,v= edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)

    for node in range (vertices):
        if visited[node] is not True:
            dfs(node, -1, visited, discovery_time, lowest_time, graph, articulation_points, timer)
if __name__ =='__main__':
    edges=[[0,1], [0,2], [1,2], [1,3], [3,4], [3,6], [4,5], [5,6]]
    vertices=7

    ans=find_articulation_points(edges, vertices)
    print(ans)