print("Setup Denah Bioskop NontonYuk")
while True:
    try:
        n = int(input("Masukkan jumlah baris: "))
        if n <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

m = int(input("Masukkan jumlah kursi per baris: "))
print("Daftar Kursi Tersedia")
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j == 13:
            continue
        if i == 1 and j % 2 == 0:
            continue
        print(f"Baris {i} - Kursi {j}")