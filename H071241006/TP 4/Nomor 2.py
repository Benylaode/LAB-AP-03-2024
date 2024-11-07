def berburu_harta():
    total_jarak = 0
    ada_bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue

        if langkah == 0:
            break
        elif langkah < 0:
            print("Input tidak valid. Masukkan bilangan positif.")
            continue

        if langkah > 20:
            ada_bahaya = True

        total_jarak = total_jarak + langkah

    print(f"Total jarak: {total_jarak} meter")
    
    if ada_bahaya:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

berburu_harta()
