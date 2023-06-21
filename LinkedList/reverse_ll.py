#!/usr/bin/python3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    def reverseList(self, head) -> Node:
        curr = head
        new_list = None
        while curr:
            new_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = new_node
        return new_list


# Usage
# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
# print(ll.search(2))  # True
# ll.delete(2)
# print(ll.search(2))  # False
