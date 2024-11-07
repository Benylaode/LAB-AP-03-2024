
def caesar_cipher(teks, pergeseran):
    hasil = ""  
    alfabet = "abcdefghijklmnopqrstuvwxyz"  
    alfabet_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  


    for karakter in teks: 
        if karakter in alfabet:  
            indeks = (alfabet.index(karakter) + pergeseran) % 26
            hasil = hasil + alfabet[indeks]  
        elif karakter in alfabet_besar:
            indeks = (alfabet.index(karakter) + pergeseran) % 26
            hasil = hasil + alfabet_besar[indeks]
        else: 
            hasil = hasil + karakter 
    
    return hasil

teks_input = input("Masukkan String: ")
pergeseran_input = int(input("Masukkan jumlah pergeseran: "))

hasil_cipher = caesar_cipher(teks_input, pergeseran_input)
 
print("Teks:", teks_input)
print("Shift:", pergeseran_input)
print("Cipher:", hasil_cipher)
