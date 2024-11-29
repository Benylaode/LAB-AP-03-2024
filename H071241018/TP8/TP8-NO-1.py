import re
def validasi_string(d):
    if len(d) != 40:
        return False
    if not re.match(r'^[A-Za-z0-9]{35}', d[:35]):
        return False
    if any(alf.isdigit() and int(alf) % 2 != 0 for alf in d[:35]):
        return False

    if not re.match(r'(1|3|5|7|9){5}$', d[35:]):
        return False
    return True
alif_string = input("Masukkan string: ")
print("True" if validasi_string(alif_string) else "False")
