def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
try:
    angka1 = float(input("Angka pertama: "))
    angka2 = float(input("Angka kedua: "))
    
    operasi = input("Operasi (+, -, *, /): ")


    if operasi == '+':
        hasil = angka1 + angka2
        print(f"Hasil: {hasil}")
    elif operasi == '-':
        hasil = angka1 - angka2
        print(f"Hasil: {hasil}")
    elif operasi == '*':
        hasil = angka1 * angka2
        print(f"Hasil: {hasil}")
    elif operasi == '/':
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {hasil}")
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")

except ValueError:
    print("Operasi tidak valid. Gunakan +, -, *, atau /.")

kalkulator()
