from collections import defaultdict
import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_heaps


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue( self, item ):
        self.items.insert(0, item)

    def dequeue( self ):
        if not self.is_empty():
            return self.items.pop()

    def is_empty( self ):
        return len(self.items) == 0

class Stack(object):
    def __init__(self):
        self.items = []

    def push( self, value ):
        self.items.append(value)

    def pop( self ):
        if not self.is_empty:
            return self.items.pop()

    def is_empty( self ):
        return len(self.items) == 0

# graph representation using adjacency matrix
class Graph_adj_matrix(object):
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjacency_matrix = [[-1] * no_of_vertices for x in range(no_of_vertices)]
        self.vertices_list = [0] * no_of_vertices

        def defaultvalue(): # return value for defaultdict if key is not present
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

    def add_edge_directed_graph( self, frm, to, cost = 0 ):
        frm_num = self.vertex_id_to_num_map[frm]
        to_num = self.vertex_id_to_num_map[to]
        self.adjacency_matrix[frm_num][to_num] = cost

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

    # find shortest path in weighted directed graph (Dijkstra algorithm)
    # time O(E.logV) space O(E+V)when implemented using minheap. time O(V^2) otherwise

    # implementing slower solution, using adj matrix
    def dijkstra_algorithm( self, source ):
        dist = [float( 'inf' )] * self.no_of_vertices
        source = self.vertex_id_to_num_map[source]
        dist[source] = 0
        visited = [False] * self.no_of_vertices

        for i in range( self.no_of_vertices ):
            # find min distance vertex from vertices not yet processed
            # u is always equal to source in first iteration
            u = self._min_distance( dist, visited )

            # put min distance vertex to shortest path tree
            visited[u] = True

            # update distance for adjacent vertices of current vertex,
            # only if new distance is shorter than the current distance
            # and vertex is not in shortest path tree
            for v in range( self.no_of_vertices ):
                newDistance = dist[u] + self.adjacency_matrix[u][v]
                if self.adjacency_matrix[u][v] > 0 and visited[v] == False and \
                    newDistance < dist[v]:
                    dist[v] = newDistance

        return distance

    # returns vertex with min distance value among the set of vertices not yet included in shortest path tree
    def _min_distance( self, dist, visited ):
        min_dist = float('inf')
        min_index = 0
        for v in range(self.no_of_vertices):
            if dist[v] < min_dist and visited[v] == False:
                min_dist = dist[v]
                min_index = v

        return min_index

    # find shortest distance from src to all vertices in weighted graph with negative edges (Bellman-Ford algorithm)
    def bellman_ford_algorithm( self, src ):
        src = self.vertex_id_to_num_map[src]
        # 1. initialize distances from src to all other vertices as INFINITE
        dist = [float( 'inf' )] * self.no_of_vertices
        dist[src] = 0

        # 2. Relax all edges | V | - 1 times.
        # A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
        for i in range( self.no_of_vertices - 1 ):
            # Update dist value and parent index of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are still in queue
            for u, v, w in self.get_edges():
                u, v = self.vertex_id_to_num_map[u], self.vertex_id_to_num_map[v]
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # 3. check for negative-weight cycles
        for u, v, w in self.get_edges():
            u, v = self.vertex_id_to_num_map[u], self.vertex_id_to_num_map[v]
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print('Graph contains negative weight cycle')
                return

        return dist

    # find minimum spanning tree in undirected weighted graph - Prim's algorithm
    # for unweighted graphs we consider all weights are equal
    def prims_algorithm( self ):
        # used to pick the minimum weight edge
        min_weight_edge = [float('inf')] * self.no_of_vertices
        parnt = [-1] * self.no_of_vertices

        visited = [False] * self.no_of_vertices

        # make vertex 0 as 0 so that it is picked as first vertex
        min_weight_edge[0] = 0
        parnt[0] = -1

        for i in range(self.no_of_vertices):
            # find min distance vertex from vertices not yet processed
            # u is always equal to source in first iteration
            u = self._min_distance( min_weight_edge, visited )

            # put min distance vertex to shortest path tree
            visited[u] = True

            # update distance for adjacent vertices of current vertex,
            # only if new distance is shorter than the current distance
            # and vertex is not in shortest path tree
            for v in range( self.no_of_vertices ):
                if 0 < self.adjacency_matrix[u][v] < min_weight_edge[v] and visited[v] == False:
                    min_weight_edge[v] = self.adjacency_matrix[u][v]
                    parnt[v] = u

        result = []
        for i in range(1, self.no_of_vertices):
            result.append('edge'+str(parnt[i])+'-'+str(i)+'->weight'+str(self.adjacency_matrix[i][parnt[i]]))

        return result

    # Given a graph as adjacency matrix, check whether graph has simple path from source to destination
    # solution : start from source vertex, do either a BFS or DFS and if we find the destination vertex while traversal
    # then the path exists otherwise not.

    # Given a graph as adjacency matrix, print all simple paths from source to destination in graph
    def print_all_paths_src_to_dst( self, src, dst ):
        # Mark all the vertices as not visited
        visited = [False] * self.no_of_vertices

        # Create an array to store paths
        path = []

        src, dst = self.vertex_id_to_num_map[src], self.vertex_id_to_num_map[dst]
        self._print_all_paths_src_to_dst(src, dst, visited, path)

    # prints all paths from u to dst
    def _print_all_paths_src_to_dst( self, u, dst, visited, path ):
        # mark current vertex as visited and append to path
        visited[u] = True
        path.append(u)

        if u == dst:
            print(path)
        else:
            # recur for all vertices adjacent to current vertex
            for i in range(self.no_of_vertices):
                if not visited[i]:
                    self._print_all_paths_src_to_dst(i, dst, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # find shortest path between every pair of vertices in graph. Assume graph has negative edges but not -ve cycle
    # Floyd-Warshall algorithm , time O(n^3)
    def floyd_warshall_algorithm( self ):
        tmp = [float('inf')* self.no_of_vertices for x in range(self.no_of_vertices)]
        # create tmp array according to the given graph
        # d[v][u] = inf for each pair (v,u)
        # d[v][v] = 0 for each vertex v

        for k in range( self.no_of_vertices ):
            for i in range( self.no_of_vertices ):
                for j in range( self.no_of_vertices ):
                    tmp[i][j] = min( tmp[i][j], tmp[i][k] + tmp[k][j] )

        return tmp


class adj_list_vertex(object):
    def __init__(self, id):
        self.id = id

        def defaultvalue():
            return -1
        # key = neighbor_id, value = cost
        self.connectedTo = defaultdict(defaultvalue)

    def add_neighbor( self, neighbor, cost ):
        self.connectedTo[neighbor] = cost

    def getId( self ):
        return self.id

    def getCost( self, neighbor ):
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

    def remove_vertex( self, id ):
        self.no_of_vertices -= 1
        if id in self.vertices_list.keys():
            del self.vertices_list[id]

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
        self.vertices_list[to].add_neighbor( self.vertices_list[frm], cost) # for undirected graphs only

    def add_edge_directed_graph( self, frm, to, cost = 0 ):
        if frm not in self.vertices_list:
            self.add_vertex(frm)
        if to not in self.vertices_list:
            self.add_vertex(to)
        self.vertices_list[frm].add_neighbor(self.vertices_list[to], cost)

    def get_vertices( self ):
        return self.vertices_list.keys()

    def __iter__(self):
        # iter creates an object that can be iterated one at a time
        return iter(self.vertices_list.values())

    # graph traversal - Depth First Search, time O(V+E)
    def depth_first_search( self):
        def defaultvalue():
            return False
        # key= id, value= True/False
        visited = defaultdict(defaultvalue)

        # this loop is to handle the disconnected vertices of graph
        for id in self.vertices_list.keys():
            if visited[id] == False:
                self._depth_first_search(id, visited)

    # recursive function for DFS or use stack for DFS
    def _depth_first_search( self, curr_id, visited):
        # mark current id as visited
        visited[curr_id] = True
        print(curr_id, end= ', ')

        # recur for all vertices adjacent to the curr_id
        neighbor_nodes = self.vertices_list[curr_id].connectedTo

        for node in neighbor_nodes:
            if not visited[node.id]:
                self._depth_first_search(node.id, visited)

    # graph traversal - Breadth First Search, time O(V+E)
    def breadth_first_search( self):
        def defaultvalue():
            return False

        # key= id, value= True/False
        visited = defaultdict( defaultvalue )

        # queue for BFS
        queue = Queue()

        # this loop is to handle the disconnected vertices of graph
        for id in self.vertices_list.keys():
            # if an id is not visited then BFS through it
            if not visited[id]:
                visited[id] = True
                queue.enqueue(id)

                while not queue.is_empty():
                    # dequeue an id from queue and print it
                    curr_id = queue.dequeue()
                    print(curr_id, end = ', ')

                    # get adj vertices of curr_id. If any id is found with visited False then mark it and enqueue
                    neighbor_nodes = self.vertices_list[curr_id].connectedTo

                    for node in neighbor_nodes:
                        if not visited[node.id]:
                            queue.enqueue(node.id)
                            visited[node.id] = True

    # topological sort in directed acyclic graph
    def topological_sort_DAG( self ):
        # mark all vertices as not visited
        def defaultvalue():
            return False

        # key= id, value= True/False
        visited = defaultdict( defaultvalue )
        stack = Stack()

        # this loop is to handle the disconnected vertices of graph
        for id in self.vertices_list.keys():
            if not visited[id]:
                self._topological_sort_DAG(id, visited, stack)

        return stack

    def _topological_sort_DAG( self, curr_id, visited, stack ):
        # mark curr_id as visited
        visited[curr_id] = True

        # recur for all adjacent/ neighbor vertices
        neighbor_nodes = self.vertices_list[curr_id].connectedTo

        for node in neighbor_nodes:
            if not visited[node.id]:
                self._topological_sort_DAG(node.id, visited, stack)

        # a vertex is pushed to stack only when all its adjacent vertices are already in stack
        stack.items.insert(0,curr_id)

    # find shortest distance from src to all vertices in unweighted directed graph (modified BFS)
    def shortest_path_modified_BFS( self, source ):

        def defaultvalue():
            return False
        visited = defaultdict(defaultvalue)

        # key = id, value = shortest distance from source to this vertex
        def defvalue():
            return 0
        distance = defaultdict(defvalue)

        # key = vertex id, value = parent to this vertex
        def defaultval():
            return None
        parent = defaultdict(defaultval)

        # queue for bfs
        queue = Queue()
        queue.enqueue(source)
        visited[source] = True

        while not queue.is_empty():
            curr_id = queue.dequeue()
            # get adj vertices of curr_id. If any id is found with visited False then mark it and enqueue
            neighbor_nodes = self.vertices_list[curr_id].connectedTo
            for node in neighbor_nodes:
                if not visited[node.id]:
                    queue.enqueue( node.id )
                    visited[node.id] = True
                    parent[node.id] = curr_id
                    distance[node.id] = distance[curr_id] + 1

        return parent, distance

    # find minimum spanning tree in undirected weighted graph - Kruskal's algorithm
    # def kruskal_algorithm( self ):

    # find shortest path between every pair of vertices in graph. Assume graph doesn't have negative edges
    # can be solved using n applications of Dijkstra

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
    # create an undirected graph using adjacency matrix
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
    print('Undirected Graph representation in adjacency matrix:', end = '\n')
    print(*graph1.get_adjacency_matrix(), sep= '\n')

    # create a directed acyclic graph - adj matrix
    graph4 = Graph_adj_matrix( 5 )
    graph4.add_vertex( 0, 'a' )
    graph4.add_vertex( 1, 'b' )
    graph4.add_vertex( 2, 'c' )
    graph4.add_vertex( 3, 'd' )
    graph4.add_vertex( 4, 'e' )
    graph4.add_edge_directed_graph( 'a', 'b', 10 )
    graph4.add_edge_directed_graph( 'b', 'e', 20 )
    graph4.add_edge_directed_graph( 'a', 'd', 30 )
    graph4.add_edge_directed_graph( 'b', 'c', 40 )
    graph4.add_edge_directed_graph( 'd', 'c', 60 )
    graph4.add_edge_directed_graph( 'e', 'd', 50 )
    print( 'Directed Graph representation in adjacency matrix:', end='\n' )
    print( *graph4.get_adjacency_matrix(), sep='\n' )

    # create an undirected graph using adjacency list
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
    print('Undirected Graph representation in adjacency list:', end = '\n')
    for v in graph2:
        for key,value in v.connectedTo.items():
            print('( %s , %s, %s)' % (v.getId(), key.getId(), value))

    # create a directed acyclic graph - adj list
    graph3 = Graph_adj_list()
    graph3.add_vertex( 'a' )
    graph3.add_vertex( 'b' )
    graph3.add_vertex( 'e' )
    graph3.add_vertex( 'c' )
    graph3.add_vertex( 'd' )
    graph3.add_edge_directed_graph( 'a', 'b', 10 )
    graph3.add_edge_directed_graph( 'b', 'e', 20 )
    graph3.add_edge_directed_graph( 'a', 'd', 30 )
    graph3.add_edge_directed_graph( 'b', 'c', 40 )
    graph3.add_edge_directed_graph( 'd', 'c', 60 )
    graph3.add_edge_directed_graph( 'e', 'd', 50 )
    print( 'Directed Graph representation in adjacency list:', end='\n' )
    for v in graph3:
        for key, value in v.connectedTo.items():
            print( '( %s , %s, %s)' % (v.getId(), key.getId(), value) )

    print('Depth first search using adj list undirected graph:', end=' ')
    graph2.depth_first_search()

    print( '\nBreadth first search using adj list undirected graph:', end=' ' )
    graph2.breadth_first_search()

    print('\nTopological sorting DAG adj list:', graph3.topological_sort_DAG().items)

    print('Shortest path in unweighted graph from source using modified BFS:', end = '\n')
    parent, distance = graph2.shortest_path_modified_BFS( 'a' )
    for d in distance.keys():
        print(d,'is',distance[d],'distance from source')
    for p in parent.keys():
        print(p,'has parent',parent[p])

    print('Dijkstra\'s algorithm using adj matrix graph, slower implementation:', end='\n')
    dist = graph4.dijkstra_algorithm('a')
    for d in dist.keys():
        print(d,'is',dist[d],'distance from source')

    print('Bellman Ford algorithm using adj matrix graph:', graph4.bellman_ford_algorithm('a'))

    print('Prim\'s algorithm using adj matrix graph:', graph4.prims_algorithm())

    print('All paths from source to destination using adj matrix graph:', end = '\n')
    graph4.print_all_paths_src_to_dst( 'a', 'e' )

    print('All pairs shortest path problem- Floyd Warshall using adj matrix graph:', graph4.floyd_warshall_algorithm())
