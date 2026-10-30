def konversi_suhu(suhu, asal, tujuan):
    valid = ['C', 'F', 'K']
    if asal not in valid or tujuan not in valid:
        raise ValueError("Skala suhu tidak dikenali.")
    
    # Ke Celcius dulu
    if asal == 'F':
        c = (suhu - 32) * 5/9
    elif asal == 'K':
        c = suhu - 273.15
    else:
        c = suhu

    # Dari Celcius ke tujuan
    if tujuan == 'F':
        hasil = (c * 9/5) + 32
    elif tujuan == 'K':
        hasil = c + 273.15
    else:
        hasil = c
    return hasil

print("=== Konversi Suhu ===")
while True:
    inp = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if inp.lower() == 'selesai':
        break
    try:
        suhu = float(inp)
        asal = input("Skala asal (C/F/K): ").upper()
        tujuan = input("Skala tujuan (C/F/K): ").upper()
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil:.1f} {tujuan}")
    except ValueError as e:
        if str(e) == "could not convert string to float":
            print("Error: Input suhu harus berupa angka.")
        else:
            print(f"Error: {e}")