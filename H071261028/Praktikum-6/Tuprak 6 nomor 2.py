def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    kandidat_set.add(nama)

    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_lower = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print("Kandidat tidak valid! Suara tidak dicatat.")
    else:
        rekap_suara[nama_pemilih_lower] = pilihan #memasukkan data ke dictionary
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set: #mengambil nama kandidat yg ada dalam set
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1#menambahkan satu suara kepada kandidat yg sdng diperiksa

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n=======================================")
    print("       HASIL PEMILIHAN KETUA KELAS")
    print("=======================================")

    for kandidat in sorted(perolehan):
        print(f"{kandidat}: {perolehan[kandidat]} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
    else:
        suara_tertinggi = max(perolehan.values())

        pemenang = [
            kandidat for kandidat, suara in perolehan.items()#untuk mengambil key and value sekaligus dari dictionary
            if suara == suara_tertinggi
        ]

        if len(pemenang) > 1:
            print("HASIL SERI! Perlu dilakukan pemilihan ulang.")
        else:
            print(
                f"PEMENANG: {pemenang[0]} "
                f"dengan {suara_tertinggi} suara!"
            )

    print("=======================================")


# PROGRAM UTAMA

print("=======================================")
print("       SISTEM PEMILIHAN KETUA KELAS")
print("=======================================")

kandidat_set = set()
rekap_suara = {}

# FASE PENDAFTARAN KANDIDAT

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        if len(kandidat_set) >= 2:
            break
        else:
            print("Minimal harus ada 2 kandidat! Silakan daftar lagi.")
            continue

    daftar_kandidat(kandidat_set, nama)

print("\nKandidat terdaftar:", 
      "{" + ", ".join(repr(n) for n in sorted(kandidat_set)) + "}")

# FASE PEMUNGUTAN SUARA

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ")

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", 
          "{" + ", ".join(repr(n) for n in sorted(kandidat_set)) + "}")

    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara,
        kandidat_set,
        nama_pemilih,
        pilihan
    )

# MENAMPILKAN HASIL

perolehan = hitung_suara(rekap_suara, kandidat_set)

tampilkan_hasil(perolehan)
