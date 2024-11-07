kata = input("masukkan string: ")

def palindrom(kata):
    print(kata[::-1])  
    if kata == kata[::-1]:
        print(f"{kata} adalah Palindrom")
    else:
        print(f"{kata} bukan Palindrom")

palindrom(kata)
