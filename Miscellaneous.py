import math


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
    visited = [[False for x in range(m)]for y in range(n)]
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

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.
def maxArea(height):
    n = len(height)
    s = 0
    e = n - 1
    mxarea = min(height[s], height[e]) * (n - 1)

    while s < e:
        mxarea = max(mxarea, (min(height[s], height[e]) * (e - s)))
        if height[s] <= height[e]:
            s += 1
        else:
            e -= 1

    return mxarea

print('Max area is:', maxArea([3,2,1,3]))

# Given a list of numbers, return all possible permutations.
#
# Input: [1, 2, 3]
# Output:
# [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 1, 3],
#     [2, 3, 1],
#     [3, 1, 2],
#     [3, 2, 1]
# ]
#

def permutations(inp):
    n = len(inp)
    if n == 0:
        return None
    if n == 1:
        return inp

    result = []

    for i in range(n):
        ans = inp[i]
        newList = inp[:i] + inp[i + 1:]
        for j in permutations(newList):
            result.append([ans] + [j])

    return result

print('permutations of all numbers:', permutations([1, 2, 3]))

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
# a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# given an integer list of which both first half and second half are sorted independently. Sort the two parts to create
# one single sorted linked list in place [do not use extra memory]

# given array S[1...n], reverse(s,i,j) which reverses order of elements between positions i and j

# given a matrix, calculate number of ways for reaching from A to B.

# given a string that has set of words and spaces, write program to move spaces to front of string. you need to traverse
# the array only once and need to adjust the string in place.

# given a string that has set of words and spaces, write program to move spaces to end of string. you need to traverse
# the array only once and need to adjust the string in place.

# Save all leaf nodes of a Binary tree in a Doubly Linked List by using
#  Right node as Next node and Left Node as Previous Node.

# Given an array,find the maximum j – i such that arr[j] > arr[i]

# Remove Alternate Duplicate characters from a char array you have to do it in Place.
# Like keeping only the odd occurences of each character.
# Example: Input: “you got beautiful eyes”
# Output: ”you gtbeaiful es”

# Find all nodes at k-distance from a given node in a binary tree

# Clone a linked list with next and random pointer

# Return a tree such that each internal node stores sum of all its child nodes. Each leaf node stores zero.

# Reversal of Linked List in groups of K.

# Check whether given binary tree is balanced or not.
# Definition is no two leaves should have height difference of greater than one.

# Remove duplicates from string in place in O(n).

# Given two sorted arrays (with repetitive elements) find the kth minimum number from both arrays.

# Find an element in a rotated array

# The cost of a stock on each day is given in an array, find the max profit that you can make by buying and
# selling in those days.For example, if the given array is {100, 180, 260, 310, 40, 535, 695}
# the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6.
# If the given array of prices is sorted in decreasing order, then profit cannot be earned at all

# Given a binary search tree , print the path which has the sum equal to k and has minimum hops.
# i.e if there are multiple paths with the sum equal to k then print the path with minimum number of nodes.

# Given an array, arrange the elements such that the number formed by concatenating the elements is highest.
# E.g.: input = [9, 93, 24, 6], the output should be: [9,93,6,24]. This is because if you concatenate all the numbers,
# 993624 is the highest number that can be formed. Given a string, find the longest substring which is palindrome.

# Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

# Given string s and string t find whether all permutation of t is present as substring in s.

# Given an array which is first strictly increasing and then strictly decreasing. Find an element in this array.

# Given a string example : shoppingwithamazoniseasy,
# we are given this string and a dictionary containing valid words , now we need to break
# the sentence into words separated by space. Output : shopping with amazon is easy

# You are given a mapping like a -> 1, b-> 2… z-> 26.
# You have to print all possible combinations of a given number using the above information.
# eg : input : 121 output : aba,la,au

# Get the next bigger number using the same digits of a number.
# Eg, For 123456, next number would be 123465

# Given a string with repeated characters, rearrange characters in a string so that no two adjacent characters are same.
# Note : It may be assumed that the string has only lowercase English alphabets.
# Examples: Input: aaabc Output: abaca; Input: aaabb Output: ababa; Input: aa Output: Not Possible;
# Input: aaaabc Output: Not Possible

