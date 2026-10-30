while True:
    try:
        n = int(input("Masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print("Sistem Reservasi PO BUS Dimulai")
total_pendapatan = 0
sisa_kursi = n

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
        if umur < 0:
            print("Umur tidak valid!")
            continue
        
        if umur <= 5:
            print("Kategori: Balita \nTiket Gratis (Rp 0)")
            harga = 0
        elif 6 <= umur <= 12:
            print("Kategori: Anak | Harga: Rp 50.000")
            harga = 50000
        else:
            print("Kategori: Dewasa | Harga: Rp 100.000")
            harga = 100000
            
        total_pendapatan += harga
        sisa_kursi -= 1
    except ValueError:
        print("Input umur harus berupa angka!")

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")