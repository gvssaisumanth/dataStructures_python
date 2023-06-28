#!/usr/bin/python3


def partition(array, low, high,):
    pivot = array[high]

    i = low-1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            (array[i], array[j]) = (array[j], array[i])
    # by the end of the loop the i will be at i-1 postion of the pivot
    # meaning the sorted position of pivot is i+1 since pivot is high we swap them
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1


def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        # sort left side of the array

        quicksort(array, low, pi-1)

        # sort right side of the array

        quicksort(array, pi+1, high)
    print(array)
