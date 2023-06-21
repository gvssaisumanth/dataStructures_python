#!/usr/bin/python3


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def mergetwo(self, l1, l2) -> Node:
        dummy = Node()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next  # since dummy is pointing to empty node whose initial value is 0


def create_sorted_linked_list(lst):
    head = None
    for val in lst:
        if not head or val < head.val:
            new_node = Node(val)
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next and current.next.val < val:
                current = current.next
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node
    return head


def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def main():
    # Create an instance of Solution
    solution = Solution()

    # Accept user input for two lists of numbers
    list1 = list(map(int, input(
        "Enter numbers for the first list, separated by space: ").split()))
    list2 = list(map(int, input(
        "Enter numbers for the second list, separated by space: ").split()))

    # Create sorted linked lists from the input lists
    l1 = create_sorted_linked_list(list1)
    l2 = create_sorted_linked_list(list2)

    # Merge the sorted linked lists
    merged_list = solution.mergetwo(l1, l2)

    # Print the merged and sorted linked list
    print("Merged and sorted linked list:")
    print_linked_list(merged_list)


if __name__ == "__main__":
    main()
