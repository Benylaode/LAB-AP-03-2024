def klasifikasi_usia():
    try:
        usia = int(input("Masukkan usia: "))
        
        if usia < 0:
            print("Usia tidak valid. Harap masukkan angka positif.")
        else:
            if usia < 12:
                kategori = "Anak-anak"
            elif 12 <= usia <= 17:
                kategori = "Remaja"
            elif 18 <= usia <= 64:
                kategori = "Dewasa"
            else:
                kategori = "Lansia"
            
            print(f"Anda termasuk dalam kategori {kategori}.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

klasifikasi_usia()
