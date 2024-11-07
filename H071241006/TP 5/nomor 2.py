def acronym(kalimat):
    kata_kata = kalimat.split()
    
    akronim = ''.join([kata[0].upper() for kata in kata_kata])
    
    print(akronim)

kata_kata = input("masukkan kalimat: ")
acronym(kata_kata)
