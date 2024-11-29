n = int(input(": "))
if n <= 0:
    print("Tinggi segitiga harus positif.")
else:
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            print(' ' * (n - i - 1) + '* ' * i)
    else: 
        for i in range(n - 1, 0, -1):
            print(' ' * (n - i - 1) + '* ' * i)