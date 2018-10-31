import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_heaps, binary_search_tree
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
def quick_sort(inp, start, end):
    if start < end:
        # inp[partioning_index] will now be at it's right place
        partioning_index = _partition(inp, start, end)

        quick_sort(inp, start, partioning_index-1)
        quick_sort(inp, partioning_index+1, end)

    return inp


def _partition(inp, start, end):
    pivot = inp[end]
    # index of smaller element
    i = start - 1

    for j in range(start, end+1):
        # if current element is <= pivot
        if inp[j] <= pivot:
            # increment index of smaller element
            i += 1
            if i < j:
                inp[i], inp[j] = inp[j], inp[i]

    return i


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
def radix_sort(inp):


# Topological Sort -- implemented in Graphs.py
# given array of n numbers containing repetition of some numbers. check whether there are repeated elements or not.
# time O(n^2), space O(1) -- brute force technique

# given array of n numbers containing repetition of some numbers. check whether there are repeated elements or not.
# time O(n.logn), space O(1) -- sorting technique

# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n^2), space O(1)

# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n.logn), space O(1) heap sort

# given array where each element represents a vote in election. Each vote integer represents ID of chosen candidate.
# Determine who wins the election , time O(n) n= no. of votes in array, space O(k) k=no.of candidates participated
# counting sort

# given an array of n elements, each integer in range [1, n^2]. sort array in O(n) time

# given an array of n elements, each integer in range [1, n^3]. sort array in O(n) time

# given arrays A and B, a number K, determine whether there exists a∈A, b∈B such that a+b = K, time O{n.logn)

# given arrays A and B, a number K, determine whether there exists a∈A, b∈B, c∈C such that a+b+c = K, time O{n.logn)

# better sorting method for linked list - Merge sort

# merge two sorted arrays. first array of size m+n with m elements, second array with n elements




