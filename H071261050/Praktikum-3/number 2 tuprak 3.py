print("---Setup Denah Bioskop NontonYuk---")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris < 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except:
        print("Input harus berupa angka!")

while True:
    try:
        kursi = int(input("Masukkan jumlah kursi per baris: "))
        if kursi < 0:
            print("Jumlah kursi per baris harus lebih dari 0!")
            continue
        break
    except:
        print("Input harus berupa angka!")

print("---Daftar Kursi Tersedia---")

for x in range(1, baris + 1):
    for y in range(1, kursi + 1):
        if y == 13:
            continue
        if x == 1:
            if kursi % 2 != 0:
                print(f"Baris {x} - Kursi{y}")
        else:
            print(f"Baris {x} - Kursi {y}")
