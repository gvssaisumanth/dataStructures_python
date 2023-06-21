#!/usr/bin/python3

'''
given certain set of strings you have to written number of occurences of that string

eg: apple, apple, apps, apps,

apple:2, apps:2

app:4,

countwordsend()
countstartswith()
erase() to erase a word
'''


class TireNode:
    def __init__(self) -> None:
        self.children = {}
        self.cntendwith = 0
        self.cntprefix = 0


class Trie:
    def __init__(self) -> None:
        self.root = TireNode()

    def insert(self, word):
        '''
        insert(word): Adds a word to the trie. It iterates through each character in the word, creating new nodes as necessary to represent each character. When it reaches the end of the word, it marks the last node as the end of a word.
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TireNode()
                node.cntprefix += 1
            node = node.children[char]
        node.cntendwith += 1

    def countwordsequal(self, word) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.cntendwith

    def countwordsstartwith(self, word) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.cntprefix

    def erase(self, word):
        nodes = [self.root]
        # for i in nodes:
        #     self.print_trie(i)
        for char in word:
            if char in nodes[-1].children:
                nodes.append(nodes[-1].children[char])
            else:
                return
        if nodes[-1].cntendwith > 0:
            for node in reversed(nodes):
                node.cntprefix -= 1
            nodes[-1].cntendwith -= 1

    def print_trie(self, node=None, word=""):
        if node is None:
            node = self.root

        if node.cntendwith > 0:
            print(f"Word: {word}, count: {node.cntendwith}")

        for char in node.children:
            self.print_trie(node.children[char], word+char)


# Initialize a Trie
trie = Trie()

# Insert words into the Trie
trie.insert("hello")
trie.insert("help")
trie.insert("hell")
trie.insert("dog")
trie.insert("cat")
trie.insert("apple")
trie.insert("apps")
trie.insert("apple")
trie.insert("apps")


print(trie.countwordsequal("apple"))
print(trie.countwordsequal("apps"))

print("starts with")
print(trie.countwordsstartwith("apps"))
print(trie.countwordsstartwith("hel"))

trie.erase("apps")

print("equal with")
print(trie.countwordsequal("apps"))
