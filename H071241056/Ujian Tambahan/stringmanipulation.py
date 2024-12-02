import itertools

def permutasi(inputan):
    kombinasi = itertools.permutations(inputan)
    lists = []
    for i in kombinasi:
        hasil = "".join(i)
        lists.append(hasil)
    print(sorted(lists))


permutasi("abc")
permutasi("123")



