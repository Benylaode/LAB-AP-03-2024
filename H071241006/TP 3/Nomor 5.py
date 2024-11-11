try:
    A = int(input("Masukkan populasi awal Serangga A: "))
    B = int(input("Masukkan populasi awal Serangga B: "))
    H = int(input("Masukkan jumlah hari: "))
except:
    print("Data tidak valid")
for hari in range(1, H + 1):
    if hari % 5 == 0:
        print(f"Hari {hari}: Predator memakan 10% populasi.")
        A = int(A * 0.3)  
        B = int(B * 0.5)  
    elif hari % 2 == 1:  
        A = int(A * 0.2)  
        B = int(B * 0.4)  
    else: 
        A = int(A * 0.8)  
        B = int(B * 0.6)  

    print(f"Hari {hari}: Serangga A = {A}, Serangga B = {B}")