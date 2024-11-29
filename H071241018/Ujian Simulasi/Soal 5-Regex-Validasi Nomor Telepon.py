import re
def valid_nomor_telepon(nomor):
    #pola
    if re.match( nomor):
        return True
    else:
        return False
nomor_telepon = input('Masukkan nomor telepon: ')
if valid_nomor_telepon(nomor_telepon):
    print('Nomor telepon valid')
else:
    print('Nomor telepon tidak Valid')

