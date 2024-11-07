def cek_valid_input(n):
    if type(n) == int and n > 0:
        return True
    else:
        return False

def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n) 
        
        langkah = langkah + 1  
    
    return langkah

input_user = input("Masukan angka: ")

try:
    n = int(input_user)  
    
    if cek_valid_input(n):
        print(f"Jumlah langkah: {hitung_langkah(n)}")
    else:
        print("Input tidak Valid")
except ValueError:
    print("Input tidak Valid")
