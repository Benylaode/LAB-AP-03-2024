import re

def validate_string(s):
    if len(s) != 45:
        return False
    if not re.match(r'^[A-Za-z02468]{40}', s[:40]):
        return False
    if not re.match(r'[13579\s]{5}$', s[-5:]):
        return False
    return True

string = input("Masukkan string: ")
print("True" if validate_string(string) else "False")