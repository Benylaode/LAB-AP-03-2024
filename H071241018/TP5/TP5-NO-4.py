def substring(x) :
    n = len(x)
    print("Selamat Menikmati")
    for a in range(1, n+1):  
        for b in range(n - a + 1):  
            print(s[b:b+a])

s = input("Input your string: ")
substring(s)
