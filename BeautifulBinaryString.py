def beautifulBinaryString(b):
    total = 0
    while '010' in b:
        total += 1
        b = b.replace("010", "011", 1)

    return total