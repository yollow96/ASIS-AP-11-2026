def rekap_nilai(*args):
    return sum(args)/len(args), max(args), min(args)

nilai_siswa = []
while True:
    inp = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if not inp:
        break
    nilai_siswa.append(float(inp))

if nilai_siswa:
    rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {int(tertinggi) if tertinggi.is_integer() else tertinggi}")
    print(f"Nilai terendah: {int(terendah) if terendah.is_integer() else terendah}")
else:
    print("Data nilai tidak tersedia.")