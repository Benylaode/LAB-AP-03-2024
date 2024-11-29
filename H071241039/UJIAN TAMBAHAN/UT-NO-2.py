from itertools import permutations

def permutasi(input_string):
    kombinasi = sorted(set((''.join(p) 
    for p in permutations(input_string))))
    return kombinasi

input_string = "abc"
output = permutasi(input_string)
print(output)