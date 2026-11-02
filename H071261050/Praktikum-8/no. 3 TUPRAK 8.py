import re

def pembersihan_no_telpon(nomor_telepon):
    no_telp_bersih = re.sub(r"\D", "", nomor_telepon)

    print(f"Sebelum : {nomor_telepon}")
    print(f"Sesudah : {no_telp_bersih}")

    if re.fullmatch(r"\d{10,13}", no_telp_bersih):
        print("Status  : Valid")
        return True
    else:
        print("Status  : Tidak valid")
        return False

print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah_data = int(input("Masukkan jumlah data: "))

list_nomor_telp = []
for i in range(1, jumlah_data + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    list_nomor_telp.append(nomor)

print("\n--- Hasil Pembersihan ---")

jumlah_valid = 0
for x, nomor in enumerate(list_nomor_telp, start=1):
    print(f"\nData {x}:")
    if pembersihan_no_telpon(nomor):
        jumlah_valid += 1

print(f"\nJumlah nomor valid: {jumlah_valid}")