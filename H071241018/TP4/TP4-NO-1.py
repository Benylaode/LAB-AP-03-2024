import random

def draw_kartu():
    return random.randint(1, 11)

def hitung_total(kartu):
    return sum(kartu)
 
def giliran_player():
    kartu_player = [draw_kartu()]

    while True:
        print(f"Kartu anda sekarang adalah: {hitung_total(kartu_player)}")
        i = input("Apakah masih akan mengabil kartu? (y/n):")
        if i == "y":
            kartu_player.append(draw_kartu())
            if hitung_total(kartu_player) > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return None 
        elif i == "n":
            break
        else:
            print("Input tidak valid, silahkan masukkan 'y' atau 'n'.")
        
    return kartu_player
    
def giliran_dealer():
    kartu_dealer= [draw_kartu()]

    while hitung_total(kartu_dealer) < 17:
        kartu_dealer.append(draw_kartu()) # type: ignore
        
    return kartu_dealer
    

def pilih_pemenang(total_player, total_dealer):
    if total_player > 21:
        return "Anda kalah!"
    elif total_dealer > 21:
        return "Anda menang, dealer melebihi 21"
    elif total_player > total_dealer:
        return "Anda menang!"
    elif total_dealer > total_player:
        return "Dealer menang"
    else:
        return "Seri!"
    
def player_blackjack():
    print("Welcome to Blackjack!")

    kartu_player = giliran_player()
    if kartu_player is None:
        return
    
    kartu_dealer = giliran_dealer()
    total_player = hitung_total(kartu_player)
    total_dealer = hitung_total(kartu_dealer)

    print(f"Kartu dealer adalah: {total_dealer}")
    print(pilih_pemenang(total_player, total_dealer))

player_blackjack()


# # Membuat daftar kosong
# daftar_kartu = []

# # Menambahkan elemen ke dalam daftar
# daftar_kartu.append(5)
# daftar_kartu.append(10)

# print(daftar_kartu)  # Output: [5, 10]