def penerimaan_nilai (*nilai):
    rata = sum(nilai) / len(nilai)
    terendah = min(nilai)
    tertinggi = max(nilai)
    return rata, tertinggi, terendah

daftar_nilai = []

while True:
    nilai_ujian = input("Masukkan nilai ujian siswa (Kosongkan untuk selesai): ")
    if nilai_ujian == "":
        break
    try:
        nilai = int(nilai_ujian)
    except ValueError:
        nilai = float(nilai_ujian)
    daftar_nilai.append(nilai)


if len (daftar_nilai) == 0:
    print("Data tidak tersedia.")
else:
    rata, tertinggi, terendah = penerimaan_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
    print(daftar_nilai)
    print(len(daftar_nilai))
