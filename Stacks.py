from collections import deque
from queue import Queue


class Stack(object):
    def __init__(self):
        self.stack = []
        self.stack_limit = 100

    def push(self, data):
        if len(self.stack) != self.stack_limit:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    # reverse elements of stack using only stack operations
    def reverseStack(self, st):
        s = Stack()
        i = 0
        length = len(st)
        while i < length:
            s.push(st.pop())
            i += 1
        return s.stack

    # implement producer consumer problem


stck = Stack()
stck.push(20)
stck.push(30)
stck.push(10)
stck.push(50)
stck.push(60)
print('stack is :', stck.stack)
print('reversed stack is :', stck.reverseStack(stck.stack))

# maximum number in sliding window
# solution 1: use 2 loops , time O(n^2)
# solution 2: use double ended queue , time O(n)
def max_num_sliding_window(inp, k):
    # store the current window elements in q, store the positions in q
    q = deque()
    n = len(inp)
    # first window
    for i in range(k):
        # remove all elements smaller than current ith element
        while q and inp[q[-1]] < inp[i]:
            q.pop()

        # then add current ith position to rear of q
        q.append(i)

    # windows from k to n-1
    for i in range(k, n):
        # print the element at front of q because its the largest from previous window
        print(str(inp[q[0]]), end= ',')
        # remove the elements out of the current window
        while q and q[0] <= i-k:
            # remove from front of q
            q.popleft()
        # remove all elements smaller than current ith element
        while q and inp[q[-1]] < inp[i]:
            q.pop()
        # then add current ith position to rear of q
        q.append(i)

    # print max element of last window
    print(str(inp[q[0]]))

print('sliding window maximum:', end =' ')
max_num_sliding_window([12, 1, 78, 90, 57, 89, 56], 3)

# replace every element with the nearest greater element on the right
# solution 1: use 2 loops , time O(n^2)
# solution 2: start from right side of array, time O(n)
def nearest_right_greater(inp):
    n = len(inp)
    # for last element there is no greatest on right, so -1
    max_frm_right = inp[-1]
    inp[n - 1] = -1
    for i in range(n-2, -1, -1):
        if max_frm_right < inp[i]:
            tmp = inp[i]
            inp[i] = max_frm_right
            max_frm_right = tmp
        else:
            inp[i] = max_frm_right
    return inp

print('leaders in the array or greatest from right for each element:', nearest_right_greater([16, 17, 4, 3, 5, 2]))

# find largest rectangle under histogram
# stack based solution, time O(n)
def largest_rectangle(hist):
    n = len(hist)

    # stack holds the indices of hist bars, in increasing order of their heights
    stck = list()
    max_area = area = 0
    indx = 0

    # loop through hist
    while indx < n:
        # append the bar to stack if it is higher than the top of stack
        if not stck or hist[indx] > hist[stck[-1]]:
            stck.append(indx)
            indx += 1
        # if this bar is lower than the top of stack then calculate the area of rectangle with stack top as smallest bar
        else:
            stck_top = stck.pop()
            if stck:
                area = hist[stck_top] * (indx - stck[-1] - 1)
            else:
                area = hist[stck_top] * indx

            # update max area
            max_area = max(max_area, area)

    # now pop remaining bars from stack and calculate area with popped bar as smallest
    while stck:
        stck_top = stck.pop()
        if stck:
            area = hist[stck_top] * (indx - stck[-1] - 1)
        else:
            area = hist[stck_top] * indx

        # update max area
        max_area = max(max_area, area)

    return max_area

print('largest rectangle in histogram:', largest_rectangle([6, 2, 5, 4, 5, 1, 6]))

# implement a stack using 2 queues
# two ways to do this: way 1 : make push operation costly
# make sure that newly entered element is always at the front of ‘q1’
class MakeStack1(object):
    def __init__(self):
        # two inbuilt queues
        self.q1 = Queue()
        self.q2 = Queue()
        # maintain current number of elements
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        # Push x first in empty q2
        self.q2.put(x)
        # transfer all remaining elements from q1 to q2
        while not self.q1.empty():
            # dequeue() from q1 and enqueue to q2()
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # swap the names of two queues
        q = self.q1
        self.q1 = self.q2
        self.q2 = q

    def pop(self):
        if self.q1.empty():
            return
        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.curr_size

# implement a stack using 2 queues
# way 2: make pop operation costly
# In push operation, the new element is always enqueued to q1. In pop() operation, if q2 is empty then all the
# elements except the last, are moved to q2. Finally the last element is dequeued from q1 and returned.
class MakeStack2(object):
    def __init__(self):
        # two inbuilt queues
        self.q1 = Queue()
        self.q2 = Queue()
        # maintain current number of elements
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        # enqueue() new element to q1
        self.q1.put(x)

    def pop(self):
        if self.q1.empty():
            return -1
        if self.q2.empty():
            while self.q1.qsize() != 1:
                self.q2.put(self.q1.queue[0])
                self.q1.get()

        tmp = self.q1.queue[0]
        self.q1.get()
        self.curr_size -= 1
        # swap the names of two queues
        q = self.q1
        self.q1 = self.q2
        self.q2 = q
        return tmp

    def top(self):
        return self.pop()

    def size(self):
        return self.curr_size


# Driver Code
if __name__ == '__main__':
    s = MakeStack1()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print('make stack using 2 queues with push operation heavy:',end=' ')
    while s.size() != 0:
        print(s.top(), end=', ')
        s.pop()

    s = MakeStack2()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print('\nmake stack using 2 queues with pop operation heavy:', end =' ')
    while s.size()!= 0:
        print(s.top(), end=', ')
