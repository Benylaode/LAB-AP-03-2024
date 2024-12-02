import random

angka = random.randint(1, 101)

while True :
    try:
        data = int(input("Masukkan tebakan anda (0 untuk berhenti): "))
    except:
        print("Data tidak valid")
        continue
    if data == angka :
        print("Selamat! Anda menebak angka dengan benar")
    elif data > angka:
        print("Angka terlalu besar")
    elif data < angka:
        print("Angka terlalu kecil")
    