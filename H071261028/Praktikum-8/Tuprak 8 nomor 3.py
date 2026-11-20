import re

print("=== Pembersihan Data Nomor Telepon ===")

jumlah_data = int(input("Masukkan jumlah data: "))

data_telepon = []
nomor_valid = []

for i in range(jumlah_data):
    nomor = input(f"\nNomor ke-{i+1}: ")
    data_telepon.append(nomor)

print("\n--- Hasil Pembersihan ---")

for i, nomor in enumerate(data_telepon, start=1):

    hasil = re.sub(r"[\s-]", "", nomor)

    if re.match(r"^[0-9]{10,13}$", hasil):
        status = "Valid"
        nomor_valid.append(hasil)
    else:
        status = "Tidak valid"

    print(f"\nData {i}:")
    print(f"Sebelum : {nomor}")
    print(f"Sesudah : {hasil}")
    print(f"Status  : {status}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")
