def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = ("C", "F", "K")
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali")

    if skala_asal == "C":
        celcius = suhu 
    elif skala_asal == "F":
        celcius = (suhu - 32) * 5/9
    else:
        celcius = suhu - 273.15

    if skala_tujuan == "C":
            return celcius
    elif skala_tujuan == "F":
            return celcius * 9/5 + 32
    else:
        return celcius + 273.15

print("=== Konversi Suhu ===")

while True:
    masukkan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if masukkan.lower() == "selesai":
        break

    try:
        suhu = float(masukkan)
    except ValueError:
        continue

    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")

    try: 
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError:
        print("Error: Skala atau suhu tidak diketahui")

    





    