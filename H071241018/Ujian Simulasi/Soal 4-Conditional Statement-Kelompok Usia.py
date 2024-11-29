try:
    n = int(input('Masukkan Usia Anda: '))
    if n < 0:
        print('Usia tidak boleh negatif. Silakan masukkan usia yang valid.')
    elif n < 12:
        print('Anda termasuk dalam kelompok anak-anak') 
    elif 12 <= n <= 17:
        print('Anda termasuk dalam kelompok remaja')
    elif 18 <= n <= 64:
        print('Anda termasuk dalam kelompok dewasa')
    else:
        print('Anda termasuk dalam kelompok lansia')
except:
    print('Input tidak valid. Harap masukkan angka untuk usia.')

