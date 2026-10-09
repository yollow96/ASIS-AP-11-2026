jarak = int(input("Masukkan jarak pengiriman (km):"))
express = input("Layanan express (ya/tidak):").strip().lower()

if express not in ["ya", "tidak"] :
    print("Error : pilihan hanya ya dan tidak")
else :
    if jarak < 5 :
        tarif = 10000
    elif jarak <=20 :
        tarif = 20000
    else :
        tarif = 35000

    layanan = 15000 if express == "ya" else 0
    total_tarif = tarif + layanan
    print("Rp",total_tarif)