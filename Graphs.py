from collections import defaultdict
import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_heaps
from . import disjoint_sets


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
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[-1] * vertices for x in range(vertices)]
        self.vertices_list = [0] * vertices

        def defaultvalue(): # return value for defaultdict if key is not present
            return -1
        # ex: a->0, b->1, c->2...
        self.vertex_id_to_num_map = defaultdict(defaultvalue)

    def add_vertex( self, vertex_num, vertex_id ):
        if 0 <= vertex_num < self.vertices:
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
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjacency_matrix[i][j] != -1:
                    edges.append((self.vertices_list[i], self.vertices_list[j], self.adjacency_matrix[i][j]))

        return edges

    def get_adjacency_matrix( self ):
        return self.adjacency_matrix

    # find shortest path in weighted directed graph (Dijkstra algorithm)
    # time O(E.logV) space O(E+V)when implemented using minheap. time O(V^2) otherwise

    # implementing slower solution, using adj matrix
    def dijkstra_algorithm( self, source ):
        dist = [float( 'inf' )] * self.vertices
        source = self.vertex_id_to_num_map[source]
        dist[source] = 0
        visited = [False] * self.vertices

        for i in range( self.vertices ):
            # find min distance vertex from vertices not yet processed
            # u is always equal to source in first iteration
            u = self._min_distance( dist, visited )

            # put min distance vertex to shortest path tree
            visited[u] = True

            # update distance for adjacent vertices of current vertex,
            # only if new distance is shorter than the current distance
            # and vertex is not in shortest path tree
            for v in range( self.vertices ):
                newDistance = dist[u] + self.adjacency_matrix[u][v]
                if self.adjacency_matrix[u][v] > 0 and visited[v] == False and \
                    newDistance < dist[v]:
                    dist[v] = newDistance

        return distance

    # returns vertex with min distance value among the set of vertices not yet included in shortest path tree
    def _min_distance( self, dist, visited ):
        min_dist = float('inf')
        min_index = 0
        for v in range(self.vertices):
            if dist[v] < min_dist and visited[v] == False:
                min_dist = dist[v]
                min_index = v

        return min_index

    # find shortest distance from src to all vertices in weighted graph with negative edges (Bellman-Ford algorithm)
    def bellman_ford_algorithm( self, src ):
        src = self.vertex_id_to_num_map[src]
        # 1. initialize distances from src to all other vertices as INFINITE
        dist = [float( 'inf' )] * self.vertices
        dist[src] = 0

        # 2. Relax all edges | V | - 1 times.
        # A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
        for i in range( self.vertices - 1 ):
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
        min_weight_edge = [float('inf')] * self.vertices
        parnt = [-1] * self.vertices

        visited = [False] * self.vertices

        # make vertex 0 as 0 so that it is picked as first vertex
        min_weight_edge[0] = 0
        parnt[0] = -1

        for i in range(self.vertices):
            # find min distance vertex from vertices not yet processed
            # u is always equal to source in first iteration
            u = self._min_distance( min_weight_edge, visited )

            # put min distance vertex to shortest path tree
            visited[u] = True

            # update distance for adjacent vertices of current vertex,
            # only if new distance is shorter than the current distance
            # and vertex is not in shortest path tree
            for v in range( self.vertices ):
                if 0 < self.adjacency_matrix[u][v] < min_weight_edge[v] and visited[v] == False:
                    min_weight_edge[v] = self.adjacency_matrix[u][v]
                    parnt[v] = u

        result = []
        for i in range(1, self.vertices):
            result.append('edge'+str(parnt[i])+'-'+str(i)+'->weight'+str(self.adjacency_matrix[i][parnt[i]]))

        return result

    # Given a graph as adjacency matrix, check whether graph has simple path from source to destination
    # solution : start from source vertex, do either a BFS or DFS and if we find the destination vertex while traversal
    # then the path exists otherwise not.

    # Given a graph as adjacency matrix, print all simple paths from source to destination in graph
    def print_all_paths_src_to_dst( self, src, dst ):
        # Mark all the vertices as not visited
        visited = [False] * self.vertices

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
            for i in range(self.vertices):
                if not visited[i]:
                    self._print_all_paths_src_to_dst(i, dst, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # find shortest path between every pair of vertices in graph. Assume graph has negative edges but not -ve cycle
    # Floyd-Warshall algorithm , time O(n^3)
    def floyd_warshall_algorithm( self ):
        tmp = [float('inf')* self.vertices for x in range(self.vertices)]
        # create tmp array according to the given graph
        # d[v][u] = infinity for each pair (v,u)
        # d[v][v] = 0 for each vertex v

        for k in range( self.vertices ):
            for i in range( self.vertices ):
                for j in range( self.vertices ):
                    tmp[i][j] = min( tmp[i][j], tmp[i][k] + tmp[k][j] )

        return tmp

    # find a cycle in undirected graph that visits every vertex (Hamiltonian cycle problem) using backtracking
    def detect_hamiltonian_cycle_undirected_graph( self ):
        path = [-1] * self.vertices

        # put vertex 0 as first vertex in path.
        # If there is a Hamiltonian Cycle, then path can be started from any point of cycle as the graph is undirected
        path[0] = 0

        if not self._detect_hamiltonian_cycle_undirected_graph(path, 1):
            return False

        for vertex in path:
            print(self.vertices_list[vertex], end=', ')
        print(self.vertices_list[path[0]], end='\n')

        return True

    def _detect_hamiltonian_cycle_undirected_graph( self, path, position ):
        # base case: if all vertices are included in path
        if position == self.vertices:
            # Last vertex must be adjacent to the first vertex in path to make a cycle
            if self.adjacency_matrix[path[position-1]][path[0]] == 1:
                return True
            else:
                return False

        # try different vertices as a next candidate in Hamiltonian cycle, except 0 because we took 0 as starting point
        for v in range(1, self.vertices):
            if self.is_safe(v, position, path):
                path[position] = v
                if self._detect_hamiltonian_cycle_undirected_graph(path, position+1):
                    return True
                # remove current vertex if it doesn't lead to a solution
                path[position] = -1

        return False

    # Check if vertex v is an adjacent vertex of previously added vertex and is not already included in the path
    def is_safe( self, v, position, path ):
        # Check if current vertex and last vertex in path are adjacent
        if self.adjacency_matrix[path[position - 1]][v] == 0:
            return False

        # Check if current vertex is already in path then return False
        if v in path:
            return False

        return True


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
        self.vertices = 0

    def add_vertex( self, id ):
        self.vertices += 1
        newVertex = adj_list_vertex(id)
        self.vertices_list[id] = newVertex

    def remove_vertex( self, id ):
        self.vertices -= 1
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
            if not visited[id]:
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
        # solution: uses makeSet, findSet, union operations of Disjoint sets.

    # find shortest path between every pair of vertices in graph. Assume graph doesn't have negative edges
    # can be solved using n applications of Dijkstra, time O(V.(V.logV + E))

    # detect a cycle in directed graph
    def detect_cycle_directed_graph( self ):
        # mark all vertices as not visited
        def defaultvalue():
            return False
        # key= id, value= True/False
        visited = defaultdict( defaultvalue )

        stack = Stack()

        # this loop is to handle the disconnected vertices of graph
        for id in self.vertices_list.keys():
            if not visited[id]:
                if self._detect_cycle_directed_graph(id, visited, stack):
                    return True
        return False

    # returns true if graph contains a cycle
    def _detect_cycle_directed_graph( self, curr_id, visited, stack ):
        # mark curr_id as visited
        visited[curr_id] = True
        # add curr_id to stack
        stack.push(curr_id)

        # recur for all adjacent/ neighbor vertices
        neighbor_nodes = self.vertices_list[curr_id].connectedTo

        for node in neighbor_nodes:
            # if any neighbor is visited or it is in stack then graph is cyclic
            if not visited[node.id]:
                if self._detect_cycle_directed_graph( node.id, visited, stack ):
                    return True
            elif node.id in stack.items:
                    return True
        # pop out the node from stack before this function call ends
        stack.items.remove(curr_id)
        return False

    # detect a cycle in undirected graph , time O(V+E)
    def detect_cycle_undirected_graph( self ):
        # mark all vertices as not visited
        def defaultvalue():
            return False
        # key= id, value= True/False
        visited = defaultdict( defaultvalue )

        # this loop is to handle the disconnected vertices of graph
        for id in self.vertices_list.keys():
            if not visited[id]:
                if self._detect_cycle_undirected_graph( id, visited, -1 ):
                    return True
        return False

    def _detect_cycle_undirected_graph( self, curr_id, visited, parent_id ):
        # mark curr_id as visited
        visited[curr_id] = True

        # recur for all adjacent/ neighbor vertices
        neighbor_nodes = self.vertices_list[curr_id].connectedTo

        for node in neighbor_nodes:
            # if a neighbor node is not visited then recurse on it
            if not visited[node.id]:
                if self._detect_cycle_undirected_graph( node.id, visited, curr_id ):
                    return True
            # if parent is not visited but neighbor is visited then there is a cycle
            elif parent_id != node.id:
                return True

        return False

    # find the cut-vertex/ articulation point in an undirected graph (DFS application)
    # Articulation point is a vertex if removed then graph splits into two disconnected components
    def find_articulation_points( self ):
        # mark all vertices as not visited
        def defaultvalue():
            return False
        visited = defaultdict(defaultvalue)

        # store articulation points
        articulation_points = defaultdict( defaultvalue )

        # key = vertex id, value = parent to this vertex
        def defaultval():
            return None
        parnt = defaultdict( defaultval )

        # discovery time of visited vertices
        def dvalue():
            return float('inf')
        discovery_time = defaultdict(dvalue)

        # low time
        low_time = defaultdict( dvalue )

        # find articulation points in DFS tree rooted at vertex i
        for id in self.vertices_list:
            if not visited[id]:
                self._articulation_points(self.vertices_list[id], visited, articulation_points, parnt, low_time, discovery_time)

        for index, value in enumerate( articulation_points):
            if value: print( index, end=', ' )

    time = 0
    def _articulation_points( self, curr, visited, articulation_points, parnt, low_time, discovery_time ):
        # count of children in current node
        children = 0

        # Mark the current node as visited and print it
        visited[curr.id]= True

        # Initialize discovery time and low value
        discovery_time[curr.id] = self.time
        low_time[curr.id] = self.time
        self.time += 1

        # Recur for all the vertices adjacent to curr
        for v in curr.connectedTo.keys():
            v = v.getId()
            # If v is not visited yet, then make it a child of curr in DFS tree and recur for it
            if not visited[v]:
                parnt[v] = curr
                children += 1
                self._articulation_points( self.vertices_list[v], visited, articulation_points,
                                           parnt, low_time, discovery_time )

                # if the subtree rooted with v has a connection to one of the ancestors of curr
                low_time[curr] = min( low_time[curr], low_time[v] )

                # curr is an articulation point in following cases:

                # (1) curr is root of DFS tree and has two or more children
                if parnt[curr] == -1 and children > 1:
                    articulation_points[curr] = True

                # (2) If curr is not root and low_time of one of its child is more than discovery_time of curr.
                if parnt[curr] != -1 and low_time[v] >= discovery_time[curr]:
                    articulation_points[curr] = True

                # Update low_time of curr for parent function calls
                elif v != parnt[curr]:
                    low_time[curr] = min( low_time[curr], discovery_time[v] )

    # find cut-edge in an undirected graph (DFS application)
    # cut-edge is an edge if removed then graph splits into two disconnected components
        # solution: time O(V+E)
        # For every edge( u, v ), do following
        # a) Remove( u, v ) from graph
        # b) See if the graph remains connected( We can either use BFS or DFS)
        # c) Add( u, v ) back to the graph

    # find strongly connected components (DFS application)
    # strongly connected means every pair of vertices is mutually reachable
    def find_strongly_connected_components( self ):
        stack = Stack()

        # mark all vertices as not visited, for first DFS
        def defaultvalue():
            return False
        visited = defaultdict( defaultvalue )

        # push vertices in stack according to their finishing time
        for id in self.vertices_list:
            if not visited[id]:
                self._push_vertices_in_order(id, visited, stack)

        # Create a reversed graph
        transposed_graph = self.getTranspose()

        # Mark all the vertices as not visited, for second DFS
        def defaultvalue():
            return False
        visited = defaultdict( defaultvalue )

        # Now process all vertices in order defined by Stack
        while not stack.is_empty():
            i = stack.items.pop()
            if not visited[i]:
                transposed_graph._depth_first_search( i, visited)
                print(end=' ')

    def _push_vertices_in_order(self, curr_id, visited, stack):
        # Mark the current node as visited
        visited[curr_id] = True

        # recur for all adjacent/ neighbor vertices
        neighbor_nodes = self.vertices_list[curr_id].connectedTo

        for node in neighbor_nodes:
            # if a neighbor node is not visited then recurse on it
            if not visited[node.id]:
                self._push_vertices_in_order( node.id, visited, stack )
        stack.push( curr_id )

    # returns the transpose of this graph
    def getTranspose( self ):
        g = Graph_adj_list()

        # recur for all adjacent/ neighbor vertices
        for id in self.vertices_list:
            neighbor_nodes = self.vertices_list[id].connectedTo
            for node in neighbor_nodes:
                g.add_edge_directed_graph(node.id, id)

        return g

    # count number of connected components of undirected graph given as adjacent matrix (using DFS)
    def number_of_connected_components( self ):
        # mark all vertices as not visited
        def defaultvalue():
            return False
        visited = defaultdict( defaultvalue )
        count = 0
        for id in self.vertices_list:
            if not visited[id]:
                # print all reachable vertices from id
                self._depth_first_search(id, visited)
                count += 1
                print('and')
        return count

    # count number of connected components of graph given as adjacent matrix (using BFS)

    # find depth/ longest path of directed acyclic graph
    # for undirected graph, use simple unweighted shortest path algorithm and return highest no. among all distances
        # solution:
        # 1. initialize distance as float('-inf') for all vertices and distance[source_vertex] as 0
        # 2. create topological order of all vertices
        # 3. For every vertex u in topological order do: For every adjacent vertex v of u do:
        #       if distance[v] < distance[u] + cost[u][v] then distance[v] = distance[u] + cost[u][v]

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
    print('Undirected Graph representation in adjacency list:', end = '\n')
    for v in graph2:
        for key,value in v.connectedTo.items():
            print('( %s , %s, %s)' % (v.getId(), key.getId(), value))

    # create a directed acyclic graph - adj list
    graph3 = Graph_adj_list()
    graph3.add_vertex( 'a' )
    graph3.add_vertex( 'b' )
    graph3.add_vertex( 'c' )
    graph3.add_vertex( 'e' )
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

    # print('All pairs shortest path problem- Floyd Warshall using adj matrix graph:', graph4.floyd_warshall_algorithm())

    print('Finding articulation points in undirected graph adj list:', graph2.find_articulation_points())

    # create another directed acyclic graph - adj list
    graph_x = Graph_adj_list()
    graph_x.add_vertex( 'a' )
    graph_x.add_vertex( 'b' )
    graph_x.add_vertex( 'c' )
    graph_x.add_edge_directed_graph( 'a', 'b', 20 )
    graph_x.add_edge_directed_graph( 'b', 'c', 30 )
    graph_x.add_edge_directed_graph( 'c', 'a', 50 )
    print('Detect cycle in a directed graph using adj list:', graph_x.detect_cycle_directed_graph())

    print('Detect cycle in an undirected graph using adj list:', graph2.detect_cycle_undirected_graph())

    # create another undirected graph- adj matrix
    graph_y = Graph_adj_matrix( 5 )
    graph_y.add_vertex( 0, 'a' )
    graph_y.add_vertex( 1, 'b' )
    graph_y.add_vertex( 2, 'c' )
    graph_y.add_vertex( 3, 'd' )
    graph_y.add_vertex( 4, 'e' )
    #       (a)--(b)--(c)
    #        |   / \   |
    #        |  /   \  |
    #        | /     \ |
    #       (e)-------(d)
    # Has Hamiltonian Cycle
    graph_y.adjacency_matrix = [[0, 1, 0, 1, 0],
                                [1, 0, 1, 1, 1],
                                [0, 1, 0, 0, 1],
                                [1, 1, 0, 0, 1],
                                [0, 1, 1, 1, 0]]
    #       (a)--(b)--(c)
    #        |   / \   |
    #        |  /   \  |
    #        | /     \ |
    #       (e)       (d)
    # Doesn't have Hamiltonian cycle
    # graph_y.adjacency_matrix = [[0, 1, 0, 1, 0],
    #                             [1, 0, 1, 1, 1],
    #                             [0, 1, 0, 0, 1],
    #                             [1, 1, 0, 0, 0],
    #                             [0, 1, 1, 0, 0]]
    print('Detect Hamiltonian cycle in undirected adj matrix graph:',end = ' ')
    graph_y.detect_hamiltonian_cycle_undirected_graph()

    print('All strongly connected components in adj list directed graph:', end=' ')
    graph3.find_strongly_connected_components()

    # create another undirected graph using adjacency list
    graph5 = Graph_adj_list()
    graph5.add_vertex( 'a' )
    graph5.add_vertex( 'b' )
    graph5.add_vertex( 'c' )
    graph5.add_vertex( 'd' )
    graph5.add_vertex( 'e' )
    graph5.add_edge( 'a', 'b', 10 )
    graph5.add_edge( 'a', 'c', 20 )
    graph5.add_edge( 'd', 'e', 30 )
    print('\nConnected components in undirected adj list graph:', end='')
    print('count of connected components is:',graph5.number_of_connected_components())