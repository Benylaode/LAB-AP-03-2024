import reduce
angka = list(map(int, input('Masukkan list angka (pisahkan dengan spasi): ').split()))
angka_genap = list(filter(lambda x: x % 2 == 0, angka))
jumlah_genap = reduce(lambda x, y: x + y, angka_genap)
print('Jumlah angka genap:', jumlah_genap)