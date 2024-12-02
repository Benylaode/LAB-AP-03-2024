n = int(input("Masukkan tinggi segitiga = "))

if n > 0:
    for i in range(n):
        a = "*" * (n-i)
        print(a)
    
else:
    print("Tinggi Segitiga harus positif")