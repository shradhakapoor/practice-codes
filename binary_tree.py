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

    def push( self, item ):
        self.items.append(item)

    def pop( self ):
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
            print('Inorder Traversal:', end=' ')
            self._print_tree(self.root)

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
    def insert_node( self, value ):
        newNode = None
        if value:
            newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        queue= Queue()
        queue.enqueue(self.root)

        while len(queue.items) > 0:
            node = queue.dequeue()
            if node.left is None:
                node.left = newNode
                break
            else:
                queue.enqueue(node.left)
            if node.right is None:
                node.right = newNode
                break
            else:
                queue.enqueue(node.right)
        return

    # find size of tree(with recursion)
    def size_with_recursion( self, node):
        if node is None:
            return 0
        return 1 + (self.size_with_recursion(node.left)) + (self.size_with_recursion(node.right))

    # find size of tree(without recursion)
    def size_without_recursion( self, node ):
        if node is None:
            return 0
        queue = Queue()
        queue.enqueue(node)
        size = 0

        while len(queue.items) > 0:
            node = queue.dequeue()
            size+=1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return size

    # print tree in reverse-order( from leaves to root) using level-order
    def reverse_tree( self, n):
        if n is None:
            return
        stack = Stack()
        stack.push(n)

        while len(stack.items) > 0:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

        return n

    # delete the tree
    def delete_tree( self ):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            node.value = None

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


    # delete a given element in tree
    def delete_node( self, item ):
        if self.root is None or item is None:
            return
        last_node = self.deepest_node()

        if self.root.value == item:
            self.root.value = last_node.value
            self.deepest_node().value = None
            return 1

        queue= Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            if node.value == item:
                node.value = last_node.value
                self.deepest_node().value = None
                return 1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return 0

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
    def deepest_node( self ):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        node = None

        while not queue.is_empty():
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return node

    # find number of leaves(without recursion)
    def number_of_leaves( self ):
        if self.root is None:
            return 0
        queue = Queue()
        queue.enqueue(self.root)
        leaves_count = 0

        while not queue.is_empty():
            node = queue.dequeue()
            if not node.left and not node.right:
                leaves_count+=1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return leaves_count

    # find number of full nodes(without recursion)
    def number_of_fullnodes( self ):
        if self.root is None:
            return 0
        queue = Queue()
        queue.enqueue(self.root)
        fullnodes_count = 0

        while not queue.is_empty():
            node = queue.dequeue()
            if node.left and node.right:
                fullnodes_count+=1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return fullnodes_count

    # find number of half nodes(nodes with one child only)(without recursion)
    def number_of_halfnodes( self ):
        if self.root is None:
            return 0
        queue = Queue()
        queue.enqueue(self.root)
        halfnodes_count = 0

        while not queue.is_empty():
            node = queue.dequeue()
            if (node.left and not node.right) or (node.right and not node.left):
                halfnodes_count+=1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return halfnodes_count

    # structurally identical trees, return true
    def structurally_identical( self, root1, root2 ):
        if root1 is root2 is None:
            return True

        if root1 and root2:
            return(root1.value == root2.value
                   and self.structurally_identical(root1.left, root2.left)
                   and self.structurally_identical(root1.right, root2.right))

        return False

    # find level with maximum sum
    def level_with_maximum_sum( self ):
        if self.root is not None:
            queue = Queue()
            current_level_list, max_level_list = [], []
            current_level_sum, max_sum = 0, float('-inf')
            marker_node = Node(float('-inf'))

            queue.enqueue( self.root )
            queue.enqueue(marker_node)

            while not queue.is_empty():
                node = queue.dequeue()

                # if all nodes of this level are traversed
                if node == marker_node:
                    if max_sum < current_level_sum:
                        max_sum = current_level_sum
                        max_level_list.clear()
                        max_level_list = current_level_list.copy()

                    current_level_sum = 0
                    current_level_list.clear()

                    # add marker_node only when queue has some element
                    if not queue.is_empty():
                        queue.enqueue(marker_node)

                # else traverse all nodes of this level
                else:
                    current_level_sum += node.value
                    current_level_list.append(node)
                    if node.left:
                        queue.enqueue(node.left)
                    if node.right:
                        queue.enqueue(node.right)

            max_string = ''
            for n in max_level_list:
                max_string += str(n.value) + '-'
            print( 'Maximum sum level is: ' + max_string)
            print ('sum of this level is: ' + str(max_sum))

    # print all root-to-leaf paths
    def paths_root_to_leaf( self ):
        if self.root is None:
            return
        path, result = Stack(), []
        self._paths_root_to_leaf(self.root, path, result)
        return result

    def _paths_root_to_leaf( self, node, path, result ):
        if node is None:
            return

        # for leaf node, form a string with all nodes' value from root to the leaf path
        if node.left is node.right is None:
            ans = ''
            for p in path.items:
                ans += str(p.value)+ '-'
            ans+= str(node.value)
            result.append(ans)

        if node.left:
            path.push(node)
            self._paths_root_to_leaf(node.left, path, result)
            path.pop()

        if node.right:
            path.push(node)
            self._paths_root_to_leaf(node.right, path, result)
            path.pop()

    # maximum path sum
    def maximum_path_sum( self ):
        if self.root is None:
            return
        path, result = Stack(), []
        self._maximum_path_sum(self.root, path, result)
        return max(result)

    def _maximum_path_sum( self, node, path, result ):
        if node is None:
            return
        if node.left is node.right is None:
            sum = node.value
            for p in path.items:
                sum += p.value
            result.append(sum)

        if node.left:
            path.push(node)
            self._maximum_path_sum(node.left, path, result)
            path.pop()

        if node.right:
            path.push(node)
            self._maximum_path_sum(node.right, path, result)
            path.pop()

    # check the existence of path with given sum
    def path_existence_with_sum(self, sum):
        if self.root is sum is None:
            return
        path = Stack()
        return self._path_existence_with_sum(self.root, path, sum)

    def _path_existence_with_sum(self, node, path, sum):
        if node is None:
            return False
        if node.left is node.right is None:
            s = sum
            for p in path.items:
                s -= p.value
            s -= node.value
            if s == 0:
                return True

        if node.left:
            path.push(node)
            self._path_existence_with_sum(node.left, path, sum)
            path.pop()

        if node.right:
            path.push(node)
            self._path_existence_with_sum(node.right, path, sum)
            path.pop()

        return False

    # convert tree to its mirror
    def tree_mirror( self, node ):
        if node is None:
            return
        self.tree_mirror(node.left)
        self.tree_mirror(node.right)
        node.left, node.right = node.right, node.left

    # least common ancestor of two nodes

    # construct binary tree from inorder and preorder traversals

    # find all ancestors of a node

    # zigzag tree traversal

    # diameter/width of tree



