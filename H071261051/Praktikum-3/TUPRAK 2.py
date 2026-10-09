print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))

        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))

        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except:
        print("Input harus berupa angka!")


print()
print("--- Daftar Kursi Tersedia ---")

for baris in range(1, jumlah_baris + 1):

    for kursi in range(1, jumlah_kursi + 1):

        if kursi == 13:
            continue

        if baris == 1:

            if kursi % 2 == 1:
                print("Baris", baris, "- Kursi", kursi)

        else:
            print("Baris", baris, "- Kursi", kursi)