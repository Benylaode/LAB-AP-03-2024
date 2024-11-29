usia = input("masukkan usia: ")

usia = int(usia)
if usia < 0:
    print("usia tidak boleh negatif atau bukan angka")
else:
    if usia < 12:
        kategori = "anak-anak"
    elif 12 <= usia <= 17:
        kategori = "remaja"
    elif 18 <= usia <= 64:
        kategori = "dewasa"
    else:
        kategori = "lansia"
        
print(f"anda termasuk dalam kategori {kategori}")