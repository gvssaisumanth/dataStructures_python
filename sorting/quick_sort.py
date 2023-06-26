

def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([9, 7, 2, 1, 4, 5, 10, 1, 2, 45, 7, 4, 1]))
print(quick_sort([10, 11, 1, 2, 4, 13, 9, 5, 3]))
