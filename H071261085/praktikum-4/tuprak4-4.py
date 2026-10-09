def konversi_suhu(val, asal, tujuan):
    asal, tujuan = asal.upper(), tujuan.upper()
    skala_valid = {'C', 'F', 'K'}
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")
    
    # Konversi dari skala asal ke Celsius
    if asal == 'C': c = val
    elif asal == 'F': c = (val - 32) * 5/9
    elif asal == 'K': c = val - 273.15
    
    # Konversi dari Celsius ke skala tujuan
    if tujuan == 'C': return c
    elif tujuan == 'F': return c * 9/5 + 32
    elif tujuan == 'K': return c + 273.15

print("=== Konversi Suhu ===")
while True:
    inp = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if inp.lower() == 'selesai':
        break
    asal = input("Skala asal (C/F/K): ")
    tujuan = input("Skala tujuan (C/F/K): ")
    
    try:
        hasil = konversi_suhu(float(inp), asal, tujuan)
        print(f"Hasil: {float(inp)} {asal.upper()} = {hasil} {tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")