import re

def validasi_nomor_telepon(nomor):
    pola = r'\+62[0-9]{8,12}$'
    if re.match(pola, nomor):
        return True
    else:
        return False
nomor_telepon = input('Masukkan nomor telepon: ')
if validasi_nomor_telepon(nomor_telepon):
    print('Nomor telepon valid')
else:
    print('Nomor telepon tidak Valid')
