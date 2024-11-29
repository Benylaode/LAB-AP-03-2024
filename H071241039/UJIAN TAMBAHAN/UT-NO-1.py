try:
    n = int(input("masukan tinggi segitiga: "))
    if n <= 0:
        print("tinggi segitiga harus positif")
    else:
        for i in range(n, 0, -1):
            print("*" * i)
except:
    print("tidak valid, masukkan angka.")