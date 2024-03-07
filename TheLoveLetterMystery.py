def theLoveLetterMystery(s):
    string = list(s)
    res = 0
    first = []
    second = []

    if len(string) % 2 == 1:
#ortadaki eleman sabit iken
        first = list(map(lambda x: ord(x), string[:len(string) // 2]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
    else:
        first = list(map(lambda x: ord(x), string[:len(string) // 2 - 1]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
        res = abs(ord(string[len(string) // 2 - 1]) - ord(string[len(string) // 2]))

    for ind in range(len(first)):
        if first[ind] != second[ind]:
            res = res + abs(first[ind] - second[ind])
            first[ind] = min(first[ind], second[ind])
            second[ind] = first[ind]

    return res