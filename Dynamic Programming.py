# given an array of n numbers, find a contiguous subsequence for which the sum of elements is maximum.
# finding M(i) that indicates max sum over all windows ending at i.
# time O(n) space O(1)
def maximum_sum_subsequence(inp):
    max_sum, current_sum = float('-inf'), 0
    strt, ennd, s = 0, 0, 0
    for i in range(0, len(inp)):
        current_sum += inp[i]
        if max_sum < current_sum:
            max_sum = current_sum
            strt = s
            ennd = i
        if current_sum < 0:
            current_sum = 0
            s = i+1

    return max_sum, strt, ennd

res = maximum_sum_subsequence([-2, -3, 4, -1, -2, 1, 5, -3])
print('contiguous subsequence where sum of elements is maximum: %d, start position: %d, end position: %d' %(res))

# given an array of n positive numbers, find M(i) that indicates max sum over all windows starting at 1 and ending at i.
# condition: not to select two contiguous numbers. time O(n)
def max_sum_not_contiguous(inp):
    # start with incl as first element in array, and excl as 0
    incl, excl = inp[0], 0

    for i in range(1, len(inp)):
        temp = incl
        # new incl is the max of (old incl and excl+current i)
        incl = max(incl, excl+inp[i])
        # assign old incl to excl
        excl = temp

    return incl

print('Maximum sum for non adjacent elements:', max_sum_not_contiguous([5, 5, 10, 100, 10, 5]))

# finding maximum sum non adjacent elements assuming its a circular array.
# So first element cannot be with last element.
def max_sum_non_adjacent_circular_array(inp):
    if len(inp) == 0:
        return 0
    if len(inp) == 1:
        return inp[0]

    # find max sum from left to right ignoring the first element
    incl = inp[1]
    excl = 0
    for i in range(2, len(inp)):
        temp = incl
        incl = max(incl, excl+inp[i])
        excl = temp

    # find max sum from right to left ignoring the last element
    incl1 = inp[len(inp) -2]
    excl1 = 0
    for i in range(len(inp)-3, -1, -1):
        temp1 = incl1
        incl1 = max(incl1, excl1+inp[i])
        excl1 = temp1

    # Maximum of the two is the answer.It guarantees that both first and last element will not be selected together
    return max(incl, incl1)

# given n petrol stations along a circular route. amount of petrol at station i is petrol[i]. you have car with
# unlimited petrol tank and it costs cost[i] of petrol to travel from station i to its next station i+1. you begin the
# journey with empty tank at one of the petrol stations, return the starting petrol station's index if you can travel
# around circuit once , otherwise return -1. time O(n)
class Petrol_Pump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

def tour(inp):
    n = len(inp)
    # consider first petrol pump as starting point and form a queue data structure
    start = 0
    end = 1
    current_petrol = inp[start].petrol - inp[start].distance

    while start!=end or current_petrol<0:

        # while we have not reached the end but the current_petrol has become negative
        while start!=end and current_petrol<0:
            # remove the starting petrol pump and change start
            current_petrol = current_petrol - inp[start].petrol + inp[start].distance
            start = (start+1)%n

            # if we reached petrol pump 0 again, then there is no possible solution
            if start == 0:
                return -1

        # when we have current_petrol as positive and want to move to next petrol pump
        current_petrol = current_petrol + inp[end].petrol - inp[end].distance
        end = (end+1) %n

    return start

arr = [Petrol_Pump(6,4), Petrol_Pump(3,6), Petrol_Pump(7,3)]
print('starting petrol pump possible:', tour(arr))

# Box Stacking: given a set of n rectangular 3D boxes. Dimensions of ith box are height hi, width wi, depth di.
# Create a stack of boxes as tall as possible, but only stack a box on another box if dimensions of 2D base of lower box
# are each strictly larger than those of 2D base of higher box. We can rotate a box so that any side functions as its
# base.It is possible to use multiple instances of same type of box.

# Determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is
# same. Recursive solution, time exponential

# Determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is
# same. Dynamic programming solution, time O(sum X n)

# given symbols 'true', 'false', 'and', 'or', 'xor'. find number of ways to parenthesize the expressions such that it
# evaluates to true.

# All pairs shortest path problem, Floyd's algorithm

# consider a row of n coins of values v1,..., vn, where n is even(since its a 2 player game). We play this game with the
# opponent.In each turn, a player selects either the first or last coin from the row, removes it from the row
# permanently, and receives the value of coin. Determine maximum possible amount of money we can definitely win if we
# move first.

# given a sequence of length n, output length of longest palindrome subsequence. using DP time O(n^2)

# Given 2 strings S and T, find the number of times S appears in T. Need not all characters of S should appear
# contiguous to T. ex: S=ab T=abadcb solution is 4.

# given a matrix with n rows and m columns, each cell has number of apples.start from upper-left corner of matrix, go
# down or right one cell.Finally arrive to bottom-right corner.Find max no. of apples that we can collect. when we pass
# through a cell- we collect all apples left there. time O(nm)

# given a matrix with 0s and 1s, find max size square sub-matrix with all 1s. time O(nm)

# given nXn matrix of +ve and -ve integers, find the sub-matrix with largest possible sum.

# find optimal number of jumps to start from first element to last element, jump length at a time can be atmost the
# value at current position in array. optimum result is reaching in minimum number of jumps.

# given an array of n numbers, find M(i) that indicates max sum over all windows starting at 1 and ending at i.
# condition: not to select three contiguous numbers.

# given a series of matrices A1XA2XA3X...XAn with their dimensions, what is the best way to parenthesize them so that
# it produces minimum number of total multiplications.

# Integer knapsack problem(duplicate items allowed) given n types of items where si is integer size of ith item type,
# vi is its value. We need to fill a knapsack of capacity C with items of maximum value.
# Can add multiple items of same type to the knapsack. time O(nC) space O(C)

# Integer knapsack problem(duplicate items allowed) given n types of items where si is integer size of ith item type,
# vi is its value. We need to fill a knapsack of capacity C with items of maximum value.
# each item is allowed to use for 0 or 1 time.

# Making Change: given n types of coin denominations of values v1<v2<v3...<vn(integers). assume v1 = 1, so that we can
# always make change for any amount of money C. find an algorithm which makes change for an amount of money C with as
# few coins as possible.

# given sequence of n numbers. determine a subsequence(not necessarily contiguous) of max length in which values in
# subsequence form a strictly increasing sequence from position 1 to i.

# given sequence of n numbers. determine a subsequence(not necessarily contiguous) of max length in which values in
# subsequence form a strictly increasing sequence from position i to n.
