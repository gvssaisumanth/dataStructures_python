#!/usr/bin/python3


def partition(array, low, high):
    pivot = array[high]

    i = low-1

    for j in range(low, high):

        if array[j] <= pivot:
            i += 1
            (array[j], array[i]) = (array[i], array[j])
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1


def quickselect(array, k, low, high):

    if low == high:
        return array[low]

    pi = partition(array, low, high)

    if k == pi:
        return array[pi]
    elif k < pi:
        return quickselect(array, k, low, pi-1)
    else:
        return quickselect(array, k, pi+1, high)


array = [7, 4, 6, 3, 9, 1, 2, 10, 8, 5]
k = 4  # if k is 4, we are looking for the 4th largest element
print("K-th smallest element is: ", quickselect(array, k, 0, len(array) - 1))
