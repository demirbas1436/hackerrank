def countingSort(arr):
    count = [0] * 100
    for i in range(0, len(arr)):
        count[arr[i]] = count[arr[i]] + 1
    return count


################################################################################################
# count = [0] * 100 =  100 elemanlı ve tüm elemanları 0 olan bir sayma dizisi oluşturur.
# Girdi dizisindeki her eleman için, sayma dizisindeki ilgili indeksteki değeri bir artırır.
################################################################################################