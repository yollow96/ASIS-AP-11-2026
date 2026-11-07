import re

def validasi_telepon(nomor):
    if re.match(r"^[0-9]{10,13}$", nomor):
        print("Nomor valid.")
        return True
    else:
        print("Nomor tidak valid!")
        return False


data_sebelum = []
data_sesudah = []
nomor_valid = []

print("=== Pembersihan Data Nomor Telepon ===")

jumlah_data = int(input("Masukkan jumlah data: "))

for i in range(jumlah_data):
    nomor = input(f"\nNomor ke-{i + 1}: ")

    nomor_bersih = re.sub(r"[ -]", "", nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(nomor_bersih)

    if validasi_telepon(nomor_bersih):
        nomor_valid.append(nomor_bersih)

print("\n=== Hasil Pembersihan ===")

for i in range(jumlah_data):
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")

    if re.match(r"^[0-9]{10,13}$", data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")