# This problem is known as Clock angle problem. we need to find angle between hands of an analog clock at a given time.
# Examples:Input:  h = 12:00, m = 30.00 Output: 165 degree; Input:  h = 3.00, m = 30.00 Output: 75 degree

# Fresh is a grocery delivery service that offers consumers the option of purchasing their groceries online and
# schedule future deliveries of purchased groceries. Fresh's backend system dynamically tracks each Fresh delivery truck
# and automatically assigns the next deliveries in a truck's plan. To accomplish this, the system generates an optimized
# delivery plan with X destinations. The most optimized plan would deliver to the closest X destinations from the start
# among all of the possible destinations in the plan.Given an array of N possible delivery destinations,
# implement an algorithm to create the delivery plan for the closest X destinations.
# Input
# The input to the function/method consists of three arguments:
# numDestinations, an integer representing the total number of possible delivery destinations for the truck (N);
# allLocations, a list where each element consists of a pair of integers representing the x and y coordinates of the delivery locations;
# numDeliveries, an integer representing the number of deliveries that will be delivered in the plan (X).
# Output
# Return a list of elements where each element of the list represents the x and y integer coordinates of the delivery destinations.
# Constraints
# numDeliveries ≤ numDestinations
# Note
# The plan starts from the truck’s location [0, 0]. The distance of the truck from a delivery destination (x, y) is the
# square root of x2 + y2. If there are ties then return any of the locations as long as you satisfy returning X deliveries.
# Example
# Input:
# numDestinations = 3
# allLocations = [[1, 2], [3, 4], [1, -1]]
# numDeliveries = 2
# Output: [[1, -1], [1, 2]]
# Explanation:
# The distance of the truck from location [1, 2] is square root(5) = 2.236
# The distance of the truck from location [3, 4] is square root(25) = 5
# The distance of the truck from location [1, -1] is square root(2) = 1.414
# numDeliveries is 2, hence the output is [1, -1] and [1, 2].
def computeDistance(x, y):
    return math.sqrt((x*x) + (y*y))

def deliveryPlan(numDestinations, allLocations, numDeliveries):
    if numDestinations <  numDeliveries:
        return None
    # find distance of all locations from (0,0)
    distMap= dict()
    for p in allLocations:
        dist = computeDistance(p[0], p[1])
        if distMap.get(dist) is None:
            distMap[dist] = [p]
        else:
            distMap[dist].append(p)

    # sort the calculated distances in increasing order
    sortedDist = sorted(distMap.keys())
    # return the co-ordinates of the first #numDeliveries distances
    res = []
    for i in range(numDeliveries):
        res.append(distMap[sortedDist[i]][0])

    return res

print('Delivery plan:', deliveryPlan(3, [[1, 2], [3, 4], [1, -1]], 2 ))

# You are in charge of preparing a recently purchased lot for a new building. The lot is covered with trenches and has
# a single obstacle that needs to be taken down before the foundation can be prepared for the building. The demolition
# robot must remove the obstacle before progress can be made on the building. Write an algorithm to determine the
# minimum distance required for the demolition robot to remove the obstacle.
# Assumptions:
# The lot is flat, except for trenches, and can be represented as a two-dimensional grid.
# The demolition robot must start from the top-left corner of the lot, which is always flat, and can move one block up,
# down, left, or right at a time.
# The demolition robot cannot enter trenches and cannot leave the lot.
# The flat areas are represented as 1, areas with trenches are represented by 0 and the obstacle is represented by 9.
# Input
# The input to the function/method consists of three arguments:
# numRows, an integer representing the number of rows;
# numColumns, an integer representing the number of columns;
# lot, representing the two-dimensional grid of integers.
# Output
# Return an integer representing the minimum distance traversed to remove the obstacle else return -1.
# Constraints
# 1 ≤ numRows, numColumns ≤ 1000
# Example
# Input:
# numRows = 3
# numColumns = 3
# lot =
# [[1, 0, 0],
# [1, 0, 0],
# [1, 9, 1]]
# Output:
# 3
# Explanation:
# Starting from the top-left corner, the demolition robot traversed the cells (0,0) -> (1,0) -> (2,0) -> (2,1).
# The robot traversed the total distance 3 to remove the obstacle.
# So, the output is 3.
def obstacleDistance(numRows, numCols, lot):
    # mark the cells with trench(0) as visited
    visited = [[False for x in range(numCols)]for y in range(numRows)]
    for i in range(numRows):
        for j in range(numCols):
            if lot[i][j] == 0:
                visited[i][j] = True

    # start from position (0,0) and BFS from start to destination(9)
    q = [] # This list works as a Queue
    # mark start as visited
    start = (0, 0, 0)  # (distance from start, row, col coordinates)
    visited[0][0] = True
    q.insert(0, start) #enqueue

    while len(q) != 0:
        tmp = q.pop()

        # if obstacle found, return the distance of this cell from start cell
        if lot[tmp[1]][tmp[2]]== 9:
            return tmp[0]

        # moving down
        if tmp[1] + 1< numRows and not visited[tmp[1]+1][tmp[2]]:
            q.insert(0,(tmp[0]+1, tmp[1]+1, tmp[2]))
            visited[tmp[1]+1][tmp[2]] = True

        # moving up
        if 0 <= tmp[1] - 1 < numRows and not visited[tmp[1]-1][tmp[2]]:
            q.insert(0,(tmp[0]+1, tmp[1]-1, tmp[2]))
            visited[tmp[1]-1][tmp[2]] = True

        # moving right
        if tmp[2] + 1 < numCols and not visited[tmp[1]][tmp[2]+1]:
            q.insert(0,(tmp[0]+1, tmp[1], tmp[2]+1))
            visited[tmp[1]][tmp[2]+1] = True

        # moving left
        if 0 <= tmp[2] - 1< numCols and not visited[tmp[1]][tmp[2]-1]:
            q.insert(0,(tmp[0]+1, tmp[1], tmp[2]-1))
            visited[tmp[1]][tmp[2]-1] = True

    return -1


