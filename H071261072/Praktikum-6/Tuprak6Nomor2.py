
print("Khaerul")

daftar_list_kandidat = set()
daftar_suara_kandidat = {}
daftar_suara_pemilihan = {}
rekapan_suara_yang_memilih = set()


def daftar_kandidat(nama):
    nama = nama.strip().title()

    if not nama:
        print("Nama kandidat tidak boleh kosong!")
        return False

    if nama in daftar_list_kandidat:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False

    daftar_list_kandidat.add(nama)
    daftar_suara_kandidat[nama] = 0

    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def hitung_suara(kandidat):
    if kandidat not in daftar_suara_kandidat:
        return False

    daftar_suara_kandidat[kandidat] += 1
    return True


def berikan_suara(nama_pemilih, kandidat):
    nama_pemilih = nama_pemilih.strip().title()
    kandidat = kandidat.strip().title()

    if not nama_pemilih:
        print("Nama pemilih tidak boleh kosong!")
        return False

    if nama_pemilih in rekapan_suara_yang_memilih:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    if kandidat not in daftar_list_kandidat:
        print("Nama kandidat yang Anda pilih tidak terdaftar!")
        return False

    if hitung_suara(kandidat):
        rekapan_suara_yang_memilih.add(nama_pemilih)
        daftar_suara_pemilihan[nama_pemilih] = kandidat

        print(
            f"Suara '{nama_pemilih}' untuk "
            f"'{kandidat}' berhasil dicatat!"
        )
        return True

    return False


def tampilkan_hasil():
    if not daftar_suara_kandidat:
        print("Belum ada kandidat yang terdaftar.")
        return

    print("\nDaftar Perolehan Suara:")

    for kandidat in sorted(daftar_suara_kandidat):
        print(
            f"   {kandidat}: "
            f"{daftar_suara_kandidat[kandidat]} suara"
        )

    total_suara = len(daftar_suara_pemilihan)

    print()
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
        return

    suara_tertinggi = max(daftar_suara_kandidat.values())

    kandidat_tertinggi = [
        kandidat
        for kandidat, suara in daftar_suara_kandidat.items()
        if suara == suara_tertinggi
    ]

    if len(kandidat_tertinggi) > 1:
        print("Hasil seri dan perlu pemilihan ulang!")

        print("Kandidat dengan suara tertinggi:")
        for kandidat in sorted(kandidat_tertinggi):
            print(f"- {kandidat}: {suara_tertinggi} suara")

    else:
        pemenang = kandidat_tertinggi[0]

        print(
            f"PEMENANG: {pemenang} "
            f"dengan {suara_tertinggi} suara!"
        )


print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")


print("\n--- PENDAFTARAN KANDIDAT ---")

while True:
    nama_kandidat = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    ).strip()

    if nama_kandidat == "":
        break

    daftar_kandidat(nama_kandidat)


print("\nKandidat terdaftar:")

if daftar_list_kandidat:
    for kandidat in sorted(daftar_list_kandidat):
        print(f"- {kandidat}")
else:
    print("Belum ada kandidat.")


print("\n--- FASE PEMUNGUTAN SUARA ---")

if not daftar_list_kandidat:
    print("Pemungutan suara tidak dapat dilakukan karena belum ada kandidat.")

else:
    while True:
        print()

        nama_pemilih = input(
            "Nama pemilih (kosongkan untuk selesai): "
        ).strip()

        if nama_pemilih == "":
            break

        if nama_pemilih.title() in rekapan_suara_yang_memilih:
            print(
                f"'{nama_pemilih.title()}' "
                "sudah memberikan suara sebelumnya!"
            )
            continue

        print(
            f"Kandidat yang tersedia: "
            f"{sorted(daftar_list_kandidat)}"
        )

        pilih_kandidat = input(
            "Pilih kandidat: "
        ).strip()

        if pilih_kandidat == "":
            print("Nama kandidat tidak boleh kosong!")
            continue

        berikan_suara(nama_pemilih, pilih_kandidat)


print("\n=================================")
print("   HASIL PEMILIHAN KETUA KELAS")
print("=================================")

tampilkan_hasil()

print("\nTerima kasih telah menggunakan sistem pemilihan!")
