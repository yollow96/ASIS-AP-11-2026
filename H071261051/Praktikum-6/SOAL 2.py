#SISTEM PEMILIHAN KETUA KELAS "VOTECLASS"
def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih.strip()
    nama_kunci = nama_asli.lower() #nama kunci adalah nama yang sudah dirapikan untuk memudahkan program mencocokkan data
    pilihan = pilihan.strip().capitalize()

    if nama_kunci in rekap_suara:
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak terdaftar!")
    else:
        rekap_suara[nama_kunci] = pilihan
        print(
            f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!"
        )


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {} # Membuat dictionary untuk menyimpan jumlah suara

# Memberikan jumlah suara awal 0 kepada setiap kandidat yang terdaftar
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

# Mengambil setiap pilihan pemilih dan menambahkan jumlah suaranya
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("========================================")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    for kandidat in sorted(perolehan):
        print(f"  {kandidat}: {perolehan[kandidat]} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    if len(perolehan) == 0:
        print("Belum ada kandidat yang terdaftar!")
    elif total_suara == 0:
        print("Belum ada suara yang masuk!")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = []

# Mencari kandidat yang jumlah suaranya sama dengan suara tertinggi
        for kandidat in perolehan:
            if perolehan[kandidat] == suara_tertinggi:
                pemenang.append(kandidat)

# Memeriksa apakah ada lebih dari satu kandidat dengan suara tertinggi
        if len(pemenang) > 1:
            print("Hasil SERI antara: " + ", ".join(sorted(pemenang))) ## Mengurutkan nama pemenang sesuai abjaddan menggabungkannya dengan koma
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(
                f"PEMENANG: {pemenang[0]} "
                f"dengan {suara_tertinggi} suara!"
            )

    print("========================================")


kandidat_set = set() #agar kandidatnya tidak ada duplikat, maka digunakan set
rekap_suara = {}

print("========================================")
print("  SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    ).strip()

    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
            continue
        break

    daftar_kandidat(kandidat_set, nama)

print("\nKandidat terdaftar:", kandidat_set)

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input(
        "\nNama pemilih (kosongkan untuk selesai): "
    ).strip()

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara,
        kandidat_set,
        nama_pemilih,
        pilihan
    )

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
