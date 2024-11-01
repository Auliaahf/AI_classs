x = [1, 3, 2, 5, 2, 4, 8, 8, 6, 8, 9, 7, 5, 3, 2, 1, 5, 4, 6, 2]
input_angka = int(input("Masukkan angka: "))

# Cek apakah angka yang dimasukkan adalah genap atau ganjil
if input_angka % 2 == 0:
    panjang = x.count(input_angka)
    print("Jumlah data: ", panjang)

    # Menyimpan indeks dari angka yang sesuai
    hasil = [i for i in range(len(x)) if x[i] == input_angka]
    print("Berada di indeks: ", hasil)

else:
    print("Bukan genap")
