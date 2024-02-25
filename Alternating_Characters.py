def alternatingCharacters(s):
    # Write your code here
    toplam = 0
    for i in range(len(s)-1):
        if ord(s[i]) == ord(s[i+1]):
            toplam = toplam + 1
    return toplam