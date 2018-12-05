from collections import defaultdict


# Implement Trie to insert, search, delete a string
class TrieNode(object):
    def __init__(self, label = None, data = None):
        self.label = label
        self.data = data

        def defvalue():
            return None
        # key= character, value= list of other trie nodes or end_of_word node
        self.children = defaultdict(defvalue)

    def add_child(self, key, data=None):
        if not isinstance(key, TrieNode):
            self.children[key] = TrieNode(key, data)
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


    # def search_string(self, inp):
    #     inp = list(inp.lower())
    #     curr_node = self.head


trie = Trie()
words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
for word in words.split():
    trie.insert_string(word)


# Implement Ternary Search Tree to insert, search, delete a string, Displaying all words of Tree

# Implement Suffix Tree to insert, search, delete a string

# Given a paragraph of words, find the word which appears maximum times. (use heap amd tries combination)

# Given 2 strings, find the longest common substring, using suffix tree, time O(m+n)

# Given text T, find the substring of T which is longest palindrome, using suffix tree

# Reverse a string, time O(n), space O(n)

# Reverse a string without using any temporary variable, time O(n), space O(1)

# give an algorithm for matching pattern in text. Assume ? and * are wildcard chars.Brute Force. time O(mn) space O(1)

# Reverse words in a sentence. time O(mn) space O(1)

# Print all permutations of a string(anagrams)

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
