try:
    umur = int(input("Masukkan umur = "))

    if umur > 0 :
        if umur < 12:
            status = "Anak-anak"
        elif 12 <= umur <= 17 :
            status = "Remaja"
        elif 18 <= umur <= 64:
            status = "Remaja"
        elif umur > 65:
            status = "Lansia"

        print(f"Anda termasuk dalam kategori {status}")
        
    else:
        print("Usia tidak valid")


except:
    print("Inputan tidak valid")
