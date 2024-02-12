def insertionSort2(n, arr):
    for i in range(1, n):
        anahtar = arr[i]
        j = i-1
        while j >=0 and anahtar < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anahtar
        print(*arr)