def runningTime(arr):
    toplam = 0
    for i in range(1, len(arr)):
        anahtar = arr[i]
        j = i-1
        while j >=0 and anahtar < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            toplam = toplam + 1
        arr[j+1] = anahtar
    return toplam