#!/usr/bin/python3


# Given the head of a linked list, remove the nth node from the end of the list and return its head


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # reverse the list
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        k = 1
        second = prev
        if n == 1:
            prev = prev.next
        while second:
            if k+1 == n and second.next:
                second.next = second.next.next
            elif k+1 == n and second.next is None:
                second.next = None
            second = second.next
            k += 1

        # rearrange it back

        order = None
        while prev:
            next_node = prev.next
            prev.next = order
            order = prev
            prev = next_node
        return order


def main():
    # User input for linked list elements
    list_data = input(
        "Enter linked list elements separated by space: ").split()
    n = int(input("Enter the position from the end to remove: "))

    # Create the linked list from user inputs
    dummy_head = ListNode()
    current = dummy_head
    for val in list_data:
        current.next = ListNode(int(val))
        current = current.next

    # Instantiate the Solution object and apply the removal function
    sol = Solution()
    updated_head = sol.removeNthFromEnd(dummy_head.next, n)

    # Print out the updated linked list
    current = updated_head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    main()
