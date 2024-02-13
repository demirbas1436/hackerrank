def marsExploration(s):
    # Write your code here
    expected_words = ["S", "O", "S"]
    a = int(len(s)/3)
    b = "".join(expected_words)*a
    fark = 0
    for i in range(len(s)):
        if s[i] != b[i]:
            fark = fark + 1
    return fark