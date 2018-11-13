from collections import defaultdict
from math import sqrt

# binary search
def binary_search(inp, x):
    low, high = 0, len(inp)-1
    while low <= high:
        mid = (low + high) // 2
        if inp[mid] == x:
            return mid
        elif inp[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return False


print('Finding x using binary search:', binary_search([33, 22, 44, 54, 64, 76, 12], 64))


# check whether there are any duplicate elements in array of n numbers, time O(n^2) space O(1)
# brute force
def find_duplicates_brute_force(inp):
    n = len(inp)
    for i in range(n):
        for j in range(i+1, n):
            if inp[i] == inp[j]:
                print(inp[i], end = ', ')


def merge_sort(inp, n):
    # splitting
    if len(inp) > 1:
        mid = len(inp) // 2
        lft = inp[:mid]
        rgt = inp[mid:]
        merge_sort(lft, n)
        merge_sort(rgt, n)

        # merging
        i, j, k = 0, 0 , 0
        while i < len(lft) and j < len(rgt):
            if lft[i] < rgt[j]:
                inp[k] = lft[i]
                i += 1
            else:
                inp[k] = rgt[j]
                j += 1
            k += 1
        while i < len(lft):
            inp[k] = lft[i]
            i += 1
            k += 1
        while j < len(rgt):
            inp[k] = rgt[j]
            j += 1
            k += 1

    if len(inp) == n:
        return inp


# check whether there are any duplicate elements in array of n numbers, time O(n.logn) space O(1)
def find_duplicates_sorting(inp):
    n = len(inp)
    inp = merge_sort(inp, n)  # worst case O(nlogn)
    for i in range(n):
        if inp[i] == inp[i+1]:
            return True


# check whether there are any duplicate elements in array of n numbers, time O(n) space O(n)
def find_duplicates_hashing(inp):
    def defValue():
        return None
    hsh = defaultdict(defValue)
    for i in inp:
        if hsh[i] is None:
            hsh[i] = 1
        else:
            return True


inp = [33, 12, 44, 54, 64, 76, 12, 33]
print('whether duplicates are there? using brute force:', end =' ')
find_duplicates_brute_force(inp)
print('\nwhether duplicates are there? using sorting:', find_duplicates_sorting(inp))
print('whether duplicates are there? using hashing:', find_duplicates_hashing(inp))


# check whether there are any duplicate elements in array of n numbers, time O(n) space O(1)
def find_duplicates_negation_technique(inp):
    n = len(inp)
    inp = merge_sort(inp, n)
    for i in range(n):
        if inp[abs(inp[i])] < 0:
            return True
        else:
            inp[abs(inp[i])] = -1 * inp[abs(inp[i])]


print('whether duplicates are there? using negation technique:',
    find_duplicates_negation_technique([4, 2, 4, 5, 2, 3, 1]))


# find element that appears maximum number of times in array, time O(n^2) space O(1), brute force
# find element that appears maximum number of times in array, time O(n.logn) space O(1), sorting
# find element that appears maximum number of times in array, time O(n) space O(n), hashing

# find first element which is repeated in an array, brute force
# find first element which is repeated in an array, sorting technique
# find first element which is repeated in an array, hashing technique

# find the missing number - given a list of n-1 integers in range of 1 to n, no duplicates in the list.
# simple solution ,time O(n^2) space O(1)
# find the missing number - given a list of n-1 integers in range of 1 to n, no duplicates in the list.
# sorting technique, time O(n.logn) space O(1)
# find the missing number - given a list of n-1 integers in range of 1 to n, no duplicates in the list.
# hashing technique, time O(n) space O(n)

# Given an array of positive integers. All numbers occur even number of times except one number which occurs
# odd number of times - O(n) time & constant space
def odd_times_occurence(inp):
    result = 0
    # do bitwise XOR of all the elements
    for elem in inp:
        result = result ^ elem

    return result


print('The only number occuring odd times:', odd_times_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]))

