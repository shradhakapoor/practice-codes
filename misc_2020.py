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
