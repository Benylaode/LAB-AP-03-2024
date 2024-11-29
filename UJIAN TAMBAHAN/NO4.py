def usia():
    try:
        n = int(input("Masukkan usia: "))
        if n < 0:
            print("Usia tidak valid, input tidak boleh negatif")
        elif n < 12:
            print("Anak-anak")
        elif n <= 17:
            print("Remaja")
        elif n <= 64:
            print("Dewasa")
        else:
            print("Lansia")
    except ValueError:
        print("Usia tidak valid, harap masukkan angka.")

usia()
