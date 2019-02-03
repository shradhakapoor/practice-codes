from math import sqrt, pow


# Given an array with stock prices on n consecutive days. Find the day on which to buy stock and on which to sell stock
# to make maximum profit.allowed to buy and sell only once.
# Concept used: Maximum difference between two elements such that larger element appears after the smaller number
# time O(n^2)
def buy_sell_once(prices):
    n = len(prices)
    # prices must be given for atleast 2 days
    if n < 2:
        return
    indces = (float('inf'), float('inf'))
    max_diff = prices[1] - prices[0]
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] - prices[i] > max_diff:
                max_diff = prices[j] - prices[i]
                indces = (i,j)

    return indces

print('The day on which to buy stock and to sell to make max profit, transact once:',buy_sell_once([1, 2, 90, 10, 110]))

# Given an array with stock prices on n consecutive days. Find the day on which to buy stock and on which to sell stock
# to make maximum profit.allowed to buy and sell only once.
# Concept used: Maximum difference between two elements such that larger element appears after the smaller number
# time O(n)
def buy_sell_once_trick(prices):
    n = len(prices)
    # prices must be given for atleast 2 days
    if n < 2:
        return
    indces = [0, float('inf')]
    max_diff = prices[1] - prices[0]
    min_elem = prices[0]
    for i in range(1, n):
        if prices[i] - min_elem > max_diff:
            max_diff = prices[i] - min_elem
            indces[1] = i
        if prices[i] < min_elem:
            min_elem = prices[i]
            indces[0] = i

    return indces

print('The day on which to buy stock and to sell to make max profit, transact once:',
    buy_sell_once_trick([1, 2, 90, 10, 110]))

# Given an array with stock prices on n consecutive days. Find the day on which to buy stock and on which to sell stock
# to make maximum profit.allowed to buy and sell multiple times.
# time O(n)
def buy_sell_multiple(prices):
    n = len(prices)
    count = 0
    # prices must be given for atleast 2 days
    if n < 2:
        return
    result = dict()
    i = 0
    while i< n-1:
        # find local minima, limit is n-2 as we are comparing current element to next element
        while i<n-1 and prices[i+1] <= prices[i]:
            i = i+1
        # If we reached the end, break as no further solution possible
        if i == n-1:
            break
        # store index of minima
        result[count] = [i]
        i = i + 1
        # find local maxima, limit is n-1 as we are comparing to previous element
        while i<n and prices[i] >= prices[i-1]:
            i = i + 1
        # store index of maxima
        result[count].append(i-1)
        count += 1

    return result

print('The day on which to buy stock and to sell to make max profit, transact multiple times:',
    buy_sell_multiple([100, 180, 260, 310, 40, 535, 695]))

# given a sequence of numbers a1, a2,...an. Find contiguous subsequence for which the sum of elements is maximum.
# efficient solution using dynamic programming
def max_sum_subsequence(inp):
    result_sum, curr_sum = float('-inf'), 0
    strt, ennd, s = 0, 0, 0
    for i in range(len(inp)):
        curr_sum += inp[i]
        # if final sum is less than the current sum then end position is here
        if result_sum < curr_sum:
            result_sum = curr_sum
            strt = s
            ennd = i
        # if current sum is negative then start from next i
        if curr_sum < 0:
            curr_sum = 0
            s = i+1

    return result_sum, strt, ennd

res = max_sum_subsequence([-2, -3, 4, -1, -2, 1, 5, -3])
print('contiguous subsequence where sum of elements is maximum: %d, start position: %d, end position: %d' %(res))

# Given set of n points S = p1,p2,...pn where pi= (xi,yi). Find pair of points having smallest distance among all pairs.
# assume all points are in 1D. time O(n(logn)^2)

# Given set of n points S = p1,p2,...pn where pi= (xi,yi). Find pair of points having smallest distance among all pairs.
# assume all points are in 2D. time O(nlogn) using divide and conquer
def distance(a, b):
    return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))

# Recursively, find the smallest distance among the given subarray points
def bruteMin(points, current=float("inf")):
    if len(points) < 2: return current
    else:
        head = points[0]
        del points[0]
        newMin = min([distance(head, x) for x in points])
        newCurrent = min([newMin, current])
        return bruteMin(points, newCurrent)

def divideMin(points):
    # pre-processing step: input points are sorted according to x coordinates
    # then find middle point in sorted array
    mid_point = len(sorted(points))//2

    # Divide given points into two halves, first from point 0 to midpoint and second from midpoint to end
    # recursively find smallest distances in both subarrays.Let distances be dl and dr.
    # Find minimum of dl and dr. let the minimum distance be minimum_d, this is upper bound of minimum distance.
    minimum_d = min([bruteMin(points[:mid_point]), bruteMin(points[mid_point:])])

    # Now we need to consider the pairs such that one point in pair is in left subarray and other in right subarray.
    # find all points whose x coordinate is between minimum_d and middle vertical line(assumed at midpoint)
    # build a strip[] of all such points
    strip = list(filter(lambda x: x[0] > mid_point - minimum_d and x[0] < mid_point + minimum_d, points))

    # find smallest distance in strip
    minimum_strip_d = bruteMin(strip)

    # finally return minimum of minimum_d and minimum_strip_d
    return min([minimum_strip_d, minimum_d])

list1 = [(12,30), (40, 50), (5, 1), (12, 10), (3,4)]
print('smallest distance between given pair of points:', divideMin(list1))