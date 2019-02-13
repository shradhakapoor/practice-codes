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
        while curr:
            curr = curr.getNext()

        curr.setNext(newNode)
        self.length += 1

    def insert_at_position(self, data = None, pos):
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
        if not self.head:
            return None
        else:
            pointer1 = pointer2 = self.head
            moves = 0
            # move nth elements from the head to skip them
            while moves < nth:
                moves += 1
                pointer1 = pointer1.nxt
            # move pointer2 till pointer1 reaches the end
            if moves == nth and pointer1.nxt is not None:
                while pointer1.nxt:
                    pointer2 = pointer2.nxt
            return pointer2

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

    # find the merging point of two lists
    def merging_point(self, list1, list2):
        if not list1 or list2:
            return None
        list_hash = dict()
        curr = list1.head
        while curr:
            if list_hash.get(curr)  is None:
                list_hash[curr] = True
                curr = curr.nxt

        # check the addresses of list2 in keys of dict()
        list1_keys = list_hash.keys()
        curr = list2.head
        while curr:
            if curr in list1_keys:
                return curr
            else:
                curr = curr.nxt

        return None

    # find the middle of the list, if we know it has no loop
    # method1: find length of list and compute midpoint, then traverse to the midpoint
    # method2: use slow  and fast pointers
    def middle_point(self)
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