print(' Minimum distance to obstacle:', obstacleDistance(3, 3,
[[1, 1, 1],
[0, 1, 1],
[1, 9, 1]]))

# ABC is partnering with the linguistics department at a local university to analyze important works of English
# literature and identify patterns in word usage across different eras. To ensure a cleaner output, the linguistics
# department has provided a list of commonly used words (e.g., "an", "the", etc.) to exclude from the analysis. In the
# context of this search, a word is an alphabetic sequence of characters having no whitespace or punctuation.
# Write an algorithm to find the most frequently used word in the text excluding the commonly used words.
# Input
# The input to the function/method consists of two arguments -
# literatureText, a string representing the block of text;
# wordsToExclude, a list of strings representing the commonly used words to be excluded while analyzing the word frequency.
# Output
# Return a list of strings representing the most frequently used word in the text or in case of a tie, all of the most
# frequently used words in the text.
# Note
# Words that have a different case are counted as the same word.
# The order of words does not matter in the output list.
# All words in the wordsToExclude list are unique.
# Any character other than letters from the English alphabet should be treated as white space.
# Example
# Input:
# literatureText =“Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill’s favorite food.”
# wordsToExclude = ["and", "he", "the", "to", "is", "Jack", "Jill"]
# Output:
# ["cheese", “s”]
# Explanation:
# The word “and” has a maximum of three frequency but this word should be excluded while analyzing the word frequency.
# The words “Jack”, “Jill”, “s”, "to" and "cheese” have the next maximum frequency(two) in the given text but the words
#  “Jack”, "to" and “Jill” should be excluded as these are commonly used words which you are not interested to include.
# So the output is ["cheese", “s”] or [“s”, "cheese"] as the order of words does not matter.
def mostFrequentWords(literatureText, wordsToExclude):
    literatureText = literatureText.split()
    for w in range(len(wordsToExclude)):
        wordsToExclude[w] = wordsToExclude[w].lower()

    frq = dict() # key: frequency, value: list of words
    words = dict() # key: word, value: frequency
    for word in literatureText:
        word = word.lower()
        if word not in wordsToExclude and word.isalnum():
            if words.get(word) is None:
                words[word] = 1
            else:
                words[word] += 1

    for k, v in words.items():
        if frq.get(v) is None:
            frq[v] = [k]
        else:
            frq[v].append(k)

    sortedF = sorted(frq.keys(), reverse = True)
    return frq[sortedF[0]]

print('Most frequent words:', mostFrequentWords(
"Jack and Jill went to the market to buy bread and cheese . Cheese is Jack ' s and Jill ' s favorite food .",
    ['and', 'he', 'the', 'to', 'is', 'Jack', 'Jill'] ))

