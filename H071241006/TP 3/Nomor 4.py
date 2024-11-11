total_harga = int(input("Masukkan total harga: "))
uang = int(input("Masukkan uang yang diberikan: "))

pecahan = [50000, 20000, 10000, 5000, 2000, 1000]

kembalian = uang - total_harga

for uang in pecahan:
    if kembalian >= uang:
        jumlah_lembar = kembalian // uang
        kembalian %= uang
        print(f"lembar {uang}: {jumlah_lembar}")

if kembalian < uang:
    print("uang kurang")