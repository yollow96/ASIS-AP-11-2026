def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.90
    return subtotal

print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ").lower() == 'y'
total_belanja = 0

while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if not nama:
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    sub = hitung_subtotal(harga, jumlah, status)
    total_belanja += sub
    print(f"Subtotal {nama}: Rp{int(sub)}")

print(f"Total belanja: Rp{int(total_belanja)}")