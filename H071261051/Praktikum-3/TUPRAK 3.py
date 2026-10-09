print("--- Sistem Reservasi PO BUS ---")

while True:
    try:
        jumlah_kursi = int(input("Masukkan maksimal kursi bus: "))

        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except:
        print("Input jumlah kursi harus berupa angka!")


print()
print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = jumlah_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print()
    print("Sisa kursi:", sisa_kursi)

    try:
        umur = int(input("Masukkan umur penumpang: "))

    except:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")

    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000")

    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000")

    sisa_kursi -= 1
    total_pendapatan += harga

print()
print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)

