import re

nomor = input("Masukkan Nomor Telepon(+62) = ")

pattern = r"^\+62\d{8,12}$"
if re.fullmatch(pattern, nomor):
    print("Nomor telepon Valid")
else:
    print("Nomor tidak valid")