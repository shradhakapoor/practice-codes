import os
__path__ = [os.path.dirname(os.path.abspath(__file__))]
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

    # print tree-- Inorder traversal
    def print( self ):
        if self.root is None:
            return
        return(self._print(self.root))

    def _print( self, node ):
        if node is None:
            return
        if node.left:
            self._print( node.left )
        print(node.value, end=' ')
        if node.right:
            self._print(node.right)

    # Tree sorting
    def tree_sort(self, root):
        # Using recursion
        # print elements in inorder traversal

        # using iteration
        stack = Stack()
        done = 0
        curr = root

        while not done:
            # reach the leftmost node of current node
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                # backtrack from empty subtree up towards the top of stack
                if not stack.is_empty():
                    curr = stack.items.pop()
                    print(curr.value, end=', ')
                    # we have visited the node , its left subtree. Now we visit its right subtree
                    curr = curr.right

                else:
                    done = 1

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
    def _max_element_with_recursion( self, node):
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

        curr = node
        while curr.left:
            curr = curr.left

        return curr.value

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

    # count number of BSTs possible with n nodes = catalan number (2nCn)/n+1 = 2n! / (n+1! n!)
    # count of number of Binary Trees with n nodes  = n! * catalan number
    def count_of_BST_possible( self, n ):
        if n is None:
            return 0

        # calculate 2n!
        twice_n = 1
        tn = (2 * n) + 1
        for i in range(1, tn):
            twice_n = twice_n * i
        # calculate n!
        single_n = 1
        for i in range(1, n+1):
            single_n *= i
        # find n+1! by n! * n+1
        n_1 = single_n * (n + 1)
        # result = catalan number
        result = twice_n / (single_n * n_1)

        return result

    # convert sorted array to BST, time complexity O(n)
    def sorted_array_to_bst( self, arr ):
        if len(arr) == 0: return
        if len(arr) == 1:
            root = Node(arr[0])
            return root
        mid = int(len(arr)/2)
        root = Node(arr[mid])

        if arr[mid-1] < arr[mid+1]:
            arr1 = arr[0:mid]
            arr2 = arr[(mid+1):]
        else:
            arr1 = arr[(mid + 1):]
            arr2 = arr[0:mid]

        root.left = self.sorted_array_to_bst(arr1)
        root.right = self.sorted_array_to_bst(arr2)

        return root

    # find floor of given data (largest data <= given data)
    def floor_of_given_value( self, root, value ):
        if root is None:
            return -1
        if root.value == value: return root.value

        # if root.value > value, then floor would be in left subtree
        if root.left:
            if root.value > value: return self.floor_of_given_value(root.left, value)

        # if root.value < value then floor is either the root or in right subtree
        if root.right:
            right_value = self.floor_of_given_value(root.right, value)
            return right_value if right_value <= value else root.value

        return root.value

    # find ceiling of given data (smallest data > given data)
    def ceil_of_given_value( self, root, value ):
        if root is None:
            return -1

        # equal to key value
        if value == root.value: return root.value

        # if root.value < value, ceil must be in right subtree
        if root.right:
            if root.value < value: return  self.ceil_of_given_value(root.right, value)

        # if root.value > value, ceil is either root.value or in left subtree
        if root.left:
            left_value = self.ceil_of_given_value(root.left, value)
            return left_value if left_value >= value else root.value

        return root.value

    # print all elements in increasing order in range r1 to r2
    def print_all_in_range( self, root, r1, r2 ):
        if root is None:
            return

        # since desired output is sorted, recurse for left subtree first
        # if root.value > r1 only then we can get elements in left subtree
        if r1 < root.value:
            self.print_all_in_range(root.left, r1, r2)

        if r1 <= root.value <= r2:
            print (root.value, end=', ')

        # if r2 > root.value only then we can get elements in right subtree
        if r2 > root.value:
            self.print_all_in_range(root.right, r1, r2)

    # remove BST elements outside the given range, and modified tree should also be BST
    def remove_elements_outside_range( self, root, r1, r2 ):
        if root is None: return

        # basically we need to fix the tree in post-order fashion
        root.left = self.remove_elements_outside_range(root.left, r1, r2)
        root.right = self.remove_elements_outside_range(root.right, r1, r2)

        # now fix the root if root is not in range
        # case 1: root.value < r1, delete root and return right subtree
        if root.value < r1:
            right_child = root.right
            self.delete(root, root.value)
            return right_child
        # case 2: if root.value > r2, delete root and return left subtree
        if root.value > r2:
            left_child = root.left
            self.delete(root, root.value)
            return left_child

        return root

    # delete an element
    def delete( self, root, item):
        if root is None:
            return False

        # if value to be deleted is less than root then the value lies in left subtree
        if item < root.value:
            root.left = self.delete(root.left, item)

        # if value to be deleted is greater than root then the value lies in right subtree
        elif item > root.value:
            root.right = self.delete(root.right, item)

        # else the value is same as root.value
        else:
            # case 1: node to be deleted has 1 child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp

            # case 2: node to be deleted has 2 children

            # get the inorder successor of root node
            temp = root.right
            while temp.left is not None:
                temp = temp.left

            smallest_value = temp
            # copy inorder successor node.value to this root.value
            root.value = smallest_value.value

            # delete the inorder successor
            root.right = self.delete(root.right, smallest_value.value)

        return root

    # tell inorder successor of given key in BST
    def inorder_successor( self, node ):
        if node is None: return

        # case 1: if node has right subtree then find least value node from that right subtree
        if node.right:
            temp = node.right
            while temp.left: temp = temp.left
            return temp

        # case 2: if node doesn't have right subtree
        # then search that node starting from root and the node from where we take the last left is the answer
        root = self.root
        store = None
        while root.value != node.value:
            if node.value < root.value:
                store = root
                root = root.left
            else: root = root.right
        return store

    # tell the predecessor of a node in BST
    def inorder_predecessor( self, node ):
        if node is None: return

        # case 1: if node has left subtree then find the max value node from that left subtree
        if node.left:
            temp = node.left
            while temp.right: temp = temp.right
            return temp

        # case 2: if node doesn't have left subtree
        # then search that node starting from root and the node from where we take the last right is the answer
        root = self.root
        store = None
        while root.value != node.value:
            if node.value > root.value:
                store = root
                root = root.right
            else: root = root.left
        return store

    # convert sorted singly linked list to height balanced BST
    cur = None

    def sorted_ll_to_bst( self, list_head ):
        if not list_head: return
        self.cur = list_head
        n = self.getSize_of_list(list_head)
        return self._sorted_ll_to_bst(n)

    def _sorted_ll_to_bst( self, list_size ):
        if list_size <= 0: return

        left = self._sorted_ll_to_bst(int(list_size/2))

        root = Node(self.cur.value)

        self.cur = self.cur.right

        right = self._sorted_ll_to_bst(list_size - int(list_size/2) -1)

        root.left = left
        root.right = right

        return root

    def getSize_of_list( self, head ):
        n = 0
        while head:
            head = head.right
            n += 1
        return n

    # check whether elements of 2 BSTs are same or not (order of elements doesn't matter)
    def check_elements_same_in_bsts( self, root1, root2 ):
        # base cases
        if not root1 and not root2: return True
        if (root2 and not root1) or (root1 and not root2): return False

        # create 2 sets and store elements in both bsts to it
        set1, set2 = set(), set()
        self._insert_to_set(root1, set1)
        self._insert_to_set(root2, set2)

        return (set1 == set2)

    def _insert_to_set( self, root, s ):
        if not root: return
        self._insert_to_set(root.left, s)
        s.add(root.value)
        self._insert_to_set(root.right, s)

    # convert BST to circular doubly linked list with space complexity(1)
    prev = None

    def bst_to_circular_doubly_linkedlist( self, root, head ):
        # initially, root points to root of the linked list and head is None

        if root is None: return

        # basically we are doing inorder traversal and inside we write steps for converting bst to dll

        self.bst_to_circular_doubly_linkedlist( root.left, head )

        if self.prev is None:
            head = root
        else:
            root.left = self.prev
            self.prev.right = root

        # make current node as prev node
        self.prev = root

        self.bst_to_circular_doubly_linkedlist( root.right, head )


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