# You have been given a task of reordering some data from a log file. In the log file, every line is a space-delimited
# list of strings; all lines begin with an alphanumeric identifier. There will be no lines consisting only of an
# identifier.
# After the alphanumeric identifier, a line will consist of either:
# - a list of words using only lowercase English letters,
# - or list of only integers.
# You have to reorder the data such that all of the lines with words are at the top of the log file. The lines with
# words are ordered lexicographically, ignoring the identifier except in the case of ties. In the case of ties
# (if there are two lines that are identical except for the identifier), the identifier is used to order
# lexicographically. Alphanumeric should be sorted in ASCII order (numbers come before letters). The identifiers must
# still be part of the lines in the output Strings. Lines with integers must be left in the original order they were in
# the file. Write an algorithm to reorder the data in the log file, according to the rules above.
# Input
# The input to the function/method consists of two argument -
# logFileSize, an integer representing the number of log lines;
# logLines, a list of strings representing the log file.
# Output
# Return a list of strings representing the reordered log file data.
# Note
# Identifier consists of only lower case english character and numbers.
# Example
# Input:
# logFileSize = 5
# logLines =
# [a1 9 2 3 1]
# [g1 act car]
# [zo4 4 7]
# [ab1 off key dog]
# [a8 act zoo]
# Output:
# [g1 act car]
# [a8 act zoo]
# [ab1 off key dog]
# [a1 9 2 3 1]
# [zo4 4 7]
# Explanation:
# Second, fourth, and fifth lines are the lines with words. According to the lexicographical order, the second line will
# be reordered first in the log file, then fifth, and the fourth comes in the log file. Next, the lines with numbers
# come in the order in which these lines were in the input.

# Michelle has created a word game for her students. The word game begins with Michelle writing a string and a number,
# K, on the board. The students must find a substring of size K such that there is exactly one character that is
# repeated once; in other words, there should be K – 1 distinct characters in the substring.
# Write an algorithm to help the students find the correct answer. If no such substring can be found, return an empty
# list; if multiple such substrings exist, return all of them, without repetitions. The order in which the substrings
# are returned does not matter.
# Input
# The input to the function/method consists of two arguments -
# inputString, representing the string written by the teacher;
# num, an integer representing the number, K, written by the teacher on the board.
# Output
# Return a list of all substrings of inputString with K characters, that have K-1 distinct character i.e. exactly one
# character is repeated, or an empty list if no such substring exists in inputString. The order in which the substrings
# are returned does not matter.
# Constraints
# The input integer can only be greater than or equal to 0 and less than or equal to 26 (0 ≤ num ≤ 26)
# The input string consists of only lowercase alphabetic characters.
# Examples
# Input:
# inputString = awaglk
# num = 4
#
# Output:
# [awag]
#
# Explanation:
# The Substrings are {awag, wagl, aglk}
# The answer is awag as it has 3 distinct characters in a string of size 4, and only one character is repeated twice.

# You are working on developing a movie with Amazon Video that consists of a series of shots: short pieces of video
# from a particular camera angle. You want to devise an application to easily group identical shots in a video into
# scenes (a sequence of shots). Shots are identical when they are labeled with the same letter, and everything in
# between identical shots is considered part of same scene. There is already an algorithm that breaks the video up
# into shots and labels them.
# Write a function which will partition a sequence of shot labels into minimal subsequences so that a shot label
# only appears in a single subsequence. The output should be the length of each subsequence.
# Input
# The input to the function/method consists of an argument -
# inputList, a list of characters representing the sequence of shots.
#
# Output
# Return a list of integers representing the length of each scene, in the order in which it appears in the given
# sequence of shots.
#
# Examples
# Example 1:
# Input
# inputList = [a, b, c]
#
# Output
# [1, 1, 1]
#
# Explanation:
# Because there are no recurring shots, all shots can be in the minimal length 1 subsequence.
#
# Example 2:
# Input
# inputList = [a, b, c, a]
#
# Output
# [4]
#
# Explanation:
# Because ‘a’ appears more than once, everything between the first and last appearance of ‘a’ must be in the same list.
# Example 3:
# Input:
# inputList = [a, b, a, b, c, b, a, c, a, d, e, f, e, g, d, e, h, i, j, h, k, l, i, j]
#
# Output:
# [9, 7, 8]