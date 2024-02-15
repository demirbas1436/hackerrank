def quickSort(arr):
    pivot = arr[0]
    less = []
    greater = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            less.append(arr[i])
        if arr[i] > pivot:
            greater.append(arr[i])

    return less + [pivot] + greater