def palindrome(kalimat):
    kalimat_bersih = kalimat.replace(" ", "")
    
    if kalimat_bersih == kalimat_bersih[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

kalimat_bersih = input("Masukkan kata: ")
palindrome(kalimat_bersih)