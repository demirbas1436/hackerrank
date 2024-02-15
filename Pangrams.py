def pangrams(s):
    new_list = []
    s = s.lower()
    for i in range(len(s)):
        if s[i] not in new_list and not s[i] == " ":
            new_list.append(s[i])
    if len(new_list)==26:
        return "pangram"
    else:
        return "not pangram"