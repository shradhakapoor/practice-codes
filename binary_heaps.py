from collections import *


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

    # in maxHeap, check if kth largest item is >= x, runtime O(k)

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

    # merge 2 binary maxHeaps , time O(m + n) -- needed to build heap from array of m+n elements
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

    def merge_2_sorted_lists( self, list1, list2 ):
        n = len(list2)
        m = len(list1)
        # iterate through all elements of list2, starting from the last element
        for i in range(n-1, -1, -1):
            # find the smallest element in list1 that is greater than list2[i].
            # move all elements one position ahead till smallest element is not found
            last = list1[m-1]
            j = m - 2
            while j >= 0 and list1[j] > list2[i]:
                list1[j+1] = list1[j]
                j -= 1

            # if there is a greater element
            if j!= m-2 or last > list2[i]:
                list1[j+1] = list2[i]
                list2[i] = last

    # given 2 arrays A and B each with n elements, find largest n pairs (A[i],B[j])
    def largest_pairs_in_arrays( self, array1, array2 ):
        n = len(array1)
        result = list()

        maxheap1, maxheap2 = Binary_Heap(), Binary_Heap()
        maxheap1.build_maxheap( array1 )
        maxheap2.build_maxheap( array2 )
        while maxheap1.heap_size != 0:
            result.append([maxheap1.delete_max_maxheap(), maxheap2.delete_max_maxheap()])

        return result

    # min-max heap - structure that supports min and max in O(1) time, insert, deletemin, deletemax in O(logn) time
        # solution: all operations of minheap and maxheap

    # find the running median in an infinite series of integers, recommended time O(n.logn) using heaps
    def median_in_running_stream( self, input_stream):
        maxheap_lo = Binary_Heap()
        minheap_hi = Binary_Heap()
        medians = []
        for i in range(len(input_stream)):
            number = input_stream[i]
            self.addNumber(number, maxheap_lo, minheap_hi)
            self.rebalance(maxheap_lo, minheap_hi)
            medians.append(self.get_median(maxheap_lo, minheap_hi))

        return medians

    # add the incoming number to left or right side
    def addNumber(self, number, maxheap_lo, minheap_hi):
        if maxheap_lo.heap_size == 0 or number < maxheap_lo.heap_list[1]:
            maxheap_lo.insert_maxheap(number)
        else:
            minheap_hi.insert_minheap(number)

    # compare sizes of two heaps and rebalance them
    def rebalance(self, maxheap_lo, minheap_hi):
        bigger_size_heap = maxheap_lo if maxheap_lo.heap_size > minheap_hi.heap_size else minheap_hi
        smaller_size_heap = maxheap_lo if maxheap_lo.heap_size < minheap_hi.heap_size else minheap_hi

        # if heaps have element difference by 2 or more then transfer the element from bigger size heap to smaller one
        if bigger_size_heap.heap_size - smaller_size_heap.heap_size >= 2:
            smaller_size_heap.insert_maxheap(bigger_size_heap.heap_list[1]) if smaller_size_heap == maxheap_lo \
                else smaller_size_heap.insert_minheap(bigger_size_heap.heap_list[1])

    # compute the median
    def get_median(self, maxheap_lo, minheap_hi):
        bigger_size_heap = maxheap_lo if maxheap_lo.heap_size > minheap_hi.heap_size else minheap_hi
        smaller_size_heap = maxheap_lo if maxheap_lo.heap_size < minheap_hi.heap_size else minheap_hi

        if bigger_size_heap.heap_size == smaller_size_heap.heap_size:
            return float(bigger_size_heap.heap_list[1] + smaller_size_heap.heap_list[1] / 2)
        else:
            return bigger_size_heap.heap_list[1]

    # maximum number in sliding window - brute force O(nk)

    # maximum number in sliding window - using BST time O(n.logk)

    # maximum number in sliding window - using double-ended-queue (perfect data structure for this problem) time O(n)
    def max_in_sliding_window_DEqueue( self, input_array, k ):
        # deQ will store useful indexes of array elements in every window and
        # it will maintain decreasing order from front to rear
        deQ = deque()
        n = len(input_array)
        result = []

        # process first window of input_array, find max in it
        for i in range(k):
            # for every element, previous smaller elements are useless, so remove them from deQ
            while deQ and input_array[i] >= input_array[deQ[-1]]:
                deQ.pop()

            # now add the input_array[i] to rear of deQ
            deQ.append(i)

        # process rest of the elements from k to n-1
        for i in range(k, n):
            # element at front of deQ is max from previous window
            result.append(input_array[deQ[0]])

            # remove the elements which are out of this window
            while deQ and deQ[0] <= i-k:
                # remove from front of deQ
                deQ.popleft()

            # for every element, previous smaller elements are useless, so remove them from deQ
            while deQ and input_array[i] >= input_array[deQ[-1]]:
                deQ.pop()

            # now add the input_array[i] to rear of deQ
            deQ.append( i )

        result.append(input_array[deQ[0]])

        return result

    # find minimum window in inputString which will contain all chars in Pattern in complexity O(n).
    # if no such window, return empty string. If multiple such windows, return one unique minimum window
    def find_min_window_for_substring( self, input_str, pattern ):

        # count occurence of chars in pattern
        # defaultdict will return int 0 if key is not present
        pattern_count_dict = defaultdict(int)
        for ch in pattern:
            pattern_count_dict[ch] += 1

        remain_missing = len( pattern )
        start_pos, end_pos = 0, float( 'inf' )
        current_start = 0

        # Enumerate function makes current_end indexes from 1
        for current_end, ch in enumerate( input_str, 1 ):
            # Whenever we encounter a character, no matter ch in pattern or not, we minus 1 in count dictionary
            # But, only when ch is in pattern, we minus the length of remain_missing
            # When the remain_missing is 0, we find a potential solution.
            if pattern_count_dict[ch] > 0:
                remain_missing -= 1
            pattern_count_dict[ch] -= 1

            if remain_missing == 0:
                # Remove redundant character
                # Try to find the fist position in input_str that makes pattern_count_dict value equals 0
                # Which means we can't skip this character in input_str when returning answer
                while pattern_count_dict[input_str[current_start]] < 0:
                    pattern_count_dict[input_str[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end

                # We need to add 1 to current_start, and the correspondence value in dictionary, is because
                # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
                # We can remove this currently first character to try to find a shorter answer.
                pattern_count_dict[input_str[current_start]] += 1
                remain_missing += 1
                current_start += 1

        return input_str[start_pos:end_pos] if end_pos != float( 'inf' ) else ''

    # Given k lists of sorted integers, find smallest range that includes atleast one number from each of k lists
    # def shortest_range_in_k_sorted_lists( self, input, k ):
    #     max = float('inf')
    #     lst = [0] * k
    #     # create a minheap with k heap nodes, each heapnode has first element of list
    #     for i in range(k):
    #         # storing (first element of list, index of list, index of next element to be stored from list)
    #         lst.append([input[i][0], i, 1])
    #
    #         # store max element
    #         if lst[i] > max:
    #             max = lst[i]
    #
    #     # create the minheap of this list of firsrt elements of each list
    #     minH = Binary_Heap()
    #     minH.build_minheap(lst)
    #
    #     # now one by one get the minimum element from minheap and replace it with next element of its list
    #     while True:
    #         # Get the minimum element and store it in output
    #         # update min value
    #         # update range
    #             # if (range > max - min + 1)
    #             #     {
    #             #         range = max - min + 1;
    #             #     start = min;
    #             #     end = max;
    #             #     }
    #         # replace the current root with next element from same list as current root. we have stored the indices of list and next element in list
    #             # if (root.j < N)
    #             #     {
    #             #         root.element = arr[root.i][root.j];
    #             #     root.j += 1;
    #             #
    #             #     // update max element
    #             #     if (root.element > max)
    #             #     max = root.element;
    #             #     }
    #         # break if we have reached end of any list
    #         # Replace root with next element of list


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

# merge k sorted(increasing order) arrays with total n inputs altogether time complexity O(nk), space complexity O(1)

# merge k sorted arrays with total n inputs altogether time complexity O(nlogk), space complexity O(k) - using minheap
def merge_k_sorted_arrays_minheap( self, arrays, n, k ):
    output = []

    # create minheap with k heap nodes. Each heap node has first element of an array
    min_hp = Binary_Heap()
    for i in range(k):
        # (arrays[i][0], array_number, next_index)
        min_hp.insert_minheap((arrays[i][0], i, 1))

    # now one by one get minimum element from minheap and replace it with next element of its array


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

print('Largest pairs of n elements in two given arrays:',maxH.largest_pairs_in_arrays([40,60,10,300,75], [10,30,12,45, 54]))

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

print('Running Median of an infinite series of integers:', maxH.median_in_running_stream([1,2,3]))

print('Maximum sliding window using doubly ended queue:', maxH.max_in_sliding_window_DEqueue([1,3,4,7,2,1,8,5], 3))

# print('Minimum window for substring to find pattern in input string:', end=' ')
print(maxH.find_min_window_for_substring('Shradha is getting married', 'asti'))