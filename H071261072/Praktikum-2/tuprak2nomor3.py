nilai = float(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if 100>= nilai >= 80:
    print("Lolos ke Tahap Wawancara")

elif 80 > nilai >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")

else:
    print("Tidak Lolos")

#nilai tes "70"
#pengalaman kerja (tahun) "3"