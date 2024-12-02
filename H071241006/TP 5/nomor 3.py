def hitung_penghapusan_anagram(string1, string2):
    frekuensi1 = [0] * 26  
    frekuensi2 = [0] * 26 
    
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
    for huruf in string1:
        indeks = alfabet.index(huruf)  
        frekuensi1[indeks] = frekuensi1[indeks] + 1

    for huruf in string2:
        indeks = alfabet.index(huruf)  
        frekuensi2[indeks] = frekuensi2[indeks] + 1
    
    penghapusan = 0
    for i in range(26):
        selisih = abs(frekuensi1[i] - frekuensi2[i])
        penghapusan = penghapusan + selisih
    
    return penghapusan

string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

hasil = hitung_penghapusan_anagram(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")
