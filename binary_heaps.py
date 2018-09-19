class Binary_Heap(object):
    def __init__(self):
        # first element of heapList is zero for simpler integer division in later methods
        self.heap_list = [0]
        # keep track of current size of heap
        self.heap_size = 0

# minheap property - parent should always be less than or equal to each of its children

    # percolate up in minHeap
    def percolate_up_minheap(self, currentnode_index):

        # parent of current node = index of current node/ 2
        while (currentnode_index // 2) > 0:

            if self.heap_list[currentnode_index] < self.heap_list[currentnode_index // 2]:
                # swap
                self.heap_list[currentnode_index], self.heap_list[currentnode_index // 2] = \
                    self.heap_list[currentnode_index // 2], self.heap_list[currentnode_index]

            # move up to parent of current node
            currentnode_index = currentnode_index // 2

    # insert element in MinHeap
    def insert_minheap( self, value ):
        self.heap_list.append(value)
        self.heap_size += 1
        self.percolate_up_minheap(self.heap_size)

    # delete minimum element in MinHeap
    def delete_min_minheap( self ):
        # deleted value (root of minheap)
        return_value = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        self.heap_list.pop()
        self.percolate_down_minheap(1)

        return return_value

    # percolate down in minHeap
    def percolate_down_minheap( self, currentnode_index ):
        while (currentnode_index * 2) <= self.heap_size:
            minchild_index = self.minimum_child_index(currentnode_index)

            if self.heap_list[currentnode_index] > self.heap_list[minchild_index]:
                # swap
                self.heap_list[currentnode_index], self.heap_list[minchild_index] = \
                    self.heap_list[minchild_index], self.heap_list[currentnode_index]

            currentnode_index = minchild_index

    # get index of smallest value child
    def minimum_child_index( self, parent_index ):
        if parent_index * 2 + 1 > self.heap_size:
            return parent_index * 2
        elif self.heap_list[parent_index*2] < self.heap_list[parent_index*2 +1]:
            return parent_index*2
        else:
            return parent_index*2 + 1

    # build MinHeap from a given list of integers
    def build_minheap( self, alist ):
        index = len(alist) // 2
        self.heap_size = len(alist)
        self.heap_list = [0] + alist[:]
        while index > 0:
            self.percolate_down_minheap(index)
            index = index -1

    # get maximum element in MinHeap
    def get_max_in_minheap( self ):
        max = float('-inf')
        for e in self.heap_list:
            if e > max:
                max = e

        return max

    # delete an ith indexed element from MinHeap
    def delete_ith_index_minheap( self, i ):
        if i <= self.heap_size:
            return_value = self.heap_list[i]
            self.heap_list[i] = self.heap_list[self.heap_size]
            self.heap_size -= 1
            self.heap_list.pop()
            self.percolate_down_minheap(i)

            return return_value

        return

# maxheap property - parent should always be greater than or equal to each of its children

    # percolate up in maxheap
    def percolate_up_maxheap( self, currentnode_index ):
        # parent of current node = index of current node/ 2
        while currentnode_index // 2 > 0:
            if self.heap_list[currentnode_index] > self.heap_list[currentnode_index // 2]:
                self.heap_list[currentnode_index], self.heap_list[currentnode_index // 2] = \
                    self.heap_list[currentnode_index // 2], self.heap_list[currentnode_index]

            # move up to parent of current node
            currentnode_index = currentnode_index // 2

    # percolate down in maxheap
    def percolate_down_maxheap( self, currentnode_index ):
        while currentnode_index*2 <= self.heap_size:
            maxchild_index = self.maximum_child_index(currentnode_index)
            if self.heap_list[currentnode_index] < self.heap_list[maxchild_index]:
                self.heap_list[currentnode_index], self.heap_list[maxchild_index] = \
                    self.heap_list[maxchild_index], self.heap_list[currentnode_index]

            currentnode_index = maxchild_index

    # get index of largest value child
    def maximum_child_index( self, parent_index ):
        if parent_index * 2 + 1 > self.heap_size:
            return parent_index * 2
        elif self.heap_list[parent_index * 2 + 1] > self.heap_list[parent_index * 2]:
            return parent_index * 2 + 1
        else:
            return parent_index * 2

    # insert element in maxheap
    def insert_maxheap( self, value ):
        self.heap_list.append(value)
        self.heap_size += 1
        self.percolate_up_maxheap(self.heap_size)

    # delete max element in maxheap
    def delete_max_maxheap( self ):
        # deleted value = root of maxheap
        return_value = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        self.heap_list.pop()
        self.percolate_down_maxheap(1)

        return return_value

    # build MaxHeap with given list of integers - time complexity is O(n), not O(n logn)
    def build_maxheap( self, alist ):
        index = len(alist) // 2
        self.heap_size = len(alist)
        self.heap_list = [0] + alist[:]

        while index > 0:
            self.percolate_down_maxheap(index)
            index -= 1

    # heap sort in ascending order (using minheap)
    def heap_sort_ascending_order( self ):
        sorted_array = []
        index = 1
        while index != self.heap_size:
            sorted_array.append(self.heap_list[1])
            self.heap_list[1] = self.heap_list[self.heap_size]
            self.heap_size -= 1
            self.heap_list.pop()
            self.percolate_down_minheap(1)

        sorted_array.append(self.heap_list[self.heap_size])
        return sorted_array

    # find all elements less than k in binary heap
    def all_elements_less_than_k( self, k, position = 1):
        # make sure element exists
        if position >= self.heap_size:
            return

        # while doing pre-order traversal in minheap, if value of parent node >=k then its children will also be greater
        if self.heap_list[position] >= k:
            return

        print(self.heap_list[position], end=', ')

        # check in left child
        self.all_elements_less_than_k(k, position*2)

        # check in right child
        self.all_elements_less_than_k(k, position*2+1)

    # merge 2 binary maxHeaps , size of first heap = m+n size of second heap = n , complexity O(m+n)
    def merge_two_maxheaps( self, maxheap1, maxheap2 ):

        # copy all elements of heap2 to heap1 to be merged in next step
        maxheap1 += maxheap2[:]

        # build heap for the modified array of size m+n
        self.build_maxheap(maxheap1)

    # get kth smallest element in MinHeap, complexity O(n + klogn)
        # solution -- build minheap in O(n), extract root element k times and heapify in O(klogn)

    # get kth smallest element in MinHeap, complexity O(n)
        # solution -- use quick sort partition algorithm to partition around kth largest number

    # given a big file with million of numbers, how do you find 10 maximum numbers from that file
        # solution:
        # sort first 10 numbers in descending order and keep track of lowest number in list
        # if incoming number is greater than the lowest number then insert the new number in its place and sort the list again

    # merge k sorted lists with total n inputs altogether time complexity O(nk), space complexity O(1)

    # merge k sorted lists with total n inputs altogether time complexity O(nlogk), space complexity O(k) - using heaps

    # given 2 arrays A and B each with n elements, find largest n pairs (A[i],B[j])

    # min-max heap - structure that supports min and max in O(1) time, insert, deletemin, deletemax in O(logn) time

    # design heap data structure that supports finding the median in an infinite series of integers

    # maximum number in sliding window - brute force

    # maximum number in sliding winodw - using heap data structure

    # maximum number in sliding window - using double-ended-queue (perfect data structure for this problem)

    # merge(union) two binary heaps

    # find minimum window in inputString which will contain all chars in Pattern in complexity O(n).
    # if no such window, return empty string. If multiple such windows, return one unique minimum window

    # in maxHeap, check if kth largest item is >= x, runtime O(k)

    # Given k lists of sorted integers, find smallest range that includes atleast one number from each of k lists

# implement stack using heap
# meaning every new element is pushed with a key/priority higher than all current elements,
# so it will be popped before any of them
class stack_using_minheap(object):
    def __init__(self):
        # key - serves as priority to pushed value
        self.key = 0
        self.hp = Binary_Heap()

    # push (key, value) into the stack
    def push( self, value ):
        self.key += 1
        self.hp.heap_list.append((self.key, value))
        self.hp.heap_size += 1

    def pop( self ):
        if self.is_empty():
            return
        self.key -= 1
        self.hp.heap_list.pop()
        self.hp.heap_size -= 1

    def is_empty( self ):
        return self.hp.heap_size == 0

# implement queue using heap
class queue_using_minheap(object):
    def __init__(self):
        self.key = 0
        self.hp = Binary_Heap()

    def enqueue( self, value ):
        self.key += 1
        self.hp.heap_list.insert(0, (self.key, value))
        self.hp.heap_size += 1

    def dequeue( self ):
        if self.is_empty(): return
        self.key -= 1
        self.hp.heap_list.pop()
        self.hp.heap_size -= 1

    def is_empty( self ):
        return self.hp.heap_size == 0



# minHeap formed by insertion
#       10
#     /    \
#    20    100
#   /  \
# 200  500
minH = Binary_Heap()
minH.insert_minheap(100)
minH.insert_minheap(200)
minH.insert_minheap(10)
minH.insert_minheap(20)
minH.insert_minheap(500)
print('MinHeap is:', minH.heap_list)

# minHeap formed by input list
#      10
#     /  \
#    60  40
#   /  \
# 300  75
minH.build_minheap([40,60,10,300,75,1,200,300])
print('Build minHeap from given list of integers:', minH.heap_list)

minH.delete_min_minheap()
print('Delete minimum element in minHeap:', minH.heap_list)

print('maximum element in heap:', str(minH.get_max_in_minheap()))

print('All elements less than k in minheap:',end=' ')
minH.all_elements_less_than_k(200)

print('\nMinHeap is:', minH.heap_list)
print('Deleting ith indexed element from minHeap:', str(minH.delete_ith_index_minheap(4)),end=', ')
print('now MinHeap is:', minH.heap_list)

print('Sorted array in ascending order using minHeap:', minH.heap_sort_ascending_order())

# maxHeap formed by insertion
#       500
#     /    \
#    200    10
#   /  \
# 20  100
maxH = Binary_Heap()
maxH.insert_maxheap(100)
maxH.insert_maxheap(200)
maxH.insert_maxheap(10)
maxH.insert_maxheap(20)
maxH.insert_maxheap(500)
mx1 = maxH.heap_list
print('MaxHeap is:', mx1)

# maxHeap formed by input list
#      10
#     /  \
#    60  40
#   /  \
# 300  75
maxH.build_maxheap([40,60,10,300,75])
mx2 = maxH.heap_list
print('Build maxHeap from given list of integers:', mx2)

maxH.merge_two_maxheaps(mx1[1:], mx2[1:])
mx3 = maxH.heap_list
print('Merge two maxheaps:', mx3)

stack = stack_using_minheap()
stack.push(20)
stack.push(10)
stack.push(50)
print('Stack implemented using minheap:', stack.hp.heap_list)

queue = queue_using_minheap()
queue.enqueue(10)
queue.enqueue(22)
queue.enqueue(45)
print('Queue implemented using minheap:', queue.hp.heap_list)