# find two repeating elements in array, all elements are in range 1 to n. time O(n^2) space O(1)
# find two repeating elements in array, all elements are in range 1 to n. time O(n.logn) space O(1) comparison sorting
# find two repeating elements in array, all elements are in range 1 to n. time O(n) space O(n) hashing
# find two repeating elements in array, all elements are in range 1 to n. time O(n) space O(1) XOR operation


# find two repeating elements in array, all elements are in range 1 to n. time O(n) space O(1) sum and product formula
def two_rep_elem_sum_prod(inp, n):
    sum_n_elements = (n * (n + 1)) // 2
    sum_inp_elements = 0
    for i in inp:
        sum_inp_elements += i

    a_sum_b = sum_inp_elements - sum_n_elements

    product_n_elements = 1
    for i in range(1, n+1):
        product_n_elements *= i
    product_inp_elements = 1
    for i in range(len(inp)):
        product_inp_elements *= inp[i]

    a_product_b = product_inp_elements // product_n_elements

    a_diff_b = sqrt((a_sum_b * a_sum_b) - (4 * a_product_b))

    a = (a_sum_b + a_diff_b) // 2
    b = a_sum_b - a

    return a,b


print('two repeating elements in a given array:', two_rep_elem_sum_prod([1,4,5,6,3,2,5,2], 6))


# given array with both +ve and -ve nos. find 2 elements whose sum is closest to 0. brute force

# given array with both +ve and -ve nos. find 2 elements whose sum is closest to 0. sorting

# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K. brute force

# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K. sorting

# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K. hashing and searching

# given array with both +ve and -ve nos. find 3 elements whose sum is closest to 0. binary search

# given array of unknown size with all 1s in beginning and 0s in end. find index in array from where 0 starts.

# given sorted array of n integers that has been rotated unknown number of times, find an element in time O(logn)
# example: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14), output index 8. solve using a variant of binary search

# given sorted array of n integers that has been rotated unknown number of times, find an element in time O(logn)
# example: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14), output index 8. Solve using recursion

# given a bitonic array, find the index of maximum element in time O(logn)

# given a sorted array A of n elements with duplicates, find index of first occurence of number p in time O(logn)

# given a sorted array A of n elements with duplicates, find index of last occurence of number p in time O(logn)

# given a sorted array A of n elements with duplicates, find number of occurences of number p in time O(n) linear search

# given a sorted array A of n elements with duplicates, find number of occurences of number p . binary search

# given an array of n elements, identify the element that appears more than n/2 times, time O(n^2) space O(1)

# given an array of n elements, identify the element that appears more than n/2 times, time O(n.logn) space O(n)

# given an array of n elements, identify the element that appears more than n/2 times, time O(n.logn) space O(1)

# given an array of n elements, identify the element that appears more than n/2 times, time O(n) space O(1)

# given array of 2n+1 elements, n elements appear twice and 1 integer appears once.find the integer in O(n) operations

# given n story building and m eggs, assume an egg breaks if its thrown from floor F or higher, otherwise not break.
# Determine floor F while breaking O(logn) eggs

# given array of n distinct integers, find local minimum: an index i such that A[i-1]<A[i]<A[i+1] in O(logn)

# given a number n , find number of trailing zeros in n!

# given array of 2n integers in format a1a2a3...anb1b2b3...bn shuffle array to a1b1a2b2a3b3...anbn without extra memory
# using brute force

# given array of 2n integers in format a1a2a3...anb1b2b3...bn shuffle array to a1b1a2b2a3b3...anbn without extra memory
# using divide and conquer

# given array, find maximum j-i such that A[j]>A[i]. ex: {34,8,10,3,2,80,30,33,1} output: 6 (j=7 i=1)- brute force

# given array, find maximum j-i such that A[j]>A[i]. ex: {34,8,10,3,2,80,30,33,1} output: 6 (j=7 i=1)
# time O(n) space O(n)

# given array, check whether list is pairwise sorted or not

# given array of n, print frequencies of elements without using extra space.all elements are +ve,editable, less than n
