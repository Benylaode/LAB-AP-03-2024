from itertools import permutations
def unik_permutations(s):
    perm = permutations(s)
    unik_perm = sorted(set([''.join(p) for p in perm]))
    return unik_perm
Hasil = unik_permutations
print(Hasil(input(':')))

