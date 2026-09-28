# while True :

#     try :
#         jumlah_kursi = int(input("Masukkan maksimal kursi: ")) 
#         break 
#     except :
#             print("Input jumlah kursi harus berupa angka!")
            
# print("---Sistem Reservasi PO BUS Dimulai---")
# sisa_kursi = jumlah_kursi - 1
# while sisa_kursi == 1 :
#     print("Sisa kursi: ",sisa_kursi)
#     umur = int(input("Masukkan umur penumpang: "))
#     if 5 <= umur >= 0 :
#         harga = 0
#         print("Kategori : Balita - Tiket gratis Rp", harga)
#     elif 6 <= umur >= 12 :
#         harga = 50000
#         print("Kategori: Anak - harga: Rp", harga)
#     elif umur > 12 :
#         harga = 100000
#         print("Kategori: Dewasa - harga: Rp", harga) 
#     else :
#         umur = "Tidak valid" 
#         print("---Semua Kursi Terisi---")
        
#         total_pendapatan = sum(harga)
#         print("Total pendapatan perjalanan PO BUS kali ini: ", total_pendapatan)

while True:
    try:
        jumlah_kursi = int(input("Masukkan maksimal kursi: "))
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

print("---Sistem Reservasi PO BUS Dimulai---")

sisa_kursi = jumlah_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print("Sisa kursi:", sisa_kursi)
    try :
        umur = int(input("Masukkan umur penumpang: "))
     
    except:
           print("Input umur harus berupa angka")
           continue
    if 0 > umur :
        print("Umur tidak valid")
        continue
    elif 0 <= umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket gratis Rp", harga)

    elif 6 <= umur <= 12:
        harga = 50000
        print("Kategori: Anak - harga: Rp", harga)

    elif umur > 12:
        harga = 100000
        print("Kategori: Dewasa - harga: Rp", harga)

    else:
        print("Umur tidak valid")
        continue
   

    total_pendapatan += harga
    sisa_kursi -= 1

print("---Semua Kursi Terisi---")
print("Total pendapatan perjalanan PO BUS kali ini:", total_pendapatan)
    