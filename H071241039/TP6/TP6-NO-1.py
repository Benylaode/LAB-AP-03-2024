inventory = {}

def display_menu():
    print("\n=== menu inventory ===")
    print("1. menambah barang")
    print("2. menghapus barang")
    print("3. menampilkan daftar barang")
    print("4. mencari barang")
    print("5. mengupdate data barang")
    print("6. keluar")

def tambah_barang():
    kode = input("masukkan kode barang: ").upper()
    if kode in inventory:
        print("kode barang tersebut sudah ada boskuu")
    else:
        nama = input("masukkan nama barang: ")
        jumlah = int(input("masukkan jumlah barang: "))
        harga = float(input("masukan harga barang: "))
        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print(f"barang {nama} berhasil ditambahkan kyaakkk><")

def hapus_barang():
    kode = input("masukkan kode barang yang mau dihapus: ").upper()
    if kode in inventory:
        del inventory[kode]
        print(f"barang dengan kode {kode} tersebut berhasil dihapus yagesya")
    else:
        print("barang tidak ditemukan abangku")


def tampilkan_barang():
    if not inventory:
        print("Inventory kosong kaks")
    else:
        print("\n=== daftar barang ===")
        print(inventory)
        for kode, data in inventory.items():
            print(f"kode: {kode}, nama: {data['nama']}, jumlah: {data['jumlah']}, harga: {data['harga']}")

def cari_barang():
    kode = input("masukan kode barang yang mau dicari: ").upper()
    if kode in inventory:
        data = inventory[kode]
        print(f"kode: {kode}, nama: {data['nama']}, jumlah: {data['jumlah']}, harga: {data['harga']}")
    else:
        print("barang tidak ditemukan bosq")

def update_barang():
    kode = input ("masukkan kode barang yang ingin di-update: ").upper()
    if kode in inventory:
        print(f"barang ditemukan: {inventory[kode]}")
        nama_baru = input("masukkan nama barang baru: ")
        jumlah_baru = input("masukkan jumlah barang baru: ")
        harga_baru = input("masukkan harga barang baru: ")

        if nama_baru:
            inventory[kode]['nama'] = nama_baru
        elif jumlah_baru:
            inventory[kode]['jumlah'] = int(jumlah_baru)
        elif harga_baru:
            inventory[kode]['harga'] = float(harga_baru)
        print("data barang berhasil diperbaharui")
    else:
        print("barang tidak ditemukan")

def main():
    while True:
        display_menu()
        pilihan = input("silahkan pilih menu (1-6): ")
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("terima kasih telah menggunakan program ini")
            break
        else:
            print("pilihan tidak valid, coba lagi")

main()
        