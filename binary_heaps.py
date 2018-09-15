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
        if i <= self.heap_size-1:
            return self.heap_list.pop(i)
        else:
            return

    # build MaxHeap

    # insert an element in MaxHeap

    # delete an arbitrary element from MinHeap

    # heap sort

    # find all elements less than k in binary heap

    # merge 2 binary maxHeaps , size of first heap = m+n size of second heap = n , complexity O(m+n.log(m+n))

    # merge 2 binary maxHeaps , size of first heap = m+n size of second heap = n , complexity O(m+n)

    # get kth smallest element in MinHeap, complexity O(klogn)

    # get kth smallest element in MinHeap, complexity O(n)

    # get k max elements from maxHeap

    # implement stack using heap

    # implement queue using heap

    # given a big file with million of numbers, how do you find 10 maximum numbers from that file

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
minH.build_minheap([40,60,10,300,75])
print('Build minHeap from given list of integers:', minH.heap_list)

minH.delete_min_minheap()
print('Delete minimum element in minHeap:', minH.heap_list)

print('maximum element in heap:', str(minH.get_max_in_minheap()))

print('Deleting ith indexed element from minHeap:', str(minH.delete_ith_index_minheap(1)))
