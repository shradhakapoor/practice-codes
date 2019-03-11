from collections import defaultdict


# Implement Trie to insert, search a string
class TrieNode(object):
    def __init__(self, label = None, data = None):
        self.label = label
        self.data = data

        def defvalue():
            return None
        # key= character, value= list of other trie nodes or end_of_word node
        self.children = defaultdict(defvalue)

    def add_child(self, key, data=None):
        # if the key is not a TrieNode
        if not isinstance(key, TrieNode):
            self.children[key] = TrieNode(key, data)
        # else if key is a Trienode
        else:
            self.children[key.label] = key


class Trie(object):
    def __init__(self):
        self.head = TrieNode()

    def insert_string(self, inp):
        word = inp
        inp = list(inp.lower())
        curr_node = self.head
        end_of_inp = True
        i = 0
        # move till the inp already exists in Trie
        while i < len(inp):
            if inp[i] in curr_node.children:
                curr_node = curr_node.children[inp[i]]
                i += 1
            else:
                end_of_inp = False
                break

        # for every new character, create a new child node
        if not end_of_inp:
            while i < len(inp):
                curr_node.add_child(inp[i])
                curr_node = curr_node.children[inp[i]]
                i += 1

        # store full word at end node to avoid travel back to get whole word
        curr_node.data = word

    def search_string(self, inp):
        if inp == '' or inp is None:
            return False

        inp = list(inp.lower())
        curr_node = self.head
        word_found = True
        i = 0
        while i < len(inp):
            if inp[i] in curr_node.children:
                curr_node = curr_node.children[inp[i]]
                i += 1
            else:
                word_found = False
                break

        # check further if we found single letter word which is actually not a word in our Trie
        if word_found:
            if curr_node.data is None:
                word_found = False

        return word_found

    # returns all words in Trie that start with prefix
    def words_with_prefix(self, prefx):
        result = []
        if not prefx:
            raise ValueError('Provide not-null prefix')

        prefx = list(prefx.lower())
        curr_node = self.head
        word_found = True
        i = 0
        while i < len(prefx):
            if prefx[i] in curr_node.children:
                curr_node = curr_node.children[prefx[i]]
                i += 1
            else:
                # prefix not in Trie, go no further
                return result

        # get words under prefix, perform BFS (it will return words ordered in increasing length)
        if curr_node == self.head:
            queue = [node for key, node in curr_node.children.items()]
        else:
            queue = [curr_node]

        while queue:
            curr_node = queue.pop()
            if curr_node.data is not None:
                result.append(curr_node.data)

            queue += [node for key, node in curr_node.children.items()]

        return result


trie = Trie()
words = 'She is not as an ass'
for word in words.split():
    trie.insert_string(word)

print('Search for string in Trie:', trie.search_string('ass'))
print('Print all words with prefix:', trie.words_with_prefix('a'))


# Implement Ternary Search Tree to insert, search, delete a string, Displaying all words of Tree
class TSTNode(object):
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.midNode = None # same as equal node
        self.rightNode = None
        self.end_of_word = False


class TST(object):
    def __init__(self, data):
        self.head = TSTNode(data)

    def insert_string(self, curr_node, inp):
        if len(inp) == 0:
            return curr_node

        frst = inp[0]
        rem = inp[1:]
        if curr_node is None:
            curr_node = TSTNode(frst)

        if frst < curr_node.data:
            curr_node.leftNode = self.insert_string(curr_node.leftNode, inp)
        elif frst > curr_node.data:
            curr_node.rightNode = self.insert_string(curr_node.rightNode, inp)
        else:
            if len(rem) == 0:
                curr_node.end_of_word = True
            else:
                curr_node.midNode = self.insert_string(curr_node.midNode, rem)

        return curr_node

    def search_string(self, curr_node, inp):
        if curr_node is None or len(inp) == 0:
            return False

        frst = inp[0]
        rem = inp[1:]

        if frst < curr_node.data:
            return self.search_string(curr_node.leftNode, inp)
        elif frst > curr_node.data:
            return self.search_string(curr_node.rightNode, inp)
        else:
            if len(rem) == 0 and curr_node.end_of_word:
                return True
            else:
                return self.search_string(curr_node.midNode, rem)

    def display_all_words(self, curr_node, result):
        if curr_node:
            # traverse left subtree
            self.display_all_words(curr_node.leftNode, result)

            # store data of this node
            result.append(curr_node.data)
            if curr_node.end_of_word:
                result.append(';')

            # traverse equal/mid subtree
            self.display_all_words(curr_node.midNode, result)

            # traverse right subtree
            self.display_all_words(curr_node.rightNode, result)


