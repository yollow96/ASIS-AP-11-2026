# def countdown (detik):
#     if detik < 0 :
#         print("Input tidak valid, angka tidak boleh negatif.")
#         angka_baru = int(input("Masukkan angka awal hitung mundur :"))
#         countdown(angka_baru)

#     elif detik == 0:
#         print(0)
#         print("Luncurkan!")

#     else:
#         print(detik)
#         countdown(detik - 1)

# angka_awal = int(input("Masukkan angka awal hitung mundur :"))
# countdown(angka_awal)

def countdown (detik):
    if detik < 0:
        print("angka tidak boleh negatif")
        angka_baru = int(input("Masukkan angka awal :"))
        countdown(angka_baru)
    elif detik == 1:
        print(0)
        
        print("luncurkan!")
    else:
        print(detik)
        countdown(detik-1)

angka_awal= int(input("Masukkan angka awal :"))
countdown(angka_awal) 

# def countdown (detik):
#     if detik < 0:
#         print("angka tdk boleh negatif")
#         angka_awal = int(input("Masukkan angka awal hitung mundur :"))
#         countdown (angka_awal)
#     elif detik == 0:
#         print(0)
#         print("luncurkan!")
#     else:
#         print(detik)
#         countdown(detik - 1)

# angka_awal = int(input("Masukkan angka awal :"))
# countdown(angka_awal)