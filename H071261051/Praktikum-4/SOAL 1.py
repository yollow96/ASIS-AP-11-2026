def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 90 // 100

    return subtotal


print("Selamat datang di Kasir Minimarket!")

status_member = input("Apakah Anda member? (y/n): ")
member = status_member == "y"

total = 0


while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member=member)

    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total += subtotal

print(f"Total belanja: Rp{total}")