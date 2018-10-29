import os
__path__=[os.path.dirname(os.path.abspath(__file__))]
from . import binary_heaps

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

# Quick Sort
# best: O(n.logn), worst: O(n^2), average: O(n.logn), worst space: O(1)
def quick_sort(inp, low, high):
    if low < high:
        pivot = _median_of_input(inp, low, high)
        quick_sort(inp, low, pivot-1)
        quick_sort(inp, pivot+1, high)

    print( 'Quick Sort in ascending order:', inp )


def _median_of_input(inp, low, high):
    mid = (low+high) // 2
    if inp[low] > inp[mid]:
        inp[low], inp[mid] = inp[mid], inp[low]

    if inp[low] > inp[high]:
        inp[low], inp[high] = inp[high], inp[low]

    if inp[mid] > inp[high]:
        inp[mid], inp[high] = inp[high], inp[mid]

    inp[mid], inp[low] = inp[low], inp[mid]

    return _partition(inp, low, high)


def _partition(inp, low, high):
    pivot = inp[low]
    left, right = low, high

    while left < right:
        while inp[right] > pivot:
            right -= 1
        while left < right and inp[left] < pivot:
            left += 1
        # if still left < right, swap inp[left] and inp[right]
        if left < right:
            inp[left], inp[right] = inp[right], inp[left]

    inp[low] = inp[right]
    inp[right] = pivot

    return right


quick_sort( [64, 34, 25, 12, 22, 11, 90], 0, 6)


# Tree Sort
# worst: O(n^2), average: O(n.logn), worst space: O(n) auxillary

# Counting Sort

# Topological Sort -- implemented in Graphs.py

# Radix sort
# sorts n^2 elements in linear time

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

# sort an array of 0's, 1's and 2's. put all o first, then 1 and all 2 in last. (counting sort)

# sort an array of 0's, 1's and 2's. put all o first, then 1 and all 2 in last. (quick sort)

# better sorting method for linked list - Merge sort

# merge two sorted arrays. first array of size m+n with m elements, second array with n elements




