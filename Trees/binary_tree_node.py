#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.data = data
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node)
        else:
            print("Value is already present in tree.")

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.print_preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.print_inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.print_postorder(self.root, "")
        else:
            print("Such traversal" + str(traversal_type) + "is not defined")

    def print_preorder(self, start, traversal):
        """Root -> Left ->Right"""
        if start:
            traversal += (str(start.data) + " - ")
            traversal = self.print_preorder(start.left, traversal)
            traversal = self.print_preorder(start.right, traversal)
        return traversal

    def print_inorder(self, start, traversal):
        '''Left -> Root -> Right'''
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += (str(start.data)+"-")
            traversal = self.print_inorder(start.right, traversal)
        return traversal

    def print_postorder(self, start, traversal):
        '''Left -> Right -> Root'''
        if start:
            traversal = self.print_postorder(start.left, traversal)
            traversal = self.print_postorder(start.right, traversal)
            traversal += (str(start.data)+"-")
        return traversal



if __name__ == "main":
    print("hey theree")
    # Set up tree
    tree = BinaryTree(10)  # Creates a root node with value 10
    tree.insert(5)  # Adds a node with value 5
    tree.insert(15)  # Adds a node with value 15
    tree.insert(3)  # Adds a node with value 3
    tree.insert(7)  # Adds a node with value 7
    print("Pre-Order" + " " + tree.print_tree("preorder"))
    print("InOrder" + " " + tree.print_tree("inorder"))
    print("postOrder" + " " + tree.print_tree("postorder"))
