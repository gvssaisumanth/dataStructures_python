#!/usr/bin/python3

import heapq


def k_way_merge(lists):
    min_heap = []

    for i in range(len(lists)):

        if lists[i]:

            # min_heap, value, index
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    print(min_heap)
    sorted_list = []
    while min_heap:
        val, list_idx, ele_idx = heapq.heappop(min_heap)

        sorted_list.append(val)

        if ele_idx + 1 < len(lists[list_idx]):
            heapq.heappush(
                min_heap, (lists[list_idx][ele_idx+1], list_idx, ele_idx+1))

    return sorted_list


sorted_lists = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(k_way_merge(sorted_lists))


'''
In this code, we first create a min heap with the first elements of each list. 
We then repeatedly remove the smallest element from the heap, 
Add it to the sorted list, and add the next element from the same list to the heap (if there is one). 
This is done until the heap is empty, at which point we have a fully sorted list.
'''
