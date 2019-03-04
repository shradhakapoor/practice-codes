# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
# It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1.
# How to maximize total profit if only one job can be scheduled at a time. Examples:
# Input: Four Jobs with following deadlines and profits
#   JobID    Deadline      Profit
#     a        4            20
#     b        1            10
#     c        1            40
#     d        1            30
# Output: Following is maximum profit sequence of jobs
#         c, a
#
#
# Input:  Five Jobs with following deadlines and profits
#    JobID     Deadline     Profit
#      a         2           100
#      b         1           19
#      c         2           27
#      d         1           25
#      e         3           15
# Output: Following is maximum profit sequence of jobs
#         c, a, e


def mergeSort(inp):
    #splitting
    if len(inp) > 1:
        mid = len(inp) // 2
        lft = inp[:mid]
        rgt = inp[mid:]

        mergeSort(lft)
        mergeSort(rgt)

        #merging
        i = j = k = 0
        while i < len(lft) and j < len(rgt):
            if lft[i][2] > rgt[j][2]:
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

    return inp


def maximizeProfit(inp, maxDeadline):
    # inp has tuples of (jobId, deadline, profit)
    n = len(inp)
    # sort jobs based on profit in decreasing order - merge sort
    sorted_inp = mergeSort(inp)
    # start with first job of sorted inp
    j = 0
    result = [sorted_inp[0]]
    # add a new job to result if its deadline is >= last added job in result
    for i in range(1, n):
        if sorted_inp[i][1] >= result[j][1]:
            result.append(sorted_inp[i])
            j += 1

    return result


print('Maximized profit:', maximizeProfit(
    [['a', 4, 20],
       ['b', 1, 10],
       ['c', 1, 40],
       ['d', 1, 30]], 4))


# print matrix elements in spiral order
def matrix_in_spiral(mat):
    m = len(mat[0]) # end index of col
    n = len(mat) # end index of row
    result = []
    row = 0 # start index of rows
    col = 0 # start index of cols

    while row < n and col < m:
        # print first row from remaining rows
        for i in range(col, m):
            result.append(mat[row][i])
        # increment start index of row
        row += 1

        # print last column from remaining columns
        for i in range(row, n):
            result.append(mat[i][m-1])
        # decrement end index of cols
        m -= 1

        # print last row of remaining rows
        if row < n:
            for i in range(m-1, col-1, -1):
                result.append(mat[n-1][i])
            # decrement end index of rows
            n -= 1

        # print first column from remaining columns
        if col < m:
            for i in range(n-1, row-1, -1):
                result.append(mat[i][col])
            # increment start index of cols
            col += 1

    return result

print('spiral matrix:', matrix_in_spiral(
    [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18] ] ))

# shuffle the deck of cards
# A deck of cards has 13 cards each of 4 suits: heart(♥), spade(♠), diamond(♦), club(♣).
# Construct unshuffled deck by using two lists, one for suits, another for cardValues.Shuffle the deck by
# iterating over all cards one by one using their indexes, and swapping the index with any random index.

import random

suits = ['♠', '♥', '♦', '♣']
cardValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# initializing an empty deck
deck = []

# CONSTRUCTING AN UNSHUFFLED DECK
for suit in suits:
    for value in cardValues:
        deck.append(value + suit)
# printing the unshuffled deck
print('The original deck of cards:\n', deck)


# SHUFFLING CARDS: iterating over all cards one by one using their indexes, swapping the index with any random index
# Iterate over all cards one by one using their indexes
for index in range(0, len(deck)):
    randomCardForSwitching = random.randrange(len(deck))
    # Swapping indexes
    temp = deck[index]
    deck[index] = deck[randomCardForSwitching]
    deck[randomCardForSwitching] = temp
# printing the shuffled deck
print('The shuffled deck of cards:\n', deck)

# Rotate array A of size n and d elements rotate(A[], d, n)
# solution1: Store d elements in a temp array,  Shift rest of the arr[], Store back the d elements,
# Time complexity : O(n), Auxiliary Space : O(d)
# solution2: rotate one by one, Time complexity : O(n * d), Auxiliary Space : O(1)

# Find the number of islands
# Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
#
# Example:
#
# Input : mat[][] = {{1, 1, 0, 0, 0},
#                    {0, 1, 0, 0, 1},
#                    {1, 0, 0, 1, 1},
#                    {0, 1, 0, 0, 0},
#                    {1, 0, 1, 0, 1}

def isSafe(mat, visited, x, y):
    m = len(visited[0])
    n = len(visited)
    if 0 <= x < m and 0 <= y < n and not visited[x][y] and mat[x][y]:
        return True
    return False

def dfs(mat, visited, i, j):
    r_neighbrs = [1, -1, 0, 0, -1, -1, 1, 1]
    c_neighbrs = [0, 0, 1, -1, 1, -1, -1, 1]
    visited[i][j] = True
    for x in range(len(r_neighbrs)):
        if isSafe(mat, visited, i+r_neighbrs[x], j+c_neighbrs[x]):
            dfs(mat, visited, i+r_neighbrs[x], j+c_neighbrs[x])

    return visited

def numberOfIslands(mat):
    m = len(mat[0])
    n = len(mat)
    visited = [[False, False, False, False, False],
               [False, False, False, False, False],
               [False, False, False, False, False],
               [False, False, False, False, False],
               [False, False, False, False, False]]
    islands = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and not visited[i][j]:
                islands += 1
                visited = dfs(mat, visited, i, j)

    return islands

print('Number of islands:', numberOfIslands(
        [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]))

# add two positive numbers without using '+'
def base2(inp):
    res = 0
    i = 1
    while inp > 1:
        inp = inp//2
        rem = inp % 2
        res = int(pow(10,i)* rem) + res
        i += 1

    return res

def add_bitwise(a, b):
    a = bin(a)
    b = bin(b)
    carry = (a & b) << 1
    sum = 0
    while carry != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry

    return base2(sum)

# print('add two numbers without using +:', add_bitwise(10, 20))



# given an integer list of which both first half and second half are sorted independently. Sort the two parts to create
# one single sorted linked list in place [do not use extra memory]

# given array S[1...n], reverse(s,i,j) which reverses order of elements between positions i and j

# find anagrams in dictionary

# given a matrix, calculate number of ways for reaching from A to B.

# given a string that has set of words and spaces, write program to move spaces to front of string. you need to traverse
# the array only once and need to adjust the string in place.

# given a string that has set of words and spaces, write program to move spaces to end of string. you need to traverse
# the array only once and need to adjust the string in place.


