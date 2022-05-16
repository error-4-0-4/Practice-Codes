#Graph Representation Using Adjacency List – I

class Graph:
 
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for i in range(self.vertices)]
 
    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source) # comment this line for directed graph 
 
    def print_graph(self):
        print("Adjacency List of Undirected Graph")
        for i in range(self.vertices):
            print(i, " => ", end = " ")
            for nbr in self.adjacency_list[i]:
                print(nbr, end = " ")
            print()
 
 
if __name__ == '__main__':
     
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.print_graph()