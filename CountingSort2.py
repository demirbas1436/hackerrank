def countingSort(arr):
    # Write your code here
    count = [0] * (max(arr) + 2)
    for i in range(0, len(arr)):
        count[arr[i]] = count[arr[i]] + 1
    count2 = []
    for i in range(len(count)):
        for j in range(count[i]):
            count2.append(i)
    return count2