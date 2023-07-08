#!/usr/bin/python3


def merge(l1, l2):

    result = []

    while l1 and l2:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    return result + l1 + l2


def k_way_merge(lists):

    if len(lists) <= 1:
        return lists[0]
    mid = len(lists)//2

    left = k_way_merge(lists[:mid])
    right = k_way_merge(lists[mid:])

    return merge(left, right)


sorted_lists = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(k_way_merge(sorted_lists))
