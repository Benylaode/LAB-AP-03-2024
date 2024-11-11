n = int(input("Masukkan jumlah baris : "))

for i in range(1,n+1) :
        print((n-i) * " " + (2*i-1) * "*")

if n %2 == 0 :
        print((2*n-1) * "*")
else :
        pass
for i in range(n-1,0,-1) :
    print((n-i) * " " + (2*i-1) * "*")