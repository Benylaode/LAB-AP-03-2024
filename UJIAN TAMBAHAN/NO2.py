import itertools

def mutasi(s):
    permutasi = set(itertools.permutations(s))
    permutasi_str = [''.join(p) for p in permutasi]
    return sorted(permutasi_str)

n = "abc"
output = mutasi(n)
print(output)
