Jarak = int(input("Masukkan jarak pengiriman (km): "))
Pernyataan = input("Layanan express (ya/tidak): ").lower()

if Pernyataan not in ["ya", "tidak"]:
     print("Pernyataan hanya memuat pernyataan 'ya' atau 'tidak'!")
else: 
    if Jarak < 5:
        Jarak = 10000
    elif Jarak <= 20:
        Jarak = 20000
    else:
        Jarak = 35000

    layanan = 15000 if Pernyataan == "ya" else 0 
    Tarif = Jarak + layanan
    print("Total tarif pengiriman: Rp", Tarif)