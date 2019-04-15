class Singly_List_Node(object):
    def __init__(self, data = None):
        self.data = data
        self.nxt = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, nxt):
        self.nxt = nxt

    def getNext(self):
        return self.nxt

    def hasNext(self):
        return self.nxt != None

class Singly_Linked_List(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def listLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.getNext()

        self.length = count

    def printList(self):
        if self.length == 0:
            print('List is empty')
        curr = self.head
        for i in range(self.length):
            print(curr.data, end= ', ')
            curr = curr.nxt

    def insert_at_beginning(self, data = None):
        newNode = Singly_List_Node(data)
        if self.listLength() == 0:
            self.head =  newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1

    def insert_at_end(self, data = None):
        newNode = Singly_List_Node(data)
        curr = self.head
        while curr.getNext():
            curr = curr.getNext()

        curr.setNext(newNode)
        self.length += 1

    def insert_at_position(self, pos, data = None):
        newNode = Singly_List_Node(data)
        if pos > self.length or pos < 0:
            return None
        elif pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            curr = self.head
            count  = 0
            while count != pos:
                curr = curr.getNext()
                count += 1

            newNode.setNext(curr.getNext())
            curr.setNext(newNode)
            self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            return
        self.head = self.head.getNext()
        self.length -= 1

    def delete_at_position(self, pos):
        if pos > self.length or pos < 0:
            return
        curr = self.head
        prev = self.head
        count = 0
        while curr.getNext() or count < pos:
            count += 1
            if count == pos:
                prev.setNext(curr.getNext())
                self.length -= 1
                return
            prev = curr
            curr = curr.getNext()

    # find nth node from the end of a linked list, length of list is not known
    def nth_from_end(self, nth):
        if not self.head or nth > self.length or nth < 0:
            return None
        else:
            pointer1 = pointer2 = self.head
            moves = 0
            # move nth elements from the head to skip them
            while moves < nth-1:
                moves += 1
                pointer1 = pointer1.nxt

            # move pointer2 till pointer1 reaches the end
            if moves < nth and pointer1.nxt:
                while pointer1.nxt:
                    pointer1 = pointer1.nxt
                    pointer2 = pointer2.nxt
            return pointer2.data

    # find if there is a cycle in the list, if yes then find start node of the loop
    def detect_cycle_in_list(self):
        if not self.head or not self.head.nxt:
            return None
        slowptr = self.head.nxt
        fastptr = slowptr.nxt
        while slowptr != fastptr:
            if not slowptr or not fastptr:
                return False
            slowptr = slowptr.nxt
            fastptr = fastptr.nxt.nxt
        # there is a cycle at slowptr and fastptr location
        return slowptr

    # reverse a singly linked list
    def reverse_list(self):
        if self.head is None:
            return None
        last = None
        curr = self.head
        while curr:
            aftr = curr.nxt
            curr.nxt = last
            last = curr
            curr = aftr
        self.head = last

    # find the intersection point of two lists
    def merging_point(self, list1, list2):

        # difference in lengths of two lists
        diff = abs(list1.length - list2.length)

        # skip diff number of nodes in longer list
        if list1.length >= list2.length:
            longerList = list1
            shorterList = list2
        else:
            longerList = list2
            shorterList = list1

        curr1 = longerList.head

        while diff != 0:
            curr1 = curr1.nxt
            diff -= 1

        curr2 = shorterList.head
        while curr1 and curr2:
            if curr1.data == curr2.data:
                return curr1.data
            curr1 = curr1.nxt
            curr2 = curr2.nxt

        return False

    # find the middle of the list, if we know it has no loop
    # method1: find length of list and compute midpoint, then traverse to the midpoint
    # method2: use slow  and fast pointers
    def middle_point(self):
        fastptr = slowptr = self.head
        while fastptr.nxt:
            slowptr = slowptr.nxt
            fastptr = fastptr.nxt.nxt

        return slowptr

    def swap_elements(self, node1, node2):
        tmp = node2.data
        node2.data = node1.data
        node1.data = tmp

    # reverse linked list in pairs
    def reverse_in_pairs(self):
        if self.head is None:
            return None
        if self.head and self.head.nxt is None:
            return self.head
        curr = self.head
        while curr and curr.nxt:
            self.swap_elements(curr, curr.nxt)
            curr = curr.nxt.nxt

    # find if a list is palindrome or not
    def palindrome_list(self):
        if self.head is None:
            return False
        if self.head.nxt is None:
            return True
        curr = self.head
        lst = []
        count = 0
        while curr:
            lst.append(curr.data)
            count += 1
            curr = curr.nxt

        curr = self.head
        i = count-1
        flag = False
        while curr and i >= 0:
            if curr.data == lst[i]:
                i -= 1
                flag = True
                curr = curr.nxt
            else:
                flag = False
                break
        return flag


    # given list {a1, a2, . . ., an}, return {a1, an, a2, an-1, . . .} without using extra space
        # SOLUTION:
        # find midpoint
        # reverse the list from midpoint to end and attach to midpoint-1
        # point nxt pointers from starting from head to elements starting from midpoint

sll = Singly_Linked_List()
sll.insert_at_beginning(10)
sll.insert_at_position(1, 30)
sll.insert_at_position(2, 50)
sll.insert_at_position(3, 20)
sll.insert_at_position(4, 5)
sll.insert_at_position(5, 70)

sll2 = Singly_Linked_List()
sll2.insert_at_beginning(60)
sll2.insert_at_position(1, 100)
sll2.insert_at_position(2, 40)
sll2.insert_at_position(3, 50)
sll2.insert_at_position(4, 20)
sll2.insert_at_position(5, 5)
sll2.insert_at_position(6, 70)

sll3 = Singly_Linked_List()
sll3.insert_at_position(0, 5)
sll3.insert_at_position(1, 5)
sll3.insert_at_position(2, 5)
print('Palindrome? :', sll3.palindrome_list())

print('intersection point of two lists:', sll.merging_point(sll, sll2))

print('Singly linked list is:', end = ' ')
sll.printList()
print('\nlength of singly linked list:', sll.length)
print('palindrome? :', sll.palindrome_list())
sll.reverse_in_pairs()
print('reverse in pairs:', end = '' )
sll.printList()
sll.reverse_list()
print('\nReverse list:', end = '')
sll.printList()
print('\nprint nth node from end:', sll.nth_from_end(4))
print('Detect cycle in list:', sll.detect_cycle_in_list())

class Doubly_List_Node(object):
    def __init__(self, data = None):
        self.data = data
        self.nxt = None
        self.prev = None

class Doubly_Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def listLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.getNext()

        self.length = count

    def insert_at_beginning(self, data = None):
        newNode = Doubly_List_Node(data)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.nxt = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def insert_at_end(self, data):
        newNode = Doubly_List_Node(data)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.nxt = newNode
            self.tail = newNode
        self.length += 1

    def insert_at_position(self, data, pos):
        newNode = Doubly_List_Node(data)
        if pos < 0 or pos > self.length:
            return
        elif pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            count = 0
            curr = self.head
            while curr or count < pos:
                count += 1
                if count == pos:
                    curr.nxt = newNode
                    newNode.prev = curr
                    self.length += 1
                curr = curr.nxt

class Circular_Linked_List(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def listLength(self):
        curr = self.head
        count = 0
        if not curr:
            self.length = 0
        else:
            while curr != self.head:
                count += 1
                curr = curr.nxt

            self.length = count










