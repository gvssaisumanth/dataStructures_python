#!/usr/bin/python3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False


# Usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(ll.search(2))  # True
ll.delete(2)
print(ll.search(2))  # False
