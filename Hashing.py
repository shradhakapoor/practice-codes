from collections import *

# implement separate chaining collision resolution technique. Perform insert, search, delete operations.
# solution: add a new element to the list of values linked to the key

# given a singly linked list, check whether it has any loop in it
# solution1: using hash table, if any key is visited again then return True
# solution2: Floyd's cycle-finding algorithm


class singly_ll_Node(object):
    def __init__(self, value = 0):
        self.value = value
        self.next = None


class singly_ll(object):
    def __init__(self, value):
        self.head = singly_ll_Node(value)

    def cycle_singly_linkedlist(self, list_head):
        slow_pointer = list_head
        fast_pointer = list_head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True

        return False


singly_linked_list = singly_ll(10)
singly_linked_list.head.next = singly_ll_Node(20)
singly_linked_list.head.next.next = singly_ll_Node(30)
singly_linked_list.head.next.next.next = singly_linked_list.head
print('Check whether there is loop in singly linked list:',
    singly_linked_list.cycle_singly_linkedlist(singly_linked_list.head))


# given m sets of integers that have n elements in them. Find an element that appeared in maximum number of sets
def find_frequent_number_in_sets(sets):
    def defvalue():
        return None
    number_set_map = defaultdict(defvalue)
    setcount = 0
    # key= number, value = list of set numbers it appeared in
    for row in sets:
        rowsize = len(row)
        setcount += 1
        for i in range(rowsize):
            item = row[i]
            if number_set_map[item] is None:
                number_set_map[item] = []
                number_set_map[item].append(setcount)
            else:
                number_set_map[item].append(setcount)

    max_count = float('-inf')
    max_num = float('inf')
    for key, val in number_set_map.items():
        if max_count < len(val):
            max_count = len(val)
            max_num = key

    return max_num


print('Element that appeared in maximum sets:', find_frequent_number_in_sets([[1,1,1,2,3], [1,1,2,2,2,2,3], [1,1,1]]))


# remove the specified characters from a given string which are present in another string
def remove_specified_chars(mainstring, markstr):
    mainstring = list(mainstring)
    markstr = list(markstr)
    # key= character of mark string, value= its count
    def defvalue():
        return None
    markchartocountmap= defaultdict(defvalue)

    for ch in markstr:
        if markchartocountmap[ch] is None:
            markchartocountmap[ch] = 1
        else:
            markchartocountmap[ch] += 1

    # process each char of mainstring and if it is not in markchartocountmap then add it to result
    result = ''
    for ch in mainstring:
        if ch not in markchartocountmap.keys() or markchartocountmap[ch] == 0:
            result += ch

    return result


print('Removing specified characters from main string:', remove_specified_chars('Shradha is good girl', 'is'))


# find first non-repeated character in a string, time O(n)
def first_non_repeated_char(mainstring):
    mainstring = list(mainstring.lower())
    # key= character, value=(count, first position it was seen)
    def defvalue():
        return None
    charcountmap = defaultdict(defvalue)
    for i in range(len(mainstring)):
        if charcountmap[mainstring[i]] is None:
            charcountmap[mainstring[i]] = (1, i)
        else:
            charcountmap[mainstring[i]] = (charcountmap[mainstring[i]][0]+1, charcountmap[mainstring[i]][1])

    for key,value in charcountmap.items():
        if value[0] == 1:
            return key

    return None


print('First non-repeated character in  string:', first_non_repeated_char('Shradha is a good girl'))
