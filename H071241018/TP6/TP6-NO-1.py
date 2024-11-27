Gudang_Garam = {}

def Tampilan_Menu():
    print("\nBarang yang tersedia")
    print("1.Tambahkan Barang")
    print("2.Hapus Barang")
    print("3.Tampilkan Barang")
    print("4.Cari Barang")
    print("5.Update Data Barang")
    print("6.Keluar")
    
def Tambahkan_Barang():
    Kode_Barang = int(input("Masukkan Kode Barang Baru: "))
    Nama_Barang = str(input("Masukkan Nama Barang Baru: "))
    Masukkan_Jumlah = int(input("Masukkan Jumlah Barang Baru: "))
    if Kode_Barang in Gudang_Garam:
        print("Barang sudah ada di gudang")
    else:
        Gudang_Garam[Kode_Barang] = {'nama': Nama_Barang}
        print(f"Jumlah '{Nama_Barang}' berhasil ditambahkan.")

def Hapus_Barang():
    Kode_Barang = int(input("Masukkan Kode Barang yang ingin dihapus: "))
    if Kode_Barang in Gudang_Garam:
        del Gudang_Garam[Kode_Barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def Tampilakn_Barang():
    if not Gudang_Garam:
        print("Tidak ada barang dalam Gudang_Garam.")
    else:
        print("\nDaftar Barang:")
        for kode, info in Gudang_Garam.items():
            print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['Jumlah']}, Harga: {info['Harga']}")

def Cari_Barang():
    Kode_Barang = int(input("Masukkan Kode Barang yang ingin dicari: "))
    if Kode_Barang in Gudang_Garam:
        info = Gudang_Garam[Kode_Barang]
        print(f"Barang Ditemukan - Kode: {Kode_Barang}, Nama: {info['nama']}, Jumlah: {info['Jumlah']}, Harga: {info['Harga']}")
    else:
        print("Kode barang tidak ditemukan.")

def Update_Barang():
    Kode_Barang = int(input("Masukkan Kode Barang yang ingin diperbarui: "))
    if Kode_Barang in Gudang_Garam:
        Nama_Barang = input("Masukkan Nama Baru: ")
        Jumlah = int(input("Masukkan Jumlah Baru: "))
        Harga = float(input("Masukkan Harga Baru: "))
        Gudang_Garam[Kode_Barang] = {'nama': Nama_Barang, 'Jumlah': Jumlah, 'Harga': Harga}
        print("Data barang berhasil diperbarui.")
    else:
        print("Kode barang tidak ditemukan.")

def main():
    while True:
        Tampilan_Menu()
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            Tambahkan_Barang()
        elif pilihan == '2':
            Hapus_Barang()
        elif pilihan == '3':
            Tampilakn_Barang()
        elif pilihan == '4':
            Cari_Barang()
        elif pilihan == '5':
            Update_Barang()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()


# def a(a, b):
#     return a + b

# # Memanggil fungsi dan menyimpan hasil
# a = a(3, -5)
# print(a)  # Output: 8