from itertools import permutations

def permutasi_unik(s):
    return sorted(set(''.join(p) for p in permutations(s)))

input_string = "abc"
print(permutasi_unik(input_string))
