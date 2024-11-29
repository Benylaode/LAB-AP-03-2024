from functools import reduce

angkaList = [1, 2, 3, 4, 5, 6]
angkaGenap = list(filter(lambda i: i % 2 == 0, angkaList))
jumlahGenap = reduce(lambda a, b: a + b, angkaGenap)
print(f"Jumlah angka genap: {jumlahGenap}")