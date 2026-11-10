daftar_buku = {}
daftar_penulis = {}
daftar_harga = {}
daftar_stok = {}

total_buku = 0
total_seluruh_stok = 0
total_nilai_aset = 0

def tambah_buku(judul, penulis, harga, stok):
    if judul in daftar_buku:
        print("Buku sudah terdaftar!")
        return

    daftar_buku[judul] = judul
    daftar_penulis[judul] = penulis
    daftar_harga[judul] = harga
    daftar_stok[judul] = stok

def total_ditemukan_buku(cari):
    total = 0

    for i in daftar_buku.keys():
        if cari.lower() in i.lower():
            total += 1

    return total

def mencari_buku(cari):
    total = total_ditemukan_buku(cari)

    if total == 0:
        print("Tidak ada buku yang ditemukan")
        return

    urutan = 0

    print(f"Ditemukan {total} buku:")

    for i in daftar_buku.keys():
        if cari.lower() in i.lower():
            urutan += 1

            dapat = i
            penulis = daftar_penulis[i]
            harga = daftar_harga[i]
            stok = daftar_stok[i]

            print(
                f"  {urutan}. {dapat} - {penulis} | "
                f"Rp{harga} | Stok: {stok}"
            )

def update_stok(buku, simbol, angka):
    if buku not in daftar_stok:
        print("Buku tidak ditemukan")
        return

    angka = int(angka)

    if simbol == "-":
        if daftar_stok[buku] < angka:
            print("Gagal membuat perubahan: stok tidak mencukupi")
            return

        daftar_stok[buku] -= angka

        print(
            f"Stok '{buku}' berkurang {angka}. "
            f"Stok sekarang: {daftar_stok[buku]}"
        )

    elif simbol == "+":
        daftar_stok[buku] += angka

        print(
            f"Stok '{buku}' bertambah {angka}. "
            f"Stok sekarang: {daftar_stok[buku]}"
        )

    else:
        print("Simbol perubahan tidak valid")

def termahal():
    if not daftar_harga:
        print("Belum ada buku yang terdaftar")
        return

    buku_tertinggi = None
    harga_tertinggi = -1

    for buku, harga in daftar_harga.items():
        if harga > harga_tertinggi:
            harga_tertinggi = harga
            buku_tertinggi = buku

    print(
        f"Buku termahal     : {buku_tertinggi} "
        f"(Rp{harga_tertinggi})"
    )

print()

print("=======================================")
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")

while True:
    try:
        print()

        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")

        menu = int(input("Pilih menu (1-5): ").strip())

        print(f"Menu yang dipilih: {menu}")

        if menu == 1:
            judul_buku = input("Judul buku: ").strip().title()
            penulis = input("Penulis: ").strip().title()
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))

            if not judul_buku or not penulis:
                print("Judul dan penulis tidak boleh kosong")
                continue

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif")
                continue

            tambah_buku(judul_buku, penulis, harga, stok)

            print()

            if judul_buku in daftar_buku:
                print(f"Buku '{judul_buku}' berhasil diproses!")

        elif menu == 2:
            cari_buku = input(
                "Masukkan kata kunci judul: "
            ).strip()

            mencari_buku(cari_buku)

        elif menu == 3:
            judul_buku = input(
                "Judul buku yang ingin diupdate: "
            ).strip().title()

            jumlah_perubahan = input(
                "Jumlah perubahan (contoh: +5 atau -3): "
            ).strip()

            if (
                len(jumlah_perubahan) < 2
                or jumlah_perubahan[0] not in ["+", "-"]
                or not jumlah_perubahan[1:].isdigit()
            ):
                print("Format perubahan tidak valid")
                continue

            simbol = jumlah_perubahan[0]
            angka = jumlah_perubahan[1:]

            update_stok(judul_buku, simbol, angka)

        elif menu == 4:
            print()

            print("===================================")
            print("  RINGKASAN INVENTARIS BOOKNEST")
            print("===================================")

            total_buku = len(daftar_buku)
            total_seluruh_stok = sum(daftar_stok.values())
            total_nilai_aset = 0

            for buku in daftar_buku:
                total_nilai_aset += (
                    daftar_harga[buku] * daftar_stok[buku]
                )

            print(f"Jumlah jenis buku : {total_buku}")
            print(f"Total seluruh stok: {total_seluruh_stok}")
            print(f"Total nilai aset  : Rp{total_nilai_aset}")

            termahal()

        elif menu == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Input yang Anda masukkan tidak valid")

    except ValueError:
        print("Input yang Anda masukkan tidak valid")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")