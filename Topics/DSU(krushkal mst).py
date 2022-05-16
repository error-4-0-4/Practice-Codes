#return leader parent of the set
def find_set(node, parent):
    if parent[node]== -1:
        return node
    
    return find_set(parent[node], parent)

def union_set(u, v, parent):
    #undirected graph union by rank implementation
    # if u>v:
    #     u,v =v, u 
    leader_p_u = find_set (u, parent)
    leader_p_v = find_set(v, parent)

    if leader_p_u != leader_p_v:
        parent[leader_p_v] = leader_p_u
        # parent[v]=u

def kruskals_mst(vertices, edges):
    edges.sort(key= lambda x: x[2])
    parent= [-1]* vertices
    ans=0
    for edge in edges:
        u=edge[0]
        v = edge[1]
        w= edge[2]

        leader_p_u = find_set (u, parent)
        leader_p_v = find_set(v, parent)

        if leader_p_u != leader_p_v:
            parent[leader_p_v] = leader_p_u
            
if __name__ =='__main__':
    # edges=[[0,1], [1,2], [2,3], [3,4], [4,5], [5,6]]
    edges=[[1,2,1], [1,3,2],[1,4,2], [2,3,2], [2,4,3], [3,4,3]]
    vertices= 7
    parent = [-1] * 7
    for edge in edges:
        union_set(edge[0], edge[1], parent)
    
    print(parent)