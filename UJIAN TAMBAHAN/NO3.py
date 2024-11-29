from functools import reduce

def jumlah_genap(angka):
    angka_genap = filter(lambda x: x % 2 == 0, angka)
    jumlah = reduce(lambda x, y: x + y, angka_genap)
    return jumlah

n = [1, 2, 3, 4, 5, 6]
output = jumlah_genap(n)
print("Jumlah angka genap:", output)