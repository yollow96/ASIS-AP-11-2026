def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    diskon = subtotal * 10 // 100
    return subtotal - diskon if adalah_member else subtotal

print("Selamat datang di Kasir Minimarket!")
is_member = input("Apakah Anda member? (y/n): ").strip().lower() == 'y'
total = 0

while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if not nama:
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    subtotal = hitung_subtotal(harga, jumlah, is_member)
    total += subtotal
    print(f"Subtotal {nama}: Rp{subtotal}")

print(f"Total belanja: Rp{total}")