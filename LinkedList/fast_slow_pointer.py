#!/usr/bin/python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
        return False


def main():
    # User input for linked list elements
    list_data = input(
        "Enter linked list elements separated by space: ").split()

    # Create the linked list from user inputs
    dummy_head = ListNode()
    current = dummy_head
    for val in list_data:
        current.next = ListNode(int(val))
        current = current.next

    # Introduce a cycle for testing
    if dummy_head.next and dummy_head.next.next:
        current.next = dummy_head.next.next

    # Instantiate the Solution object and apply the hasCycle function
    sol = Solution()
    has_cycle = sol.hasCycle(dummy_head.next)

    # Print out whether the linked list has a cycle
    if has_cycle:
        print("The linked list has a cycle.")
    else:
        print("The linked list doesn't have a cycle.")


if __name__ == "__main__":
    main()
