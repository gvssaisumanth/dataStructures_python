#!/usr/bin/python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reorder-list/description/


class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # at this point slow will be at the middle of the list and fast will be at the end of the list

        # we will be breaking the list in 2 halves

        second = slow.next
        prev = slow.next = None
        # we will be reversing the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # after this the nodes from second till end will be reversed and prev will be pointing to the first one in that seq

        # merge

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # first becomes first.next, second becomes second.next updating the sequence
            first, second = tmp1, tmp2


def main():
    # Creating an instance of Solution class
    solution = Solution()

    # Taking a list of numbers from the user
    numbers = list(
        map(int, input("Enter numbers separated by space: ").split()))

    # Creating a dummy ListNode as the head of the list
    head = ListNode(0)
    current = head

    for number in numbers:
        new_node = ListNode(number)
        current.next = new_node
        current = new_node

    # Dropping the dummy head and setting the actual head of the list
    head = head.next

    # Reordering the list
    solution.reorderList(head)

    # Printing the reordered list
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    main()
