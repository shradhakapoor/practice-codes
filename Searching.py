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
def sum_closest_zero_bruteforce(inp):
    min_l, min_r = 0, 1
    n = len(inp)
    min_sum = inp[0] + inp[1]
    for i in range(n-1):
        for j in range(i+1, n):
            sm = inp[i] + inp[j]
            if abs(min_sum) > abs(sm):
                min_sum = sm
                min_l = i
                min_r = j

    return inp[min_l],inp[min_r]


print('Sum closest to zero, using brute force:', sum_closest_zero_bruteforce([1, 60, -10, 70, -80, 85]))


# given array with both +ve and -ve nos. find 2 elements whose sum is closest to 0. sorting
def sum_closest_zero_sorting(inp):
    n = len(inp)
    inp = merge_sort(inp, n)
    l, r = 0, n-1
    min_l, min_r = 0, n-1
    min_sum = float('inf')
    # there should be atleast 2 input values
    if n < 2:
        return

    while l < r:
        sm = inp[l] + inp[r]
        if abs(min_sum) > abs(sm):
            min_sum = sm
            min_l = l
            min_r = r
        if sm < 0:
            l += 1
        else:
            r -= 1

    return inp[min_l], inp[min_r]


print('Sum closest to zero, using sorting:', sum_closest_zero_sorting([1, 60, -10, 70, -80, 85]))


# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K.brute force, O(n^3)time
def triplet_sum_closest_k(inp, K):
    n = len(inp)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for h in range(j+1, n):
                if inp[i]+inp[j]+inp[h] == K:
                    print(inp[i],inp[j],inp[h])


print('Triplet that sum to given K, brute force:', end = ' ')
triplet_sum_closest_k([1, 4, 45, 6, 10, 8], 22)


# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K.sorting, O(n^2)time
def triplet_sum_closest_k_sorting(inp, K):
    n = len(inp)
    inp = merge_sort(inp, n)
    for i in range(n-2):
        r = n-1
        l = i+1
        while l < r:
            sm = inp[i] + inp[l] + inp[r]
            if sm == K:
                print(inp[i],inp[l],inp[r])
            elif sm < K:
                l += 1
            else:
                r -= 1


print('Triplet that sum to given K, sorting:', end = ' ')
triplet_sum_closest_k([1, 4, 45, 6, 10, 8], 22)


# given array with both +ve and -ve nos. find 3 elements whose sum is closest to given element K. using set
def triplet_sum_closest_k_set(inp, K):
    n = len(inp)
    for i in range(n-1):
        # find pair in remaining inp with sum = K - inp[i]
        s = set()
        curr_sum = K - inp[i]
        for j in range(i+1, n):
            rem_sum = curr_sum-inp[j]
            if rem_sum in s:
                print(inp[i],', ',inp[j],', ', rem_sum)
            else:
                s.add(inp[j])


print('Triplet that sum to given K, using set:', end = ' ')
triplet_sum_closest_k([1, 4, 45, 6, 10, 8], 22)


# given array of unknown size with all 1s in beginning and 0s in end. find index in array from where 0 starts.
def index_first_zero(inp, low, high):
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if inp[mid] == 0 and (inp[mid-1] == 1 or mid == 0):
            break
        # first 0 lies to left of mid
        elif inp[mid] == 0:
            high = mid-1
        # first 0 lies to right of mid
        else:
            low = mid+1

    # required index
    return mid


def find_first_zero_unknown_size(inp):
    low, high = 0, 1
    while inp[high] == 1:
        # lower bound
        low = high
        # upper bound
        high = 2*high

    return index_first_zero(inp, low, high)


print('Position of first zero in an infinite input:', find_first_zero_unknown_size([1,1,1,1,1,0,0,0,0]))


# given sorted array of n integers that has been rotated unknown number of times, find an element in time O(logn)
# example: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14), output index 8. solve using a variant of binary search
def sorted_rotated_usingbinarySearch(inp, K, low, high):
    if low > high:
        return -1
    mid = (low+high)// 2
    # if key is present at mid point then return mid
    if inp[mid] == K:
        return mid
    # else, if inp[low...mid] is sorted then
    if inp[low] <= inp[mid]:
        # if inp[low...mid] is sorted, determine which half can contain the key
        if inp[low] <= K <= inp[mid]:
            return sorted_rotated_usingbinarySearch(inp, K, low, mid-1)
        else:
            return sorted_rotated_usingbinarySearch(inp, K, mid+1, high)
    # if inp[low...mid] is not sorted then inp[mid+1...high] must be sorted
    if inp[mid+1] <= K <= inp[high]:
        return sorted_rotated_usingbinarySearch(inp, K, mid+1, high)
    else:
        return sorted_rotated_usingbinarySearch(inp, K, low, mid-1)


