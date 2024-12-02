import re

def validasi_string(S):
    if len(S) != 45:
        return False
    
    pola = r'^[A-Za-z02468]{40}[13579\s]{5}$'
    
    if re.match(pola, S):
        return True
    else:
        return False

input = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 99"

print(validasi_string(input))  
