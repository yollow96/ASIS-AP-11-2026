def rekap_nilai(*args):
    return sum(args) / len(args), max(args), min(args)

nilai_list = []
while True:
    inp = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if not inp:
        break
    # Mengubah ke int jika bilangan bulat, atau float jika ada desimal
    val = float(inp)
    nilai_list.append(int(val) if val.is_integer() else val)

if nilai_list:
    rata, max_val, min_val = rekap_nilai(*nilai_list)
    print(f"Rata-rata kelas: {rata}\nNilai tertinggi: {max_val}\nNilai terendah: {min_val}")
    print(nilai_list)
else:
    print("Data nilai tidak tersedia.")