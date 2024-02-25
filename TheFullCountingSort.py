def countSort(arr):
    for i in range((len(arr) // 2)):
        arr[i][1] = '-'

    strings = {}
    for x, y in arr:
        x = int(x)
        strings.setdefault(x, '')
        strings[x] += ' ' + y

    print(' '.join(strings[x].strip() for x in sorted(strings)))