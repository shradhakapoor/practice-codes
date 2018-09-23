from collections import defaultdict

# graph representation using adjacency matrix
class Graph_adj_matrix(object):
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjacency_matrix = [[-1] * no_of_vertices for x in range(no_of_vertices)]
        self.vertices_list = [0] * no_of_vertices

        def defaultvalue(): # return value for defaultdict of key is not present
            return -1
        # ex: a->0, b->1, c->2...
        self.vertex_id_to_num_map = defaultdict(defaultvalue)

    def add_vertex( self, vertex_num, vertex_id ):
        if 0 <= vertex_num < self.no_of_vertices:
            self.vertex_id_to_num_map[vertex_id] = vertex_num
            self.vertices_list[vertex_num] = vertex_id

    def add_edge( self, frm, to, cost = 0 ):
        frm_num = self.vertex_id_to_num_map[frm]
        to_num = self.vertex_id_to_num_map[to]
        self.adjacency_matrix[frm_num][to_num] = cost
        self.adjacency_matrix[to_num][frm_num] = cost # for undirected graphs only

    def get_vertices( self ):
        return self.vertices_list

    def get_edges( self ):
        edges = []
        for i in range(self.no_of_vertices):
            for j in range(self.no_of_vertices):
                if self.adjacency_matrix[i][j] != -1:
                    edges.append((self.vertices_list[i], self.vertices_list[j], self.adjacency_matrix[i][j]))

        return edges

    def get_adjacency_matrix( self ):
        return self.adjacency_matrix

class adj_list_vertex(object):
    def __init__(self, id):
        self.id = id

        def defaultvalue():
            return -1
        self.connectedTo = defaultdict(defaultvalue)

    def add_neighbor( self, neighbor, cost ):
        self.connectedTo[neighbor] = cost

    def __str__( self ):
        return str(self.id) + 'connected to' + str([x for x in self.connectedTo])

    def get_connections( self ):
        # return all the id s connected to this vertex
        return self.connectedTo

    def getId( self ):
        return self.id

    def getWeight( self, neighbor ):
        return self.connectedTo[neighbor]

# graph representation using adjacency list
class Graph_adj_list(object):
    def __init__(self):
        def defaultvalue():
            return None
        # key = id , value = vertex node of that id
        self.vertices_list = defaultdict(defaultvalue)
        self.no_of_vertices = 0

    def add_vertex( self, id ):
        self.no_of_vertices += 1
        newVertex = adj_list_vertex(id)
        self.vertices_list[id] = newVertex

    def get_vertex( self, v ):
        if v in self.vertices_list:
            return self.vertices_list[v]
        else:
            return

    def add_edge( self, frm, to, cost =0 ):
        if frm not in self.vertices_list:
            self.add_vertex(frm)
        if to not in self.vertices_list:
            self.add_vertex(to)
        self.vertices_list[frm].add_neighbor(self.vertices_list[to], cost)

    def get_vertices( self ):
        return self.vertices_list.keys()

    def __contains__(self, id):
        return id in self.vertices_list

    def __iter__(self):
        # iter creates an object that can be iterated one at a time
        return iter(self.vertices_list.values())

# create an undirected graph using adjacency matrix

# create an undirected graph using adjacency list

# create a directed acyclic graph

# graph traversal - Depth First Search

# graph traversal - Breadth First Search

# topological sort in directed acyclic graph

# find shortest path in unweighted directed graph (modified BFS)

# find shortest path in weighted directed graph (Dijkstra algorithm)

# find shortest path in weighted directed graph with negative edges (Bellman-Ford algorithm)

# find shortes path in weighted acyclic graph

# find minimum spanning tree in undirected weighted graph - Prim's algorithm
# for unweighted graphs we consider all weights are equal

# find minimum spanning tree in undirected weighted graph - Kruskal's algorithm

# Given a graph as adjacency matrix, check whether graph has simple path from source to destination

# Given a graph as adjacency matrix, count all simple paths from source to destination in graph

# find shortest path between every pair of vertices in graph. Assume graph doesn't have negative edges
# can be solved using n applications of Dijkstra

# find shortest path between every pair of vertices in graph. Assume graph has negative edges
# Floyd-Warshall algorithm

# find the cut-vertex in an undirected graph (DFS application)
# Cut-Vertex is a vertex if removed then graph splits into two disconnected components

# find cut-edge in an undirected graph (DFS application)
# cut-edge is an edge if removed then graph splits into two disconnected components

# find a cycle in undirected graph that visits every vertex (Hamiltonian cycle problem)

# find strongly connected components (DFS application)

# count number of connected components of graph given as adjacent matrix (using DFS)

# count number of connected components of graph given as adjacent matrix (using BFS)

# detect a cycle in undirected graph in constant time, not necessarily a minimum spanning tree

# detect cycle in directed graph

# find depth of directed acyclic graph
# for undirected graph, use simple unweighted shortest path algorithm and return highest no. among all distances

# determine whether a directed graph has a unique topological ordering

# find lowest common ancestor of 2 vertices in directed acyclic graph "DAG"

# Given DAG, find shortest ancestral path between two vertices

# check two given graphs are isomorphic or not

# given directed graph, return the reverse graph. each edge from v to w is replaced by edge from w to v


if __name__ == '__main__':
    # undirected graph - adjacency matrix
    # a-10-b-20-e
    # |30  |40  |60
    # d-50-c ...d
    graph1 = Graph_adj_matrix(5)
    graph1.add_vertex(0, 'a')
    graph1.add_vertex(1, 'b')
    graph1.add_vertex(2, 'c')
    graph1.add_vertex(3, 'd')
    graph1.add_vertex(4, 'e')
    graph1.add_edge('a', 'b', 10)
    graph1.add_edge('b', 'e', 20)
    graph1.add_edge('a', 'd', 30)
    graph1.add_edge('c', 'b', 40)
    graph1.add_edge('c', 'd', 50)
    graph1.add_edge('d', 'e', 60)

    print('Graph representation in adjacency matrix:', end = '\n')
    print(*graph1.get_adjacency_matrix(), sep= '\n')

    # undirected graph - adjacency list
    graph2 = Graph_adj_list()
    graph2.add_vertex('a')
    graph2.add_vertex('b')
    graph2.add_vertex('e')
    graph2.add_vertex('c')
    graph2.add_vertex('d')
    graph2.add_edge('a', 'b', 10)
    graph2.add_edge('b', 'e', 20)
    graph2.add_edge('a', 'd', 30)
    graph2.add_edge('b', 'c', 40)
    graph2.add_edge('c', 'd', 50)
    graph2.add_edge('d', 'e', 60)
    print('Graph representation in adjacency list:', end = '\n')
    for v in graph2:
        for key,value in v.get_connections().items():
            print('( %s , %s, %s)' % (v.getId(), key.getId(), value))