def weightedUniformStrings(s, queries):
    new_words = set()
    prev = ""
    count = 0
    for c in s:
        ascii = ord(c) - 96
        new_words.add(ascii)
        if c == prev:
            count += 1
            new_words.add(ascii * count)
        else:
            prev = c
            count = 1
    result = []
    for query in queries:
        if query in new_words:
            result.append("Yes")
        else:
            result.append("No")
    return result

#############################################################################################################
# Bir uniform alt string, bir stringin içindeki aynı harflerden oluşan bir alt kümeyi ifade eder.
# Örneğin, s = “abca” ise, bu stringin uniform alt stringleri a, b, c, aa, bc ve aca’dır. Bu alt
# stringlerin ağırlıkları ise, harflerin alfabedeki sıralarına göre belirlenir. Örneğin, a harfinin
# ağırlığı 1, b harfinin ağırlığı 2, c harfinin ağırlığı 3’tür. Bir alt stringin ağırlığı ise, içindeki
# harflerin ağırlıklarının toplamıdır. Örneğin, aa’nın ağırlığı 1 + 1 = 2, bc’nin ağırlığı 2 + 3 = 5,
# aca’nın ağırlığı 1 + 3 + 1 = 5’tir.
#############################################################################################################