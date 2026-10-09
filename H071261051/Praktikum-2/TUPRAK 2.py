# NOMOR 2
jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").lower()


if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

biaya_express = 15000 if express == "ya" else (0 if express == "tidak" else "invalid")

if biaya_express == "invalid":
    print("Input layanan tidak valid! Harap masukkan 'ya' atau 'tidak'.")
else:
    total_tarif = tarif_dasar + biaya_express
    print(f"Total tarif pengiriman: Rp{total_tarif}")
