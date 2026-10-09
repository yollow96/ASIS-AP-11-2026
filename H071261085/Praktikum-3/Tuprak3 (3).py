# Input validasi kuota kursi bus
while True:
    try:
        sisa_kursi = int(input("Masukkan maksimal kursi bus: "))
        if sisa_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print("Sistem Reservasi PO BUS Dimulai")

total_pendapatan = 0

# Perulangan selama kursi masih tersedia
while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    input_umur = input("Masukkan umur penumpang: ")
    
    try:
        umur = int(input_umur)
    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    # Penentuan kategori dan harga tiket
    if umur <= 5:
        harga = 0
        print("Kategori: Balita Tiket Gratis (Rp 0)")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak Harga: Rp 50.000")
    else:
        harga = 100000
        print("Kategori: Dewasa Harga: Rp 100.000")

    total_pendapatan += harga
    sisa_kursi -= 1

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")