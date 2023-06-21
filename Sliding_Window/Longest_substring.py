# Given a string s, find the length of the longest
# substring
# without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# https://www.youtube.com/watch?v=qtVh-XEpsJo

def longestSubstringSet(s) -> int:
    hashSet = set()
    left = 0
    max_c = 0

    for r in range(len(s)):
        char = s[r]
        while char in hashSet:
            hashSet.remove(char)
            left+=1
        hashSet.add(char)
        max_c = max(max_c, r-left+1)
    return max_c





def longestSubstring(s) -> int:
    hashTable = {}
    left = 0
    max_c = 0

    for r in range(len(s)):
        char = s[r]
        if char in hashTable:
            left = max(hashTable[char]+1, left)

        hashTable[char] = r
        max_c = max(max_c, r-left+1)
    return max_c
