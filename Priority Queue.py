# implementing priority queue using Arrays
class Node(object):
    def __init__(self, key_value = None, priority_value = None):
        self.key_value = key_value
        self.priority_value = priority_value


class Priority_Queue(object):
    def __init__(self):
        self.items = []

    def is_empty( self ):
        return len(self.items) == 0

    # size of priority queue
    def pqueue_size( self ):
        return len(self.items)

    # insert data with priority key
    def enqueue( self, key_value, priority_value ):
        newnode = Node(key_value, priority_value)
        self.items.insert(0, newnode)
        self.prioritize_items()

    # print queue
    def print_pqueue( self ):
        if not self.is_empty():
            for node in self.items:
                print ('key:', node.key_value, '  priority:', node.priority_value)

    # delete elements with a given key
    def dequeue_given_key( self, key ):
        for i in range(self.pqueue_size()):
            if self.items[i].priority_value == key:
                self.items[i].priority_value = None
        self.prioritize_items()

    # arrange the elements in order of their priorities, smaller priority no. to larger
    # used Bubble sort - very inefficient
    def prioritize_items( self ):
        isSorted = False
        lastUnsorted = self.pqueue_size() - 1
        while not isSorted:
            isSorted = True
            for i in range(lastUnsorted):
                j = i+1
                if self.items[i].priority_value is None:
                    continue
                while self.items[j].priority_value is None:
                    j += 1
                if self.items[i].priority_value > self.items[(j)].priority_value:
                    self.items[i].priority_value, self.items[(j)].priority_value =\
                        self.items[(j)].priority_value, self.items[i].priority_value
                    isSorted = False
            lastUnsorted -= 1

    # delete Min - delete element with smallest key. smallest key means max priority
    def dequeue_min_key( self ):
        if not self.is_empty():
            return self.items.pop(0)

    # delete Max - delete element with largest key. largest key means min priority
    def dequeue_max_key( self ):
        if not self.is_empty():
            return self.items.pop((self.pqueue_size()-1))

    # return kth smallest key
    def kth_smallest_key( self, k ):
        return self.items[k-1]


pq = Priority_Queue()
pq.enqueue(10, 1)
pq.enqueue(22, 5)
pq.enqueue(200, 4)
pq.enqueue(45, 4)
pq.enqueue(55, 3)
pq.enqueue(45, 7)

pq.print_pqueue()

p = pq.dequeue_max_key()
print('\nDequeue element with max key(least priority)', str(p.priority_value))
pq.print_pqueue()

p = pq.dequeue_min_key()
print('\nDequeue element with min key(highest priority)', str(p.priority_value))
pq.print_pqueue()

print('kth smallest priority element:', str(pq.kth_smallest_key(3).key_value))

print('\nDequeue given key:', end= '\n')
pq.dequeue_given_key(4)
pq.print_pqueue()