print('In-order tree traversal:', end=' ')
bst.print()

print('\nTree sort in ascending order:', end=' ')
bst.tree_sort(bst.root)

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

print('shortest distance between two nodes:', str(bst.shortest_distance_between_two_nodes(bst.root, 200, 450)))

print('count of number of BSTs possible with n nodes:', str(bst.count_of_BST_possible(7)))

print('\nConvert sorted array to BST:', end=' ')
bst._print(bst.sorted_array_to_bst([70,60,50,40,30,20,10]))

print('\nFloor of given value:', bst.floor_of_given_value(bst.root, 810))
print('ceiling of given value:', bst.ceil_of_given_value(bst.root, 720))

print('Inorder successor of node:', str(bst.inorder_successor(bst.root).value))
print('Inorder predecessor of node:', str(bst.inorder_predecessor(bst.root).value))

print('Print all elements in the range r1 to r2 in increasing order:')
bst.print_all_in_range(bst.root, 100, 750)

print('\nRemove all elements outside the range:', end=' ')
bst._print(bst.remove_elements_outside_range(bst.root, 100, 750))

print('\nDelete a node in tree:', end=' ')
bst._print(bst.delete(bst.root, 500))

# 5->100->2050->10000
linked_list = Node(5)
linked_list.right = Node(100)
linked_list.right.right = Node(2050)
linked_list.right.right.right = Node(10000)
print('\nConvert sorted linked list to bst:',end = ' ')
bst._print(bst.sorted_ll_to_bst(linked_list))

print('\nCheck whether 2 BSTs have same set of elements', bst.check_elements_same_in_bsts(bst.root, bst.root))

# print('\nConvert BST to circular doubly linked list:', end='\n ')
# bst.bst_to_circular_doubly_linkedlist(bst.root, None)
