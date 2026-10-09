def hitung_subtotal (harga_barang, jumlah_barang, adalah_member=False):
    subtotal = harga_barang*jumlah_barang
    if adalah_member:
        subtotal = subtotal - (subtotal * 10/100)
    return int(subtotal)


print("Selamat Datang di Kasir Minimarket")

status = str(input("Apakah Anda Member? (y/n): " ))
if status == "y":
    adalah_member = True
else : 
    adalah_member = False

total = 0

while True :
        nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai): "))
        if nama_barang == "":
            break
        harga_barang = int(input("Masukkan harga barang: "))
        jumlah_barang = int(input("Masukkan Jumlah Barang: "))

        subtotal = hitung_subtotal(harga_barang, jumlah_barang, adalah_member)
        print(f"Subtotal {nama_barang}: Rp{subtotal}")
        total = total + subtotal
print(f"Total belanja : {total}")
