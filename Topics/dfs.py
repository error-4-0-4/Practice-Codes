def build_graph(vertices, edges):
    graph={}
    for node in range (vertices):
        graph[node]=[]

    for edge in edges:
        parent, child= edge[0], edge[1]
        graph[parent].append(child)
        graph[child].append(parent)
    return graph

def dfs_recur(node, visited, graph, ans):
    visited[node]=True
    ans.append(node)
    for nbr in graph[node]:
        if visited[nbr] is not True:
            ans= dfs_recur(nbr, visited, graph,ans)
    return ans

def dfs(vertices, edges):
    visited = [False]*vertices
    graph= build_graph(vertices,edges)
    ans=[]
    for node in range(vertices):
        if visited[node] is not True:
            dfs_recur (node, visited, graph, ans)
    # dfs_recur(0, visited, graph, ans)
    return ans

if __name__=='__main__':
    vertices = 7
    edges=[[0,1], [1,2], [2,4], [3,5], [3,6]]
    ans = dfs(vertices, edges)
    print(ans)