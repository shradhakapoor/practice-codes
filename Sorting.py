import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_heaps, binary_search_tree, Graphs
from collections import defaultdict


print('.................................................................................')
# Bubble sort (ascending order)
# best: O(n), worst: O(n^2), average: O(n^2), worst space: O(1) auxillary
def bubble_sort(inp):
    n = len(inp)

    # traverse through all array elements
    for i in range(n):
        # last i elements are already in place
        for j in range(n-i-1):
            # swap if jth element > j+1 th element
            if inp[j] > inp[j+1]:
                inp[j], inp[j+1] = inp[j+1], inp[j]

    print('Bubble Sort in ascending order:', inp)


bubble_sort([64, 34, 25, 12, 22, 11, 90])


# Selection Sort (ascending order)
# best: O(n), worst: O(n^2), average: O(n^2), worst space: O(1) auxillary
def selection_sort(inp):
    n = len(inp)

    # Traverse through all elements
    for i in range(n):
        # find minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1,n):
            if inp[min_index] > inp[j]:
                min_index = j

        # swap found minimum element with ith element
        inp[i], inp[min_index] = inp[min_index], inp[i]

    print( 'Selection Sort in ascending order:', inp )


selection_sort( [64, 34, 25, 12, 22, 11, 90] )


# Insertion Sort (ascending order)
# best: O(n^2), worst: O(n^2), average: O(n^2), worst space: O(1) auxillary, O(n^2) total
def insertion_sort(inp):
    n = len(inp)

    # Traverse through all elements from 1st position
    for i in range(1, n):
        curr_element = inp[i]
        j = i-1

        # insert curr_element at correct place in sorted part of array
        # by moving each element of sorted array one position right
        while j >= 0 and curr_element < inp[j]:
            inp[j+1] = inp[j]
            j -= 1

        inp[j+1] = curr_element

    print( 'Insertion Sort in ascending order:', inp )


insertion_sort( [64, 34, 25, 12, 22, 11, 90] )


# Shell Sort
# it's a generalisation of insertion sort
# best: O(n), worst: O(n.log^2(n)), average: depends on gap sequence, worst space: O(n)
def shell_sort(inp):
    n = len(inp)

    # start with a big gap then reduce the gap
    gap = n//2

    # we do gapped insertion sort for this gap size
    # insertion sort is sorting with gap = 1

    # First gap-elements inp[0, gap-1] are in gapped order.
    # keep adding one more element until the entire array is gap sorted
    while gap > 0:

        for i in range(gap, n):
            # add inp[i] to the gap-sorted array.
            curr_element = inp[i]

            # insert curr_element at correct place in gap-sorted array
            # by moving each element of gap-sorted array one position right
            j = i
            while j >= gap and curr_element < inp[j-gap]:
                inp[j] = inp[j-gap]
                j -= gap

            inp[j] = curr_element

        gap = gap // 2

    print( 'Shell Sort in ascending order:', inp )


shell_sort( [64, 34, 25, 12, 22, 11, 90] )


# Merge Sort
# best: theta(n.logn), worst: theta(n.logn), average: theta(n.logn), worst space: theta(n) auxillary

