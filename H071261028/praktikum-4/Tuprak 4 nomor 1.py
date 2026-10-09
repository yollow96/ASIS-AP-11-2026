def hitung_subtotal (harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member :
        subtotal = subtotal -(subtotal * 10 / 100)
    return subtotal

print ("Selamat datang di Kasir Minimarket!")
total_belanja = 0
status_keanggotaan = input("Apakah Anda member? (y/n) :")
if status_keanggotaan == "y":
    adalah_member = True 
else:
    adalah_member = False

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai):")
    if nama_barang == "":
        break
    harga_barang = int(input("Harga barang:"))
    jumlah_barang = int(input("Jumlah_barang:"))

    subtotal = hitung_subtotal(harga_barang, jumlah_barang, adalah_member)
    print("subtotal", nama_barang +":", "Rp" + int(subtotal))
    total_belanja = total_belanja + subtotal
print("Total belanja : Rp" + str(int(total_belanja)))

# def hitung_total (harga, jumlah, adalah_member=False):
#     subtotal = harga * jumlah
#     if adalah_member :
#         subtotal = subtotal -(subtotal * 10 / 100)
#     return subtotal

# print("Selamat datang di Kasir Minimarket!")
# total_belanja = 0
# member = input("Apakah Anda member? (y/n):")
# if member == "y":
#     adalah_member = True
# else:
#     adalah_member = False

# while True:
#     nama_barang = input("Masukkan nama barang (kosongkan untuk selesai):")
#     if nama_barang == "":
#         break
#     harga_barang = int(input("Harga barang :"))
#     jumlah_barang = int(input("Jumlah barang :"))

#     subtotal = hitung_total(harga_barang, jumlah_barang, adalah_member)
#     print("Subtotal", nama_barang + ":", "Rp" + str(int(subtotal)))

#     total_belanja = total_belanja + subtotal
#     print("Total_belanja : Rp" + str(int(total_belanja)))


# def hitung_total(harga, jumlah, adalah_member=False):
#     subtotal = harga * jumlah
#     if adalah_member:
#         subtotal = subtotal - (subtotal * 10 / 100)
#     return subtotal

# print("Selamat datang di kasir!")
# total_belanja = 0
# member = input("Apakah anda member? (y/n):")
# if member == "y":
#     adalah_member = True
# else:
#     adalah_member = False

# while True:
     

    