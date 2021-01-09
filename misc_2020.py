#find whether an integer is palindrome, without converting it to string
def isPalindrome(x):
    new_list = list()
    while x:
        new_list.append(int(x % 10))
        x = x // 10

    x = new_list
    last = len(x) - 1
    first = 0
    while first <= last:
        if x[first] != x[last]: return False
        first += 1
        last -= 1

    return True


print('is palindrome:', isPalindrome(1234321))

# You are given a list of pairs of items(strings), each pair is an association. Return the association group with the
# highest number of elements. If two groups have same size, return the group that has the lexological smallest element
# between these 2. Also while returning the group, return it in a lexological sorted order.
# Sample Input : {{Item0,Item1}, {Item2, Item3}, {Item0, Item4}}
def largestItemAssociation(itemAssociation):
    visited = set(item for items in itemAssociation for item in items)
    n = len(visited)
    parent=[-1]*n
    groups = []

    def find(x):
        if parent[x]<0:
            return x
        else:
            return find(parent[x])

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if xroot == yroot :return
        if abs(parent[xroot]) < abs(parent[yroot]):
            parent[xroot]=yroot
        else:
            parent[yroot]=xroot

    def formGroups(parent):
        for i in range(len(parent)):
            tmp = []
            x = i
            while x != -1:
                tmp.append(x)
                x = parent[x]
            groups.append(tmp)
        groups.sort(key=len, reverse=True)
        # filter out the largest groups only
        maxlen = float('-inf')
        result = []
        for items in groups:
            if len(items)>= maxlen:
                maxlen=len(items)
                result.append(items)
        return result

    for items in itemAssociation:
        for x in range(1, len(items)):
            union(items[x], items[x-1])

    groups = formGroups(parent)
    # sort lexicographically
    for i in groups:
        i.sort()

    return groups[0] # return items first appearing lexicographical order


input = [[1, 0],
         [3, 2],
         [0, 4],
         [2, 5]]
print('largestItemAssociation:',largestItemAssociation(input))

# DP 15 Tushar roy
# Maximum sum rectangular submatrix in 2D matrix, using 2D kadane's solution
# kadane take O(N) time
# time O(ncols*ncols*nrows) space O(nrows)
class Result():
    def __init__(self, maxSum=0, maxleft=0, maxright=0, maxup=0, maxdown=0):
        self.maxSum = maxSum
        self.maxleft = maxleft
        self.maxright = maxright
        self.maxup = maxup
        self.maxdown = maxdown

    def recSubmatrixSum(self, grid):
        nrows= len(grid)
        ncols = len(grid[0])
        tmp = [0]*nrows
        result = Result()
        for left in range(ncols):
            for i in range(nrows):
                tmp[i] = 0
            for right in range(left, ncols):
                for i in range(nrows):
                    tmp[i] += grid[i][right]
                kadaneResult = self.kadane(tmp) # kadaneResult = [maxSum, start, end]
                if kadaneResult[0] > result.maxSum:
                    result.maxSum = kadaneResult[0]
                    result.maxleft = left
                    result.maxright = right
                    result.maxup = kadaneResult[1]
                    result.maxdown = kadaneResult[2]

        return result

    def kadane(self, arr):
        max = 0
        maxStart = -1
        maxEnd = -1
        currStart = 0
        maxSoFar = 0
        for i in range(len(arr)):
            maxSoFar += arr[i]
            if maxSoFar < 0:
                maxSoFar = 0
                currStart = i+1
            if max < maxSoFar:
                maxStart = currStart
                maxEnd = i
                max = maxSoFar

        return [max,maxStart, maxEnd]

input = [[2,  1, -3, -4,  5],
        [0,  6,  3,  4,  1],
        [2, -2, -1,  4, -5],
        [-3,  3,  1,  0,  3]]
result = Result().recSubmatrixSum(input)
print(result.maxSum , result.maxleft ,result.maxright ,result.maxup ,result.maxdown )

# DP 17 Tushar roy
# given jobs with start and end time and profit on finishing the job. what max profit can you make when finish all jobs?
class Job():
    def __init__(self, s=0, e=0, profit =0):
        self.start= s
        self.end = e
        self.profit = profit

def weightedSchedulingProfit(jobs):
    T = [0]*len(jobs)
    jobs.sort(key = lambda x : x.end)
    T[0] = jobs[0].profit
    for i in range(len(jobs)): # initialise
        T[i] = max(T[i-1], jobs[i].profit)
        for j in range(i-1, -1, -1):
            if jobs[j].end <= jobs[i].start: # do not overlap
                T[i] = max(T[i], jobs[i].profit+T[j])
                break
    return max(T)

jobs = [Job()]*9
jobs[0] = Job(1, 3, 5)
jobs[1] = Job(2, 5, 6)
jobs[2] = Job(4, 6, 5)
jobs[3] = Job(6, 7, 4)
jobs[4] = Job(5, 8, 11)
jobs[5] = Job(7, 9, 2)
print(weightedSchedulingProfit(jobs))

# DP 18 Tushar roy
# longest common substring
def longestCommonSubstring(string1, string2):
    T = [[0]*(len(string1)+1) for _ in range(len(string2)+1)]
    maxnumber = 0
    x=y=0
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i-1]== string2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
                if maxnumber < T[i][j]:
                    maxnumber = T[i][j]
    return maxnumber

print(longestCommonSubstring('abcdaf', 'zbcdf')) # returns length of longest common substring

# Implement the Unix find command as an API. Given a path and criteria, print the names of files in the path matching
# the criteria.
#
# Example:
# •	Find all files with size > 5MB
# •	Find all XML files
# •	Find all files modified less than a week ago
#
# Milestones:
# 1.	Able to understand that a File API is needed. Candidate will then be given a File API with helper methods
# (isDirectory, getSize, getChildren, getLastModifiedDate, etc).
# 2.	Come up with basic FileFind API for a single directory. Then able to extend it to perform recursive search.
# 3.	Implement a single criterion a time. Able to understand that various criteria can be abstracted behind a
# FileMatcher interface. Implement the interface and implementations
# 4.	Able to extend from a single criterion at a time to combining criteria (AND/OR)
# 5.	Able to follow symlinks
#
# SDE2 candidate should be able to hit first 3 milestone with minimal guidance and milestone 4 with some help.
# Milestone 5 is a stretch goal for extra signal, but optional.
#