def merge_sort(inp, n):
    # splitting
    if len(inp)>1:
        mid = len(inp)//2
        lefthalf = inp[:mid]
        righthalf = inp[mid:]

        merge_sort(lefthalf, n)
        merge_sort(righthalf, n)

        # merging
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                inp[k]=lefthalf[i]
                i += 1
            else:
                inp[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            inp[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            inp[k]=righthalf[j]
            j += 1
            k += 1

    # n is length of initial input, this is passed just to print the final sorted array.
    if len(inp) == n:
        print( 'Merge Sort in ascending order:', inp )


merge_sort( [64, 34, 25, 12, 22, 11, 90], 7)

# Heap Sort -- implemented in file binary_heaps.py
# best: theta(n.logn), worst: theta(n.logn), average: theta(n.logn), worst space: theta(1) auxillary, theta(n) total
minH = binary_heaps.Binary_Heap()
# minHeap formed by insertion
#       10
#     /    \
#    20    100
#   /  \
# 200  500
minH.insert_minheap(100)
minH.insert_minheap(200)
minH.insert_minheap(10)
minH.insert_minheap(20)
minH.insert_minheap(500)
print( 'Heap Sort in ascending order:', minH.heap_sort_ascending_order() )


# Quick Sort, pivot as last element
# best: O(n.logn), worst: O(n^2), average: O(n.logn), worst space: O(1)
# sort an array of 0's, 1's and 2's. put all o first, then 1 and all 2 in last. (quick sort)

# def quick_sort(inp, start, end):
#     if start < end:
#         # inp[partioning_index] will now be at it's right place
#         partioning_index = _partition(inp, start, end)
#
#         quick_sort(inp, start, partioning_index-1)
#         quick_sort(inp, partioning_index+1, end)
#
#     return inp
#
#
# def _partition(inp, start, end):
#     pivot = inp[end]
#     # index of smaller element
#     i = start - 1
#
#     for j in range(start, end+1):
#         # if current element is <= pivot
#         if inp[j] <= pivot:
#             # increment index of smaller element
#             i += 1
#             if i < j:
#                 inp[i], inp[j] = inp[j], inp[i]
#
#     return i

def quick_sort(inp, start, end):
    if start < end:
            # making inp[start] as pivot
            mid = start+end // 2
            if mid <= end:
                inp[start], inp[mid] = inp[mid], inp[start]

            lo = start
            hi = end
            while lo < hi:
                if inp[lo+1] > inp[start] and inp[hi] < inp[start]:
                    inp[lo+1], inp[hi] = inp[hi], inp[lo+1]
                if inp[lo+1] <= inp[start]:
                    lo += 1
                if inp[hi] >= inp[start] and lo < hi:
                    hi -= 1


            inp[lo], inp[start] = inp[start], inp[lo]

            quick_sort(inp, start, lo-1)
            quick_sort(inp, lo+1, end)

    return inp

print('Quick sort in ascending order:', quick_sort([64, 34, 25, 12, 22, 11, 90], 0, 6))


# Tree Sort
# worst: O(n^2), average: O(n.logn), worst space: O(n) auxillary

# BST
#           500
#          /   \
#        400   800
#       /  \   /  \
#     200 450 700 900
bst = binary_search_tree.Binary_Search_Tree(500)
bst.insert(400)
bst.insert(800)
bst.insert(200)
bst.insert(450)
bst.insert(700)
bst.insert(900)

print('Tree sort in ascending order:', end=' ')
bst.tree_sort(bst.root)


# Counting Sort, sorting in linear time in certain situations
# sort an array of 0's, 1's and 2's. put all o first, then 1 and all 2 in last. (counting sort)
def counting_sort(inp):
    min_value = min(inp)
    max_value = max(inp)
    length = len(inp)
    def defaultvalue():
        return 0
    temp = defaultdict(defaultvalue)

    for i in range(length):
        # count the occurence of each integer in input
        temp[inp[i]] += 1

    temp_sum = 0
    for i in range(min_value, max_value + 1):
        temp_sum += temp[i]
        # compute sum_count
        temp[i] = temp_sum

    output = [0] * len(inp)
    for i in range(length):
        output[(temp[inp[i]]-1)] = inp[i]
        temp[inp[i]] -= 1

    print('\nCounting Sort in ascending order:', output)


counting_sort([6, 3, 5, 11, 2, 11, 9, 6, 3])


# Radix sort
# sorts n^2 elements in linear time

# Topological Sort -- implemented in Graphs.py
# create a directed acyclic graph - adj list
graph3 = Graphs.Graph_adj_list()
graph3.add_vertex( 'a' )
graph3.add_vertex( 'b' )
graph3.add_vertex( 'c' )
graph3.add_vertex( 'e' )
graph3.add_vertex( 'd' )
graph3.add_edge_directed_graph( 'a', 'b', 10 )
graph3.add_edge_directed_graph( 'b', 'e', 20 )
graph3.add_edge_directed_graph( 'a', 'd', 30 )
graph3.add_edge_directed_graph( 'b', 'c', 40 )
graph3.add_edge_directed_graph( 'd', 'c', 60 )
graph3.add_edge_directed_graph( 'e', 'd', 50 )
print('Topological Sort in ascending order:', graph3.topological_sort_DAG().items)


# given array of n numbers containing repetition of some numbers. check whether there are repeated elements or not.
# time O(n^2), space O(1) -- brute force technique
def find_repeated_number(inp):
    size = len(inp)
    for i in range(size):
        for j in range(i+1, size):
            if inp[i] == inp[j]:
                return True


if find_repeated_number([6, 3, 5, 11, 2, 11, 9, 6, 3]):
    print('There are repeated elements, using Brute Force Technique.')

# given array of n numbers containing repetition of some numbers. check whether there are repeated elements or not.
# time O(n.logn), space O(1) -- sorting technique


# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n^2), space O(1)
    # solution: counting the frequency of each integer ID.
def find_winner(inp):
    # count_dict - key = ID, value = frequency of ID
    def defValue():
        return 0
    count_dict = defaultdict(defValue)
    for id in inp:
        if count_dict[id] is None:
            count_dict[id] = 1
        else:
            count_dict[id] += 1

    # find the winner
    mx_id, mx = 0, 0
    for id, freq in count_dict.items():
        if freq > mx:
            mx = freq
            mx_id = id
    print('Winner is the candidate ID %s with %s votes'% (str(mx_id), str(mx)))


find_winner([12, 13, 11, 12, 12, 45, 45, 45, 45, 45, 12, 13, 11])

# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n.logn), space O(1) heap sort

# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n) n= no. of votes in array, space O(k) k=no.of candidates participated
# counting sort

# given an array of n elements, each integer in range [1, n^2]. sort array in O(n) time

# given an array of n elements, each integer in range [1, n^3]. sort array in O(n) time


# given arrays A and B, a number K, determine whether there exists a∈A, b∈B such that a+b = K, time O{n.logn) space O(n)
def find_sum_pairs(A, B, K):
    m, n = len(A), len(B)
    # store all elements of array A in a set
    s = set(A)
    # subtract each element of B from K and check if the result is present in s
    for elem in B:
        diff = K - elem
        if diff in s:
            print(diff,', ', elem)


print('pairs of a and b where a + b = k are:', end = '\n')
find_sum_pairs([1, 0, -4, 7, 6, 4], [0, 2, 4, -3, 2, 1], 8)


# given array A of n elements, find i j k such that A[i]^2 + A[j]^2 = A[k]^2
# given arrays A and B, a number K, determine whether there exists a∈A, b∈B, c∈C such that a+b+c = K
def find_sum_triplets(A, B, C, K):
    m, n, o = len(A), len(B), len(C)

    # dictionary, key = sum of A and B, value = pair of a and b
    def defValue():
        return []
    temp_dict = defaultdict(defValue)

    for i in range(m):
        for j in range(n):
            sm = A[i] + B[j]
            temp_dict[sm].append((A[i], B[j]))

    for t in temp_dict.keys():
        diff = K - t
        if diff in C:
            result = temp_dict[t]
            result.append(diff)
            print(result)


print('Triplets of a, b and c where a + b + c = k are:', end = '\n')
find_sum_triplets([1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50, 60], [39, 28, 23, 45, 1], 50)

# better sorting method for linked list - Merge sort


# merge two sorted arrays. first array of size m+n with m elements, second array with n elements
def merge_sorted_arrays(A, B, m, n):
    # iterate through B starting from last element
    for i in range((n-1), -1, -1):
        j = m-1
        while B[i] < A[j]:
            A[j+1] = A[j]
            j -= 1
        if j >= 0:
            # insert the element from B into right position in A and increment the size of A.
            A[j+1] = B[i]
            m += 1

    print('Merged Sorted Array is:', A)

merge_sorted_arrays([1, 5, 9, 10, 15, 20, 0, 0, 0, 0], [2, 3, 8, 13], 6, 4)







