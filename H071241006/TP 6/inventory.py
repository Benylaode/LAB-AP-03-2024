
inventory = []

def tampilkan_menu():
    print("\n=== Menu Inventory Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))

    for barang in inventory:
        if barang['nama'] == nama:
            print(f"Barang '{nama}' sudah ada")
            return
   
    barang = {
        'nama': nama,
        'jumlah': jumlah,
        'harga': harga
    }

    inventory.append (barang)
    print(f"Barang '{nama}' berhasil ditambahkan!")
 


def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    
    for barang in inventory:
        if barang['nama'] == nama:
            inventory.remove(barang)
            print(f"Barang '{nama}' berhasil dihapus!")
            return
    
    print(f"Barang '{nama}' tidak ditemukan!")

def tampilkan_daftar_barang():
    if len(inventory) == 0:
        print("Inventory kosong!")
    else:
        print("\n=== Daftar Barang di Gudang ===")
        for i, barang in enumerate(inventory):
            print(f"{i}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

def cari_barang():
    nama = input("Masukkan nama barang yang ingin dicari: ")
    
    for barang in inventory:
        if barang['nama'] == nama:
            print(f"Barang ditemukan: Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
            return
    
    print(f"Barang '{nama}' tidak ditemukan!")

def update_barang():
    nama = input("Masukkan nama barang yang ingin diupdate: ")
    
    for barang in inventory:
        if barang['nama'] == nama:
            print(f"Data barang '{nama}' ditemukan.")
            barang['jumlah'] = int(input("Masukkan jumlah barang yang baru: "))
            barang['harga'] = float(input("Masukkan harga barang yang baru: "))
            print(f"Barang '{nama}' berhasil diupdate!")
            return
    
    print(f"Barang '{nama}' tidak ditemukan!")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_daftar_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

main()