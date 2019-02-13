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









