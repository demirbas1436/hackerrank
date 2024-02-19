def funnyString(s):
    ascii_list = []
    ascii_list2 = []
    kelimeler = s.split()
    ters_kelimeler = [kelime[::-1] for kelime in kelimeler]
    ters_string = " ".join(ters_kelimeler)

    for i in range(len(s)):
        ascii_list.append(ord(s[i]))
    for i in range(len(ters_string)):
        ascii_list2.append(ord(ters_string[i]))
    print(ascii_list)
    print(ascii_list2)
    fark_list = []
    fark_list2 = []
    for i in range(0, len(ascii_list) - 1):
        fark_list.append(abs(ascii_list[i] - ascii_list[i + 1]))
    for i in range(0, len(ascii_list2) - 1):
        fark_list2.append(abs(ascii_list2[i] - ascii_list2[i + 1]))
    if fark_list == fark_list2:
        return "Funny"
    else:
        return "Not Funny"