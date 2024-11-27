def enkripsi(text, shift):
    kapital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    nomor = "0123456789"
    
    output = ""

    for huruf in text:

        if huruf in huruf_kecil:
            index = huruf_kecil.index(huruf)
            akhir = (index + shift) % 26
            output += huruf_kecil[akhir]
        
        elif huruf in kapital:
            index = kapital.index(huruf)
            new_index = (index + shift) % 26
            output += kapital[new_index]

        elif huruf in nomor:
            index = nomor.index(huruf)
            if shift % 10 == 0:
                new = shift + 1
                new_index =  (index + new) % 10
            else :
                new_index =  (index + shift) % 10
            output += nomor[new_index]

        else:
            output += huruf

    return output


input_string = input("Masukkan string untuk dienkripsi: ")
while True:
    try:
        shift_value = int(input("Masukkan nilai pergeseran (shift): "))
        break
    except ValueError :
        print ('Input tidak valid masukkan bilangan bulat.')

encrypted_string = enkripsi(input_string, shift_value)

print("Hasil enkripsi:", encrypted_string)