#       110
#      /   \
#   200      30
#  /  \     /  \\
# 140  50   6  32
#  //
# 1

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

tree.insert_node(32)
tree.insert_node(1)
print('inserting node 32...')
tree.print_tree()
print('')

print('size of tree, recursively: '+ str(tree.size_with_recursion(tree.root)))
print('size of tree, iteratively: '+ str(tree.size_without_recursion(tree.root)))

print('Deepest node value: '+ str(tree.deepest_node().value))

print('Number of leaves: '+ str(tree.number_of_leaves()))

print('Number of Full nodes: '+ str(tree.number_of_fullnodes()))

print('Number of Half nodes: '+ str(tree.number_of_halfnodes()))

print('Paths from root to leaf:' + str(tree.paths_root_to_leaf()))

tree2 = BinaryTree(110)
tree2.insert_node(200)
tree2.insert_node(30)
tree2.insert_node(140)
tree2.insert_node(50)
tree2.insert_node(6)
tree2.insert_node(32)
tree2.insert_node(1)
if tree.structurally_identical(tree.root, tree2.root ):
    print('Trees are structurally identical')
else:
    print('Trees are not structurally identical')

# tree.level_with_maximum_sum()
# print('Maximum sum among all paths is: '+ str(tree.maximum_path_sum()))

print('Existence of path with given sum: '+ str(tree.path_existence_with_sum(451)))

tree.tree_mirror(tree.root)
print('Mirror of tree ...')
tree.print_tree()
print('')

print('Reversing the tree ...')
tree.reverse_tree(tree.root)
tree.print_tree()
print('')

if tree.delete_node(32):
    print('success to delete')
    tree.print_tree()
    print('')
else:
    print('Item not found in tree')

print('deleting tree ...')
tree.delete_tree()
tree.print_tree()
print('')