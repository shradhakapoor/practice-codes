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

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    # Inorder traversal
    def print_tree( self ):
        if self.root is not None:
            print('Inorder Traversal:'+ str(self._print_tree(self.root)))

    def _print_tree( self, cur_node ):
        if cur_node is not None:
            # inorder traversal
            self._print_tree(cur_node.left)
            print(str(cur_node.value), end='-')
            self._print_tree(cur_node.right)

    # level-order traversal
    def level_order_traversal( self, node ):
        if node is None:
            return
        queue = Queue()
        queue.enqueue(node)
        traversal = ''
        while len(queue.items) > 0:
            traversal += str(queue.items[-1].value) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        print('Level order traversal: '+traversal)

    # find maximum element(with recursion)
    def maximum_element_with_recursion( self ):
        if self.root is None:
            print('Tree doesn\'t exist!')
        else:
            print('Maximum element recursively is: '+str(self._max_element_with_recursion(self.root)))

    max_elem = float('-inf')
    def _max_element_with_recursion( self, node ):
        if node:
            if node.value > self.max_elem:
                self.max_elem = node.value
                self._max_element_with_recursion(node.left)
                self._max_element_with_recursion(node.right)
            return self.max_elem

    # find maximum element(without recursion, using level-order traversal)
    def maximum_element_without_recursion( self ):
        if self.root is None:
            return
        max = float("-inf")
        node = self.root
        queue = Queue()

        queue.enqueue(node)
        while len(queue.items) > 0:
            if max < queue.items[-1].value:
                max = queue.items[-1].value
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        print ('Maximum element iteratively is :' + str(max))

    # search an element(with recursion)
    # def search_element_with_recursion( self, element ):
    #     if self.root is None or element is None:
    #         return('Sorry, not found in this tree')
    #     else:
    #         return('Found'+ str(self._search_element_with_recursion(self.root, element)))
    #
    # def _search_element_with_recursion( self, node, element ):
    #     if node:
    #         if element == node.value:
    #             return node.value
    #         else:
    #             self._search_element_with_recursion(node.left, element)
    #             self._search_element_with_recursion(node.right, element)

    # search an element(without recursion)
    def search_element_without_recursion( self, element ):
        if self.root is None or element is None:
            return('Sorry, not found in this tree')
        queue = Queue()
        node = self.root
        queue.enqueue(node)
        node_counter = 1

        while len(queue.items) > 0:
            if element == queue.items[-1].value:
                return('Found at node number ' + str(node_counter))
            node = queue.dequeue()
            node_counter+=1

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return ('Sorry, not found in this tree')

    # insert an element

    # find size of tree(with recursion)

    # find size of tree(without recursion)

    # print tree in reverse-order( from leaves to root) using level-order

    # delete the tree

    # delete a given element in tree

    # height/depth of node(with recursion)
    def height_with_recursion( self, node ):
        if node is None:
            return 0
        return 1 + max( self.height_with_recursion( node.left ), self.height_with_recursion( node.right ) )

    # height/depth of node(without recursion)
    def height_without_recursion( self, node ):
        if node is None:
            return 0
        queue = Queue()
        queue.enqueue(node)
        height = 0

        while True:
            # number of nodes at current level
            node_count = len(queue.items)

            if node_count == 0:
                return height
            height+=1
            # dequeue current level, enqueue next level
            while node_count > 0:
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
                node_count-=1

    # find deepest node of tree

    # find number of leaves(without recursion)

    # find number of full nodes(without recursion)

    # find number of half nodes(nodes with one child only)(without recursion)

    # structurally identical trees, return true

    # diameter/width of tree

    # find level with maximum sum

    # print all root-to-leaf paths

    # maximum path sum (from any start-to-end path)

    # check the existence of path with given sum

    # convert tree to its mirror

    # least common ancestor of two nodes

    # construct binary tree from inorder and preorder traversals

    # find all ancestors of a node

    # zigzag tree traversal







#       110
#      /   \
#   200      30
#  /  \     /
# 140  50   6

tree = BinaryTree(110)
tree.root.left = Node(200)
tree.root.right = Node(30)
tree.root.left.left = Node(140)
tree.root.left.right = Node(50)
tree.root.right.left = Node(6)
tree.print_tree()
print('')
tree.level_order_traversal(tree.root)
tree.maximum_element_without_recursion()
tree.maximum_element_with_recursion()
print(tree.search_element_without_recursion(140))
#print(tree.search_element_with_recursion(140))
print('Height of tree, recursively calculated: '+ str(tree.height_with_recursion(tree.root.left)))
print('Height of tree, iteratively calculated: '+ str(tree.height_without_recursion(tree.root.right)))
