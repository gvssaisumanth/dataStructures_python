#!/usr/bin/python3


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char not in Map:
                stack.append(char)
            else:
                # we are checking if stack is empty or stack[-1] the last appended element is corresponding opening one
                # if either case fails balanced paranthesis failed
                if not stack or stack[-1] != Map[char]:
                    return False
                stack.pop()
        return True if not stack else False
