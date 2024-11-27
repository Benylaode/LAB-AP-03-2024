def anagram(x, y):
    x = sorted(x)
    y = sorted(y)
    
    v1, v2 = 0, 0 
    dihapus = 0

    while v1 < len(x) and v2 < len(y):

        if x[v1] == y[v2]:
            v1 += 1
            v2 += 1
        elif x[v1] < y[v2]:
            dihapus += 1
            v1 += 1
        else:
            dihapus += 1
            v2 += 1
    
    dihapus += len(x) - v1
    dihapus += len(y) - v2

    return dihapus

s1 = input("kata1 : ")
s2 = input("kata2 : ")
print(f"huruf yang dihapus : {anagram(s1,s2)}")



# def jumlah_penghapusan_anagram(s1, s2):
#   """
#   Fungsi untuk menghitung jumlah minimum penghapusan karakter agar dua string menjadi anagram.

#   Args:
#     s1: String pertama.
#     s2: String kedua.

#   Returns:
#     Jumlah minimum penghapusan karakter.
#   """

#   # Hapus karakter non-alfanumerik
#   s1 = ''.join(filter(str.isalnum, s1)).lower()
#   s2 = ''.join(filter(str.isalnum, s2)).lower()

#   # Hitung frekuensi huruf
#   freq1 = {}
#   for char in s1:
#     freq1[char] = freq1.get(char, 0) + 1

#   freq2 = {}
#   for char in s2:
#     freq2[char] = freq2.get(char, 0) + 1

#   # Hitung jumlah penghapusan
#   total_hapus = 0
#   for char in freq1:
#     total_hapus += abs(freq1[char] - freq2.get(char, 0))
#   for char in freq2:
#     if char not in freq1:
#       total_hapus += freq2[char]

#   return total_hapus

# # Contoh penggunaan
# s1 = input("kata: ")
# s2 = input("kata: ")
# hasil = jumlah_penghapusan_anagram(s1, s2)
# print(hasil)  # Output: 4