class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def print_tree( self ):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree( self, cur_node ):
        if cur_node is not None:
            # inorder traversal
            self._print_tree(cur_node.left)
            print(str(cur_node.value), end=', ')
            self._print_tree(cur_node.right)

    # level-order traversal

    # find maximum element(with recursion)

    # find maximum element(without recursion, using level-order traversal)

    # search an element(with recursion)

    # search an element(without recursion)

    # insert an element

    # find size of tree(with recursion)

    # find size of tree(without recursion)

    # print tree in reverse-order( from leaves to root) using level-order

    # delete the tree

    # delete a given element in tree

    # height/depth of tree(with recursion)

    # height/depth of tree(without recursion)

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







#       10
#      /   \
#   20      30
#  /  \     /
# 40  50   60

tree = BinaryTree(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)
tree.root.right.left = Node(60)
tree.print_tree()

