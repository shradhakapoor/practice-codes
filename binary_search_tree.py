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
        self.node = Node(value)

    # insert element
    def insert( self, value ):
        if self.node is None:
            self.node = Node(value)
        else:
            self._insert(self.node, value)

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
        else: #if value == node.value: add the value as a list to this node.value
            print('Value already in tree')

    # print tree-- Inorder traversal
    def print( self ):
        if self.node is None:
            return
        return(self._print(self.node))

    def _print( self, node ):
        if node is None:
            return
        if node.left:
            self._print( node.left )
        print(node.value, end=' ')
        if node.right:
            self._print(node.right)

    # Tree sorting
    def tree_sort(self, node):
        # Using recursion
        # print elements in inorder traversal

        # using iteration
        stack = Stack()
        done = 0
        curr = node

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
        if item is None or self.node is None:
            return False
        return self._search_with_recursion(self.node, item)

    def _search_with_recursion( self, node, item ):
        if node is None:
            return False
        elif node.value == item:
            return True
        elif item < node.value:
            return self._search_with_recursion(node.left, item)
        else:
            return self._search_with_recursion(node.right, item)

    # find an element, iteratively
    def search_with_iteration( self, item ):
        if item is None or self.node is None:
            return False
        node = self.node
        while node:
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
        if self.node is None:
            print('Tree doesn\'t exist!')
        else:
            print('Maximum element recursively is: '+str(self._max_element_with_recursion(self.node)))

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
        if node.right and self.minimum_element_with_iteration(node.right) < node.value:
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
        if self.node is None or k is None:
            return
        stack = Stack()
        return self._kth_smallest_element(self.node, stack).items[k-1]

    def _kth_smallest_element( self, node, stack ):
        # inorder traversal to store the elements of bst in sorted order
        if node:
            self._kth_smallest_element(node.left, stack)
            stack.push(node.value)
            self._kth_smallest_element(node.right, stack)

        return stack

    # given 2 nodes, find the lowest common ancestor in BST
    def lowest_common_ancestor( self, node, value1, value2 ):
        if node is None:
            return
        if node.value > max(value1, value2):
            return self.lowest_common_ancestor(node.left, value1, value2)
        elif node.value < min(value1, value2):
            return self.lowest_common_ancestor(node.right, value1, value2)
        else:
            return node

    # find shortest distance between 2 nodes
    def shortest_distance_between_two_nodes( self,node, value1, value2 ):
        if node is None:
            return 0
        if node.value > max(value1, value2):
            return self.shortest_distance_between_two_nodes(node.left, value1, value2)
        if node.value < min(value1, value2):
            return self.shortest_distance_between_two_nodes(node.right, value1, value2)
        if value1 <= node.value <= value2 or value2 <= node.value <= value1:
            return self.distance_from_node(node, value1) + self.distance_from_node(node, value2)

    def distance_from_node( self, node, value ):
        if node.value == value:
            return 0
        elif node.value > value:
            return 1+ self.distance_from_node(node.left, value)
        else:
            return 1+ self.distance_from_node(node.right, value)

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
            node = Node(arr[0])
            return node
        mid = len(arr)//2
        node = Node(arr[mid])

        if arr[mid-1] < arr[mid+1]:
            arr1 = arr[0:mid]
            arr2 = arr[(mid+1):]
        else:
            arr1 = arr[(mid + 1):]
            arr2 = arr[0:mid]

        node.left = self.sorted_array_to_bst(arr1)
        node.right = self.sorted_array_to_bst(arr2)

        return node

    # find floor of given data (largest data <= given data)
    def floor_of_given_value( self, node, value ):
        if node is None:
            return -1
        if node.value == value: return node.value

        # if node.value > value, then floor would be in left subtree
        if node.value > value:
            if node.left: return self.floor_of_given_value(node.left, value)

        # if node.value < value then floor is either the node or in right subtree
        if node.right:
            right_value = self.floor_of_given_value(node.right, value)
            return right_value if right_value <= value else node.value

        return node.value

    # find ceiling of given data (smallest data > given data)
    def ceil_of_given_value( self, node, value ):
        if node is None:
            return -1

        # equal to key value
        if value == node.value: return node.value

        # if node.value < value, ceil must be in right subtree
        if node.value < value:
            if node.right: return  self.ceil_of_given_value(node.right, value)

        # if node.value > value, ceil is either node.value or in left subtree
        if node.left:
            left_value = self.ceil_of_given_value(node.left, value)
            return left_value if left_value >= value else node.value

        return node.value

    # print all elements in increasing order in range r1 to r2
    def print_all_in_range( self, node, r1, r2 ):
        if node is None:
            return

        # since desired output is sorted, recurse for left subtree first
        # if node.value > r1 only then we can get elements in left subtree
        if r1 < node.value:
            self.print_all_in_range(node.left, r1, r2)

        if r1 <= node.value <= r2:
            print (node.value, end=', ')

        # if r2 > node.value only then we can get elements in right subtree
        if r2 > node.value:
            self.print_all_in_range(node.right, r1, r2)

    # remove BST elements outside the given range, and modified tree should also be BST
    def remove_elements_outside_range( self, node, r1, r2 ):
        if node is None: return

        # basically we need to fix the tree in post-order fashion
        node.left = self.remove_elements_outside_range(node.left, r1, r2)
        node.right = self.remove_elements_outside_range(node.right, r1, r2)

        # now fix the node if node is not in range
        # case 1: node.value < r1, delete node and return right subtree
        if node.value < r1:
            right_child = node.right
            self.delete(node, node.value)
            return right_child
        # case 2: if node.value > r2, delete node and return left subtree
        if node.value > r2:
            left_child = node.left
            self.delete(node, node.value)
            return left_child

        return node

    # delete an element
    def delete( self, node, item):
        if node is None:
            return False

        # if value to be deleted is less than node then the value lies in left subtree
        if item < node.value:
            node.left = self.delete(node.left, item)

        # if value to be deleted is greater than node then the value lies in right subtree
        elif item > node.value:
            node.right = self.delete(node.right, item)

        # else the value is same as node.value
        else:
            # case 1: node to be deleted has 1 child or no child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # case 2: node to be deleted has 2 children

            # get the inorder successor of node node
            temp = node.right
            while temp.left is not None:
                temp = temp.left

            smallest_value = temp
            # copy inorder successor node.value to this node.value
            node.value = smallest_value.value

            # delete the inorder successor
            node.right = self.delete(node.right, smallest_value.value)

        return node

    # tell inorder successor of given key in BST
    def inorder_successor( self, node ):
        if node is None: return

        # case 1: if node has right subtree then find least value node from that right subtree
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left

            return temp

        # case 2: if node doesn't have right subtree
        # then search that node starting from node and the node from where we take the last left is the answer
        tmp = self.node
        parent = None
        while tmp.value != node.value:
            if tmp.value > node.value:
                parent = tmp
                tmp = tmp.left
            else:
                tmp = tmp.right
        return parent

    # tell the predecessor of a node in BST
    def inorder_predecessor( self, node ):
        if node is None: return

        # case 1: if node has left subtree then find the max value node from that left subtree
        if node.left:
            temp = node.left
            while temp.right:
                temp = temp.right

            return temp

        # case 2: if node doesn't have left subtree
        # then search that node starting from node and the node from where we take the last right is the answer
        node = self.node
        parent = None
        while node.value != node.value:
            if node.value > node.value:
                parent = node
                node = node.right
            else:
                node = node.left
        return parent

    # convert sorted singly linked list to height balanced BST
    cur = None

    def sorted_ll_to_bst( self, list_head ):
        if not list_head: return
        self.cur = list_head
        n = self.getSize_of_list(list_head)
        return self._sorted_ll_to_bst(n)

    def _sorted_ll_to_bst( self, list_size ):
        if list_size <= 0: return

        left = self._sorted_ll_to_bst(list_size//2)

        node = Node(self.cur.value)

        self.cur = self.cur.right # traversing the linked list, cur = cur.next

        right = self._sorted_ll_to_bst(list_size - int(list_size/2) -1)

        node.left = left
        node.right = right

        return node

    def getSize_of_list( self, head ):
        n = 0
        while head:
            head = head.right
            n += 1
        return n

    # check whether elements of 2 BSTs are same or not (order of elements doesn't matter)
    def check_elements_same_in_bsts( self, node1, node2 ):
        # base cases
        if not node1 and not node2: return True
        if (node2 and not node1) or (node1 and not node2): return False

        # create 2 sets and store elements in both bsts to it
        set1, set2 = set(), set()
        self._insert_to_set(node1, set1)
        self._insert_to_set(node2, set2)

        return set1 == set2

    def _insert_to_set( self, node, s ):
        if not node: return
        self._insert_to_set(node.left, s)
        s.add(node.value)
        self._insert_to_set(node.right, s)

    # convert BST to circular doubly linked list with space complexity(1)
    prev = None

    def bst_to_circular_doubly_linkedlist( self, node, head ):
        # initially, node points to node of the linked list and head is None

        if node is None: return

        # basically we are doing inorder traversal and inside we write steps for converting bst to dll

        self.bst_to_circular_doubly_linkedlist( node.left, head )

        if self.prev is None:
            head = node
        else:
            node.left = self.prev
            self.prev.right = node

        # make current node as prev node
        self.prev = node

        self.bst_to_circular_doubly_linkedlist( node.right, head )


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
bst.tree_sort(bst.node)

print('\nSearch an item recursively: ', str(bst.search_with_recursion(700)))
print('Search an item iteratively: ', str(bst.search_with_iteration(700)))

print('height of tree:', str(bst.height(bst.node)))

print('Minimum element in tree(iteratively):', str(bst.minimum_element_with_iteration(bst.node)))

# binary tree
#       110
#      /   \
#   200      30
#  /  \     /
# 140  50   6
tree = binary_tree.BinaryTree(310)
tree.node.left = Node(200)
tree.node.right = Node(400)
tree.node.left.left = Node(140)
tree.node.left.right = Node(250)
tree.node.right.left = Node(350)
print('Binary tree', end = ' ')
tree.print_tree()
print('\nIs this binary tree a bst?(non-effecient solution):', str(bst.check_binarytree_is_bst(tree.node)))
print('Is this binary tree a bst?(effecient solution):', str(bst.check_binarytree_is_bst_effeciently(tree.node)))

print('kth smallest element in tree:', str(bst.kth_smallest_element(2)))

print('lowest common ancestor of two nodes:', str(bst.lowest_common_ancestor(bst.node, 700, 900).value))

print('shortest distance between two nodes:', str(bst.shortest_distance_between_two_nodes(bst.node, 200, 800)))

print('count of number of BSTs possible with n nodes:', str(bst.count_of_BST_possible(7)))

print('\nConvert sorted array to BST:', end=' ')
bst._print(bst.sorted_array_to_bst([70,60,50,40,30,20,10]))

print('\nFloor of given value:', bst.floor_of_given_value(bst.node, 810))
print('ceiling of given value:', bst.ceil_of_given_value(bst.node, 720))

print('Inorder successor of node:', str(bst.inorder_successor(bst.node).value))
print('Inorder predecessor of node:', str(bst.inorder_predecessor(bst.node).value))

print('Print all elements in the range r1 to r2 in increasing order:')
bst.print_all_in_range(bst.node, 100, 900)

print('\nRemove all elements outside the range:', end=' ')
bst._print(bst.remove_elements_outside_range(bst.node, 100, 750))

print('\nDelete a node in tree:', end=' ')
bst._print(bst.delete(bst.node, 500))

# 5->100->2050->10000
linked_list = Node(5)
linked_list.right = Node(100)
linked_list.right.right = Node(2050)
linked_list.right.right.right = Node(10000)
print('\nConvert sorted linked list to bst:',end = ' ')
bst._print(bst.sorted_ll_to_bst(linked_list))

print('\nCheck whether 2 BSTs have same set of elements', bst.check_elements_same_in_bsts(bst.node, bst.node))

# print('\nConvert BST to circular doubly linked list:', end='\n ')
# bst.bst_to_circular_doubly_linkedlist(bst.node, None)
