nilai_tes = float(input("masukkan nilai tes: "))

if nilai_tes >= 80:
    print("langsung lolos ke tahap wawancara")
pengalaman_kerja = float(input("masukkan pengalaman kerja (tahun): "))
if nilai_tes >= 65 and nilai_tes <= 80 and pengalaman_kerja >= 2:
    print("lolos bersyarat")
else:
    print("tidak lolos")