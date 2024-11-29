def proses_list_angka(angka_list):
    angka_genap = list(filter(lambda x: x % 2 == 0, angka_list))
    
    jumlah_genap = 0
    for angka in angka_genap:
        jumlah_genap += angka
    
    print(f"Jumlah angka genap: {jumlah_genap}")

input_data = [1, 2, 3, 4, 5, 6]
proses_list_angka(input_data)
