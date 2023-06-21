#!/usr/bin/python3

'''
What is a Trie?
Trie is a very useful data structure. It is commonly used to represent a dictionary for looking up words in a vocabulary.

For example, consider the task of implementing a search bar with auto-completion or query suggestion. 
When the user enters a query, the search bar will automatically suggests common queries starting with the characters input by the user.
Trie is a tree-like data structure made up of nodes. 
Nodes can be used to store data. Each node may have none, one or more children. 
When used to store a vocabulary, each node is used to store a character, and consequently each "branch" of the trie represents a unique word. 
The following figure shows a trie with five words (was, wax, what, word, work) stored in it.
'''

'''
This is also called as Prefix Tree
'''


class TrieNode:
    '''Defining class for a Trie Node'''

    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:

    ''' Defining a Trie by initializing with TrieNode'''

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        '''
        insert(word): Adds a word to the trie. It iterates through each character in the word, creating new nodes as necessary to represent each character. 
        When it reaches the end of the word, it marks the last node as the end of a word.
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def print_tree(self):
        node = self.root
        for k, v in node.children.items():
            print(k, v)


# Initialize a Trie
trie = Trie()

# Insert words into the Trie
trie.insert("hello")
trie.insert("help")
trie.insert("hell")
trie.insert("dog")
trie.insert("cat")

# print the tree
trie.print_tree()

# Search for some words
print(trie.search("hello"))  # returns True
# returns False because 'hel' is not a complete word in the Trie
print(trie.search("hel"))
print(trie.search("cat"))    # returns True
print(trie.search("doggy"))  # returns False because 'doggy' is not in the Trie

# Check if Trie starts with a prefix
# returns True because 'hel' is a prefix for 'hello' and 'hell'
print(trie.starts_with("hel"))
# returns True because 'do' is a prefix for 'dog'
print(trie.starts_with("do"))
# returns True because 'ca' is a prefix for 'cat'
print(trie.starts_with("ca"))