ternary_st = TST('c')
ternary_st.insert_string(ternary_st.head, 'cat')
ternary_st.insert_string(ternary_st.head, 'cats')
ternary_st.insert_string(ternary_st.head, 'rat')
ternary_st.insert_string(ternary_st.head, 'at')
print('Search string in Ternary Search Tree:',ternary_st.search_string(ternary_st.head, 'at'))
res = []
ternary_st.display_all_words(ternary_st.head, res)
print('Display all words in Ternary Search Tree:', res )


def compare(inpp, inpt):
    eq = 0
    k = 0

    while k < len(inpp):
        if inpt[k] in inpp:
            eq = 1
        else:
            eq = 0
            break
        k += 1
    return eq


# Print all permutations of a string(anagrams)
def anagrams(txt, pattern):
    txt = list(txt.lower())
    pattern = list(pattern.lower())
    m = len(pattern)
    n = len(txt)
    if m is None or n is None:
        return

    # current txt window
    i = 0
    j = m-1
    windw = txt[i:j+1]

    while j < n:
        # if pattern is same as current txt window then print current txt window
        if compare(pattern, windw):
            for c in range(i, j+1):
                print(txt[c], end=' ')
            print()
        i += 1
        j += 1
        if j < n-1:
            windw.pop(0)
            windw.append(txt[j])


print('All Anagrams of given string:', anagrams('BACDGABCDA', 'ABCD'))

# Implement Suffix Tree to insert, search, delete a string

# Given a paragraph of words, find the word which appears maximum times. (use heap amd tries combination)

# Given 2 strings, find the longest common substring, using suffix tree, time O(m+n)

# Given text T, find the substring of T which is longest palindrome, using suffix tree

# Reverse a string, time O(n), space O(n)

# Reverse a string without using any temporary variable, time O(n), space O(1)
# def reverse_string_without_temp(inp):
#     inp = list(inp.lower())
#     # idea: to use XOR
#     # XOR properties:  x^0 = x, x^1 = -x, x^x = 0
#     start = 0
#     end = len(inp) -1
#     while start < end:
#         inp[start] ^= int(inp[end])
#         inp[end] ^= int(inp[start])
#         inp[start] ^= int(inp[end])
#         start += 1
#         end -= 1
#
#     return inp
#
# print('Reverse string without using temporary variable:', reverse_string_without_temp('shradha'))


# Find the longest common prefix in given list of strings
def longestCommonPrefix(strs):
    res = ''
    n = len(strs)
    flag = 0
    if n == 0:
        return res
    elif n == 1:
        return strs[0]
    else:
        smallest = len(min(strs, key=len))
        for i in range(smallest):
            ch = ''
            for j in range(n):
                if j == 0:
                    ch = strs[j][i]
                else:
                    if ch != strs[j][i]:
                        flag = 0
                        break
                    elif j == n - 1 and ch == strs[j][i]:
                        flag = 1
                        res += ch
            if flag == 0:
                return res

    return res

print('Longest common prefix:', longestCommonPrefix(['flowers','flow','flight']))

# give an algorithm for matching pattern in text. Assume ? and * are wildcard chars.Brute Force. time O(mn) space O(1)

# Reverse words in a sentence. time O(mn) space O(1)

# Print all combinations of a string

# Given a string 'ABCCBCBA', recursively remove adjacent characters if they are same.
# for example, ABCCBCBA->ABBCBA->ACBA

# Given a set of characters C and input string I, find minimum window in I that contains all chars in C.
# example: I = ABBACBAA, C = AAB has minimum window BAA

# Given 2 strings s1, s2. print all interleavings of s1, s2. Assume all chars in s1, s2 are different

# Given a matrix nXn containing random numbers. Check whether the rows match with columns. use suffix tree.

# Replace all spaces with '%20'. Assume string has sufficient space at end of string to hold additional characters.

# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all
# 'O's into 'X's in that surrounded region.
