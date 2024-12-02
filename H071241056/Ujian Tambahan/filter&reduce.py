from functools import reduce

list_angka = [1,2,3,4,5,6]
genap = list(filter(lambda i : i%2 == 0, list_angka))

jumlah = reduce(lambda i, j: i+j, genap)
print(jumlah)
