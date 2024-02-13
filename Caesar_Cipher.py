def caesarCipher(s, k):
    new_words = []
    for c in s:
        ascii = ord(c)
        if ascii in range(65, 91):
            ascii = ascii + k
            if ascii not in range(65, 91):
                ascii = 65 + (ascii - 91) % 26
            new_words.append(chr(ascii))
        elif ascii in range(97, 123):
            ascii = ascii + k
            if ascii not in range(97, 123):
                ascii = 97 + (ascii - 123) % 26
            new_words.append(chr(ascii))
        else:
            new_words.append(chr(ascii))
    return "".join(new_words)