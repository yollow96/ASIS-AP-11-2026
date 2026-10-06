print("Setup Denah Bioskop NontonYuk")

# Input validasi jumlah baris
while True:
    try:
        N = int(input("Masukkan jumlah baris: "))
        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

# Input validasi jumlah kursi
while True:
    try:
        M = int(input("Masukkan jumlah kursi per baris: "))
        if M <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("Daftar Kursi Tersedia")

# Nested loop untuk mencetak kursi
for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        # Aturan mitos: kursi 13 dilewati
        if kursi == 13:
            continue
            
        # Aturan Baris VVIP (Baris 1): hanya kursi ganjil
        if baris == 1:
            if kursi % 2 != 0:
                print(f"Baris 1 Kursi {kursi}")
        # Aturan Baris Reguler (Baris 2 dan seterusnya)
        else:
            print(f"Baris {baris} Kursi {kursi}")