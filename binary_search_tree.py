import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_tree


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue( self, item ):
        self.items.insert(0, item)

    def dequeue( self ):
        return self.items.pop()

    def is_empty( self ):
        return len(self.items) == 0


class Stack(object):
    def __init__(self):
        self.items = []

    def push( self, item ):
        self.items.append(item)

    def pop( self ):
        if not self.is_empty:
            return self.items.pop()
        return

    def is_empty( self ):
        return len(self.items) == 0


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    # insert element
    def insert( self, value ):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert( self, node, value ):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        else:
            print('Value already in tree')

    # print tree-- preorder traversal
    def print( self ):
        if self.root is None:
            return
        return(self._print(self.root))

    def _print( self, node ):
        if node is None:
            return
        print(node.value, end=' ')
        self._print(node.left)
        self._print(node.right)

    # find an element, with recursion
    def search_with_recursion( self, item ):
        if item is None or self.root is None:
            return False
        return self._search_with_recursion(self.root, item)

    def _search_with_recursion( self, node, item ):
        if node is None:
            return False
        elif node.value == item:
            return True
        elif item < node.value:
            return self._search_with_recursion(node.left, item)
        else:
            return self._search_with_recursion(node.right, item)

    # find an element, without recursion
    def search_with_iteration( self, item ):
        if item is None or self.root is None:
            return False
        node = self.root
        while node is not None:
            if item > node.value:
                node = node.right
            elif item < node.value:
                node = node.left
            else:
                return True

        return False

    # height of tree
    def height( self, node ):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    # find maximum element in tree(with recursion)
    def maximum_element_with_recursion( self ):
        if self.root is None:
            print('Tree doesn\'t exist!')
        else:
            print('Maximum element recursively is: '+str(self._max_element_with_recursion(self.root)))

    max_elem = float( '-inf' )
    def _max_element_with_recursion( self, node ):
        if node:
            if node.value > self.max_elem:
                self.max_elem = node.value
            self._max_element_with_recursion(node.left)
            self._max_element_with_recursion(node.right)

        return self.max_elem

    # find minimum element in tree(without recursion)
    def minimum_element_with_iteration( self, node ):
        if node is None:
            return
        min_elem = float('inf')
        queue = Queue()

        queue.enqueue(node)
        while not queue.is_empty():
            node = queue.dequeue()

            if node.value < min_elem:
                min_elem = node.value

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return min_elem

    # check if binary tree is BST or not, complexity O(n^2)
    def check_binarytree_is_bst( self, node ):
        # empty tree is BST
        if node is None:
            return True
        # return false if max of node.left is > than node.value
        if node.left and self._max_element_with_recursion(node.left) > node.value:
            return False
        # return false if min of node.right is ≤ then node.value
        if node.right and self.minimum_element_with_iteration(node.right) <= node.value:
            return False
        # return false if recursively left subtree or right subtree is not BST
        if not self.check_binarytree_is_bst(node.left) or not self.check_binarytree_is_bst(node.right):
            return False

        # if passed all above conditions then its a BST
        return True

    # check if binary tree is BST or not, complexity O(n)
    def check_binarytree_is_bst_effeciently( self, node ):
        if node is None:
            return True
        return self._check_binarytree_is_bst_effeciently(node, float('-inf'), float('inf'))

    def _check_binarytree_is_bst_effeciently( self, node, min_value, max_value ):
        if node is None:
            return True
        # return false if node.value violates min max constraint
        if node.value < min_value or node.value > max_value:
            return False
        # otherwise check subtrees are recursively tightening the min or max constraint
        return (self._check_binarytree_is_bst_effeciently(node.left, min_value, node.value-1) and
                self._check_binarytree_is_bst_effeciently(node.right,node.value+1, max_value))

    # find k-th smallest element(recursively)
    def kth_smallest_element( self, k ):
        if self.root is None or k is None:
            return
        stack = Stack()
        return self._kth_smallest_element(self.root, stack).items[k-1]

    def _kth_smallest_element( self, node, stack ):
        # inorder traversal to store the elements of bst in sorted order
        if node:
            self._kth_smallest_element(node.left, stack)
            stack.push(node.value)
            self._kth_smallest_element(node.right, stack)

        return stack

    # given 2 nodes, find the lowest common ancestor in BST
    def lowest_common_ancestor( self, root, value1, value2 ):
        if root is None:
            return
        if root.value > max(value1, value2):
            return self.lowest_common_ancestor(root.left, value1, value2)
        elif root.value < min(value1, value2):
            return self.lowest_common_ancestor(root.right, value1, value2)
        else:
            return root

    # find shortest distance between 2 nodes
    def shortest_distance_between_two_nodes( self,root, value1, value2 ):
        if root is None:
            return 0
        if root.value > value1 and root.value > value2:
            return self.shortest_distance_between_two_nodes(root.left, value1, value2)
        if root.value < value1 and root.value < value2:
            return self.shortest_distance_between_two_nodes(root.right, value1, value2)
        if (root.value >= value1 and root.value <= value2) or (root.value <= value1 and root.value >= value2):
            return self.distance_from_root(root, value1) + self.distance_from_root(root, value2)

    def distance_from_root( self, node, value ):
        if node.value == value:
            return 0
        elif node.value > value:
            return 1+ self.distance_from_root(node.left, value)
        else:
            return 1+ self.distance_from_root(node.right, value)

    # count number of BSTs possible with n nodes

    # convert BST to circular doubly linked list with space complexity(1)

    # convert sorted doubly linked list to balanced BST

    # convert sorted array to BST, time complexity O(n)

    # convert singly linked list (sorted in ascending order) to height balanced BST

    # find floor of given data (largest data <= given data)

    # find ceiling of given data (smallest data > given data)

    # print all elements in range r1 to r2

    # trim the given BST, and form a new tree with all the elements between r1 to r2

    # check whether elements of 2 BSTs are same or not (order of elements doesn't matter)

    # delete an element

    # tell inorder successor of given key in BST

    # tell the predecessor of a node in BST


# BST
#           500
#          /   \
#        400   800
#       /  \   /  \
#     200 450 700 900

bst = Binary_Search_Tree(500)
bst.insert(400)
bst.insert(800)
bst.insert(200)
bst.insert(450)
bst.insert(700)
bst.insert(900)

print('Pre-order tree traversal:', end=' ')
bst.print()

print('\nSearch an item recursively: ', str(bst.search_with_recursion(700)))
print('Search an item iteratively: ', str(bst.search_with_iteration(700)))

print('height of tree:', str(bst.height(bst.root)))

print('Minimum element in tree(iteratively):', str(bst.minimum_element_with_iteration(bst.root)))

# binary tree
#       110
#      /   \
#   200      30
#  /  \     /
# 140  50   6
tree = binary_tree.BinaryTree(110)
tree.root.left = Node(200)
tree.root.right = Node(30)
tree.root.left.left = Node(140)
tree.root.left.right = Node(50)
tree.root.right.left = Node(6)
print('Binary tree', end = ' ')
tree.print_tree()
print('\nIs this binary tree a bst?(non-effecient solution):', str(bst.check_binarytree_is_bst(tree.root)))
print('Is this binary tree a bst?(effecient solution):', str(bst.check_binarytree_is_bst_effeciently(tree.root)))

print('kth smallest element in tree:', str(bst.kth_smallest_element(2)))

print('lowest common ancestor of two nodes:', str(bst.lowest_common_ancestor(bst.root, 700, 900).value))

print('shortest distance between two nodes:', str(bst.shortest_distance_between_two_nodes(bst.root, 200, 450)) )