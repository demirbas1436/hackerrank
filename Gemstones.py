def gemstones(arr):
    new_set = set(arr[0])
    for i in range(1, len(arr)):
        new_set = new_set.intersection(set(arr[i]))
    return len(new_set)