print('Find K in a sorted rotated array:', sorted_rotated_usingbinarySearch([4, 5, 6, 7, 8, 9, 1, 2, 3], 6, 0, 8))


# given a bitonic array, find the index of maximum element in time O(logn), modified binary search
def max_elem_bitonic_array(inp, low, high):
    # Base case: only one element is present
    if low == high:
        return inp[low]

    # if only two elements are present and first is greater
    if high == low+1 and inp[high] <= inp[low]:
        return inp[low]
    # if only two elements are present and second is greater
    if low == high -1 and inp[high] > inp[low]:
        return inp[high]

    mid = (low+high)// 2
    # if inp[mid] is greater than both mid-1 and mid+1
    if inp[mid-1] <= inp[mid] > inp[mid+1]:
        return inp[mid]
    # if inp[mid] is greater than next elem but smaller than previous elem then max lies on left side of inp
    if inp[mid-1] > inp[mid] > inp[mid+1]:
        return max_elem_bitonic_array(inp, low, mid-1)
    else:
        return max_elem_bitonic_array(inp, mid+1, high)


print('Maximum element in bitonic array:', max_elem_bitonic_array([1, 3, 50, 10, 9, 7, 6], 0, 6))


# given a sorted array A of n elements with duplicates, find index of first occurence of number p in time O(logn)
def first_occurence_p(inp, low, high, p):
    result = -1
    while low <= high:
        mid = (low+high) // 2
        # if p is found then update result and search in left inp
        if inp[mid] == p:
            result = mid
            high = mid -1
        elif p < inp[mid]:
            high = mid-1
        else:
            low = mid+1

    return result


print('Sorted array with duplicates, first occurence of p:', first_occurence_p([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 0, 9, 5))


# given a sorted array A of n elements with duplicates, find index of last occurence of number p in time O(logn)
def last_occurence_p(inp, low, high, p):
    result = -1
    while low <= high:
        mid = (low+high) // 2
        # if p is found then update result and search in right inp
        if inp[mid] == p:
            result = mid
            low = mid +1
        elif p < inp[mid]:
            high = mid-1
        else:
            low = mid+1

    return result


print('Sorted array with duplicates, first occurence of p:', last_occurence_p([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 0, 9, 5))


# given a sorted array A of n elements with duplicates, find number of occurences of number p in time O(n) linear search
def number_occurences_linearsearch(inp, p):
    result = 0
    for i in range(len(inp)):
        if p == inp[i]:
            result += 1
    return result


print('Sorted array, number of occurences of p, linear search:',
    number_occurences_linearsearch([1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8], 2))


# given a sorted array A of n elements with duplicates, find number of occurences of number p . binary search
def number_occurences_p_binarysearch(inp, low, high, p):
    # find index of p in inp
    indx = binary_search(inp, p)

    # if p not found
    if not indx:
        return 0
    # count p's on left side
    count = 1
    left = indx -1
    while left >= 0 and inp[left] == p:
        count += 1
        left -= 1
    # count p's on right side
    right = indx+1
    while right < len(inp) and inp[right] == p:
        count += 1
        right += 1

    return count


print('Sorted array, number of occurences of p, binary search:',
    number_occurences_p_binarysearch([1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ], 0 , 9, 2))

# if a number repeats more than or equal to n/2 times then we can find that element at inp[n/2] time O(1) space O(1)

# given an array of n elements, identify the element that appears more than n/2 times, time O(n^2) space O(1)
def element_frequency_halflength(inp):
    n = len(inp)
    max_count = 0
    indx = -1

    for i in range(n):
        count = 0
        for j in range(n):
            if inp[i] == inp[j]:
                count += 1
        if max_count < count:
            max_count = count
            indx = i

    if max_count >= n//2:
        return inp[indx]


print('element that appears more than n/2 times:', element_frequency_halflength([1, 1, 2, 1, 3, 5, 1]))

# given an array of n elements, identify the element that appears more than n/2 times, time O(n.logn) space O(n)
# Solution -- Binary Search Tree: insert elements in BST one by one
# if an element is already present then increment the count of the node.
# At any stage, if count of a node becomes more than n/2 then return.

# given an array of n elements, identify the element that appears more than n/2 times, time O(n) space O(n)
# hashing

# given array of 2n+1 elements, n elements appear twice and 1 integer appears once.find the integer in O(n) operations
def n_appeartwice_1_appearonce(inp):
    n = len(inp)
    xor = 0
    # find xor of all numbers.
    # XOR of a number with itself is 0.
    # XOR of a number with 0 is the number.
    for i in range(n):
        xor ^= inp[i]

    return xor


print('n elements appear twice and 1 integer appears once:', n_appeartwice_1_appearonce([3, 8, 3, 2, 2, 1, 1]))


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
