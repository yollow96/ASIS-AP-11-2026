# tarif pengiriman barang
jarak = float(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").strip().lower()

# Validasi input express
if express not in ["ya", "tidak"]:
    print("Error: Pilihan layanan express hanya boleh 'ya' atau 'tidak'!")
else:
    if jarak < 5:
        tarif_dasar = 10000
    elif jarak <= 20:
        tarif_dasar = 20000
    else:
        tarif_dasar = 35000

    biaya_tambahan = 15000 if express == "ya" else 0
    total_tarif = tarif_dasar + biaya_tambahan
    print(f"Total tarif pengiriman: Rp{total_tarif}")