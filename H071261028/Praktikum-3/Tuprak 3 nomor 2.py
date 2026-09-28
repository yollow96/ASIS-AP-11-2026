
# while True :
#     if jumlah_baris : int(input("Masukkan jumlah baris: "))
#     elif jumlah_baris <= 0 :
#         print("Jumlah baris harus lebih dari 0!")
#     elif jumlah_baris < 0 :
#         print("Jumlah baris harus lebih dari 0!")
#     elif jumlah_baris <0 :
#         break
#     else :
#         print("Input harus berupa angka!")

# while True :
#     try :
#         jumlah_kursi = int(input("Masukkan jumlah kursi: "))
#         if jumlah_kursi == 13 :
#             continue
#         else :
#             break
#     except :
#         print("Input harus berupa angka!")


# while True :
#     try :
#         jumlah_baris = int(input("Masukkan jumlah baris: "))
#         if jumlah_baris == 13 :
#             continue
#         elif jumlah_baris < 0 :
#             print("Jumlah baris harus lebih dari 0!")
#         else :
#             jumlah_kursi =int(input("Masukkan jumlah kursi per baris: "))
#     except :
#             print("Input harus berupa angka!")
#     if jumlah_baris == 1 :
#         for jumlah_baris in range(1, jumlah_baris + 1, 2) :
#           print("Baris", jumlah_baris, "- Kursi", jumlah_kursi)
        
# while True:
#     try:
#         jumlah_baris = int(input("Masukkan jumlah baris: "))

#         if jumlah_baris == 0:
#             break

#         elif jumlah_baris == 13:
#             continue

#         elif jumlah_baris < 0:
#             print("Jumlah baris harus lebih dari 0!")

#         else:
#             jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))

#             for jumlah_baris in range(1, jumlah_baris + 1, 2):
#                 print("Baris", jumlah_baris, "- Kursi", jumlah_kursi)

#     except:
#         print("Input harus berupa angka!")
    
print("---Setup Denah Bioskop NontonYuk---")
while True:
    
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
        break
    except:
        print("Input baris harus berupa angka!")

print("--- Daftar Kursi Tersedia ---")
for baris in range(1, jumlah_baris + 1):
    if baris == 1:
        for kursi in range(1, jumlah_kursi + 1, 2):
            if kursi == 13:
                continue
            print("Baris", baris, "- Kursi", kursi)

    else:
        for kursi in range(1, jumlah_kursi):
            if kursi == 13:
                continue

            print("Baris", baris, "- Kursi", kursi)
        
        
    
            
        
            
