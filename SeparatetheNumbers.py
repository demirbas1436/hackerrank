def separateNumbers(s):
    if len(s)==1:
        print("NO")
        return
    for i in range(1, len(s)//2+1):
        genstr = s[:i]
        prev = int(genstr)
        while len(genstr) < len(s):
             sonraki = prev+1
             genstr+=str(sonraki)
             prev = sonraki
        if genstr == s:
            print("YES", s[:i])
            return
    print("NO")