import re

n = input("masukan nomor telepon indonesia: ")
pattern = r"^\+62\d{8,12}$"
if re.fullmatch(pattern, n):
    print("nomor telepon valid")
else:
    print("nomor telepon tidak valid")