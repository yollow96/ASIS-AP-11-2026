while True:
        try:
            kursi = int(input("Masukkan maksimal kursi bus: "))
            if kursi < 0:
                print("Input jumlah kursi harus berupa angka positif!!")
                continue
            break
        except:
             print("Input jumlah kursi harus berupa angka!!")

print ("---Sistem Reservasi PO BUS Dimulai---")

sisa = kursi
total_pendapatan = 0

while sisa > 0:
     print(f"Sisa kursi = {sisa}")
     umur_penumpang = input("Masukkan umur penumpang: ")
     try:
        umur = int(umur_penumpang)
     except:
            print("input umur harus berupa angka!!")
            continue
     if umur < 0:
            print("Umur tidak valid!!")
            continue
     
     if umur <= 5:
            kategori = "Balita"
            harga_tiket = 0
     elif umur <= 12:
            kategori = "Tiket Anak"
            harga_tiket = 50000
     else:
            kategori = "Tiket Dewasa"
            harga_tiket = 100000

     if harga_tiket == 0:
            print(f"Kategori: {kategori} - Tiket Gratis (Rp{harga_tiket})")
     else:
        harga_format = f"{harga_tiket}"
        print(f"Kategori: {kategori} - Harga Tiket: Rp{harga_format}")

     total_pendapatan += harga_tiket
     sisa -= 1

print("---Semua kursi telah terisi---")
print(f"Total pendapatan perjalanan PO BUS kali ini : Rp{total_pendapatan}")   