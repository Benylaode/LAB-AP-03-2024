import re

def validasi_nomor_telepon():
    nomor = input("Masukkan nomor telepon: ")
    
    pola = r"^\+62\d{8,12}$"
    
    if re.match(pola, nomor):
        print("Nomor telepon valid")
    else:
        print("Nomor telepon tidak valid")

validasi_nomor_telepon()
