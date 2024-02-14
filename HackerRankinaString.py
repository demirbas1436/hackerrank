def hackerrankInString(s):
    word = "hackerrank"
    toplam = 0
    for i in range(len(s)):
        sought_word = word[toplam]
        if sought_word == s[i]:
            toplam = toplam + 1
        if toplam == len(word):
            return "YES"
    return "NO"