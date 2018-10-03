class Disjoint_Sets(object):
    def __init__( self, no_of_elements ):
        self.no_of_elements = no_of_elements
        # tells the parent of each vertex, -ve value means its the root
        # number after -ve sign will tell how many vertices are contained within this set
        # initially all vertices are parent of themselves
        self.parent = [-1]*(no_of_elements+1)
        # every index represents a vertex, so 0 is no vertex. ex, vertex 1 at index 1, vertex 2 at index 2...
        self.parent[0] = None

    def find_root_of_vertex( self, x ):
        # if value at index of x is not -1 then it is not the parent of itself
        if self.parent[x] > 0:
            # find the parent of value at x, by recursively calling find
            # move the vertex directly under the root of this set
            self.parent[x] = self.find_root_of_vertex(self.parent[x])
            return self.parent[x]
        else:
            return x

    # unites the sets that contain vertex x and y
    def union_by_rank( self, x, y ):
        # find roots of two sets, x and y
        x_root = self.find_root_of_vertex(x)
        y_root = self.find_root_of_vertex(y)

        # if both elements are in same set then no need to unite anything
        if x_root == y_root:
            return None

        # if x's rank < y's rank
        if abs(self.parent[x_root]) < abs(self.parent[y_root]):
            # move x under y
            self.parent[x] = y_root
            self.parent[y_root] -= 1
        # else if x's rank >= y's rank
        elif abs(self.parent[x_root]) >= abs(self.parent[y_root]):
            # move y under x
            self.parent[y] = x_root
            self.parent[x_root] -= 1


if __name__ == '__main__':
    disjoint_set = Disjoint_Sets(8)
    print('initial disjoint set:', disjoint_set.parent)

    print('Find root of given vertex:', disjoint_set.find_root_of_vertex(2))

    disjoint_set.union_by_rank(1,2)
    disjoint_set.union_by_rank( 2, 3 )
    disjoint_set.union_by_rank( 3, 4 )
    disjoint_set.union_by_rank( 5, 6)
    disjoint_set.union_by_rank( 6, 7 )
    disjoint_set.union_by_rank( 7, 8 )
    print('Unite two sets:', disjoint_set.parent)

    disjoint_set.union_by_rank(4,8)
    print( 'Unite two sets after adding an edge:', disjoint_set.parent )



