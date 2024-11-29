def palindrome(madam):   
    a = "".join(reversed(madam))

    if madam == a :
        print("Palindrome")
    else :
        print("Bukan Palindrome")

madam = input("Masukkan kata atau kalimat :")
palindrome(madam)

