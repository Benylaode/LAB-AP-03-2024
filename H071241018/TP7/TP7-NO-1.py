import os.path
from datetime import datetime

daftar =os.listdir("film")
daftar_film = [file for file in daftar if os.path.isfile(os.path.join("film", file))]
daftar_tiket = {}

def generate_ticket_id():
    return "TICK" + datetime.now().strftime("tanggal:%d bulan:%m tahun:%Y pukul:%H menit:%M detik:%S")


def detail_tiket(film, id_tiket):
    tanggal_beli = datetime.now().strftime(" tanggal:%d - bulan:%m - tahun:%Y pukul:%H : menit:%M : detik:%S")
    film_diproses = (film[:27] + '..') if len(film) > 27 else film.ljust(27)  # Memotong jika lebih dari 27 karakter
    detail = f"""
    +---------------------------------------------+
    |               TIKET BIOSKOP                 |
    | ID TICKET: {id_tiket.ljust(27)}             |
    | Film: {film_diproses}                       |
    | tanggal_beli: {tanggal_beli.ljust(27)}      |
    +---------------------------------------------+
    |         Terimakasih telah membeli           |
    |                tiket anda                   |
    +---------------------------------------------+
    """
    return detail
    
def tambah_film():
    while True:
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if nama_film == "":
            break
        nama_film_txt = f"{nama_film}.txt"
        
        if nama_film_txt in daftar_film:
            print(f"Film '{nama_film}' sudah ada dalam daftar.\n")
            continue
        
        print(f"Film '{nama_film}' berhasil ditambahkan.\n")

        if not os.path.exists("film"):
            os.makedirs("film")
        with open(f"film/{nama_film}.txt", "w") as file:
            file.write(f"Film: {nama_film}\n")
            file.write("Informasi tentang film ini akan ditambahkan kemudian.\n")
        print(f"File untuk film '{nama_film}' telah dibuat: film/{nama_film}.txt\n")

def hapus_film():
    while True:
        if len(daftar_film) == 0:
            print("Tidak ada film yang tersedia.")
            break
        print("--- Daftar Film ---")
        for idx, film in enumerate(daftar_film, 1):
            print(f"{idx}. {film}")
        print("0. Kembali")
        
        pilihan = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(daftar_film):
            film_dihapus = daftar_film.pop(pilihan - 1)
            print(f"Film '{film_dihapus}' berhasil dihapus.\n")

def daftar_tiket_admin():
    print("--- Daftar Tiket ---")
    if len(daftar_tiket) == 0:
        print("Belum ada tiket yang dibeli.\n")
    else:
        for idx, (id_tiket, tiket_info) in enumerate(daftar_tiket.items(), 1):
            print(f"{idx}. ID Tiket: {id_tiket} | Film: {tiket_info['film']} | tanggal_beli: {tiket_info['tanggal_beli']}")

def hapus_tiket_admin():
    while True:
        if len(daftar_tiket) == 0:
            print("Belum ada tiket yang tersedia.")
            break
        print("--- Daftar Tiket ---")
        for idx, (id_tiket, tiket_info) in enumerate(daftar_tiket.items(), 1):
            print(f"{idx}. ID Tiket: {id_tiket} | Film: {tiket_info['film']} | tanggal_beli: {tiket_info['tanggal_beli']}")
        print("0. Kembali")

        pilihan = int(input("Masukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(daftar_tiket):
            tiket_dihapus = list(daftar_tiket.keys())[pilihan - 1]
            del daftar_tiket[tiket_dihapus]
            os.remove(f"tickets/{tiket_dihapus}.txt")  
            print(f"Tiket dengan ID '{tiket_dihapus}' berhasil dihapus.\n")

def beli_tiket():
    if len(daftar_film) == 0:
        print("Belum ada film yang tersedia.\n")
        return
    print("--- Daftar Film ---")
    
    for idx, film in enumerate(daftar_film, 1):
        print(f"{idx}. {film}")
    print("0. Kembali")
    
    pilihan = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
    if pilihan == 0:
        return
    if 1 <= pilihan <= len(daftar_film):
        film_dipilih = daftar_film[pilihan - 1]
        id_tiket = generate_ticket_id()
        tanggal_beli_beli = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        daftar_tiket[id_tiket] = {'film': film_dipilih, 'tanggal_beli': tanggal_beli_beli}
        
        print(f"Tiket berhasil dibeli. ID tiket Anda: {id_tiket}")
        
        if not os.path.exists("tickets"):
            os.makedirs("tickets")
        with open(f"tickets/{id_tiket}.txt", "w") as file:
            file.write(f"TIKET BIOSKOP\n")
            file.write(f"ID Tiket  : {id_tiket}\n")
            file.write(f"Film      : {film_dipilih}\n")
            file.write(f"tanggal_beli   : {tanggal_beli_beli}\n")
            file.write("Terima kasih telah membeli tiket Anda!\n")
        
        print(f"File tiket telah dibuat: tickets/{id_tiket}.txt\n")
        detail_tiket(film, id_tiket)

def sistem_pemesanan_tiket():
    while True:
        print("--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = int(input("Pilih peran (1/2/3): "))
        
        if peran == 1:
            while True:
                print("--- Menu Admin ---")
                print("1. Tambah film")
                print("2. Hapus film")
                print("3. Daftar Tiket")
                print("4. Hapus Tiket")  
                print("5. Kembali")
                opsi_admin = int(input("Pilih opsi (1/2/3/4/5): "))
                
                if opsi_admin == 1:
                    tambah_film()  
                elif opsi_admin == 2:
                    hapus_film()
                elif opsi_admin == 3:
                    daftar_tiket_admin()
                elif opsi_admin == 4:
                    hapus_tiket_admin() 
                elif opsi_admin == 5:
                    break
        
        elif peran == 2:
            while True:
                print("--- Menu Pengunjung ---")
                print("1. Lihat daftar film")
                print("2. Beli tiket")
                print("3. Kembali")
                opsi_pengunjung = int(input("Pilih opsi (1/2/3): "))
                
                if opsi_pengunjung == 1:
                    if len(daftar_film) == 0:
                        print("Belum ada film yang tersedia.\n")
                    else:
                        print("--- Daftar Film ---")
                        for idx, film in enumerate(daftar_film, 1):
                            nama_film_tanpa_txt = film[:-4]  
                            print(f"{idx}. {nama_film_tanpa_txt}")
                    print()
                elif opsi_pengunjung == 2:
                    beli_tiket() 
                elif opsi_pengunjung == 3:
                    break
        
        elif peran == 3:
            print("Terima kasih telah menggunakan sistem ini.")
            break

sistem_pemesanan_tiket()
