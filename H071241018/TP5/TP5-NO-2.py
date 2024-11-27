def acronym (x) :
    
    akronim= ""
    for word in x.split():
        akronim += word[0].upper() 
    return akronim

a = input("Masukkan kata atau kalimat :")
print(acronym(a))