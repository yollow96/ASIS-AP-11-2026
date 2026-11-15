import re

print("=== PROGRAM PEMBERSIHAN DATA NOMOR TELEPON ===")

data_sebelum = []
data_setelah = []
nomor_valid = []

def bersihkan_nomor(nomor):
    nomor_bersih = re.sub(r"[\s-]", "", nomor)
    return nomor_bersih


def validasi_nomor(nomor):
    pola_nomor = r"^[0-9]{10,13}$"

    if re.match(pola_nomor, nomor):
        return True
    else:
        return False


while True:
    try:
        jumlah_data = int(input("Masukkan jumlah data nomor telepon: "))

        if jumlah_data > 0:
            break
        else:
            print("Jumlah data harus lebih dari 0.")

    except ValueError:
        print("Input harus berupa angka!")


for i in range(jumlah_data):
    print(f"\nData nomor telepon ke-{i + 1}")

    nomor = input("Masukkan nomor telepon: ")

    data_sebelum.append(nomor)

    nomor_bersih = bersihkan_nomor(nomor)

    data_setelah.append(nomor_bersih)

    if validasi_nomor(nomor_bersih):
        nomor_valid.append(nomor_bersih)
        print("Nomor telepon valid.")
    else:
        print("Nomor telepon tidak valid!")


print("\n=== HASIL PEMBERSIHAN DATA ===")

print("\nData sebelum dibersihkan:")

for i, nomor in enumerate(data_sebelum, start=1):
    print(f"{i}. {nomor}")


print("\nData setelah dibersihkan:")

for i, nomor in enumerate(data_setelah, start=1):
    print(f"{i}. {nomor}")


print("\n=== DAFTAR NOMOR VALID ===")

if len(nomor_valid) > 0:
    for i, nomor in enumerate(nomor_valid, start=1):
        print(f"{i}. {nomor}")
else:
    print("Tidak ada nomor telepon yang valid.")

print("\nJumlah nomor valid:", len(nomor_valid))