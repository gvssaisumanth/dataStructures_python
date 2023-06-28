#!/usr/bin/python3


def partition(array, low, high):
    pivot = array[high]

    i = low-1

    for j in range(low, high):

        if array[j] <= pivot:
            i += 1

            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1


def findkthlargest(array, k, low, high):

    if low == high:
        return array[low]

    pi = partition(array, low, high)

    k_abs = len(array)-pi

    if k_abs == k:
        return array[pi]

    if k_abs < k:
        return findkthlargest(array, k, low, pi-1)
    if k_abs > k:
        return findkthlargest(array, k, pi+1, high)


array = [7, 4, 6, 3, 9, 1, 2, 10, 8, 5]
k = 4  # if k is 4, we are looking for the 4th largest element
print("K-th largest element is: ", findkthlargest(array, k, 0, len(array) - 1))
