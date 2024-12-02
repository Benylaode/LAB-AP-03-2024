import random

def tarik_kartu():
    return random.randint(1, 11)

def hitung_total(kartu):
    return sum(kartu)

def blackjack():
    print("Selamat datang di Blackjack!")

    kartu_pemain = [tarik_kartu()]
    kartu_dealer = [tarik_kartu()]

    while True:
        total_pemain = hitung_total(kartu_pemain)
        print(f"Kartu anda sekarang adalah: {total_pemain}")

        if total_pemain > 21:
            print("Anda kalah, kartu anda melebihi 21.")
            return
        
        aksi = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if aksi == 'y':
            kartu_pemain = kartu_pemain + [tarik_kartu()]
        else:
            break

    total_dealer = hitung_total(kartu_dealer)
    print(f"Kartu dealer adalah: {total_dealer}")

    while total_dealer < 17:
        kartu_dealer = kartu_dealer + [tarik_kartu()]
        total_dealer = hitung_total(kartu_dealer)
        print(f"Kartu dealer sekarang adalah: {total_dealer}")

    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_pemain > total_dealer:
        print("Anda menang!")
    elif total_pemain < total_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

blackjack()