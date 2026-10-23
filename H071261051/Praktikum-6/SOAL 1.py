#SISTEM INVENTARIS TOKO BUKU BOOKNEST
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Buku tidak ditemukan!")
    else:
        print(f"Ditemukan {len(hasil)} buku:")

        for nomor, buku in enumerate(hasil, start=1): #memeberikan nomor urut ke buku
            print(
                f"  {nomor}. {buku['judul']} - {buku['penulis']} "
                f"| Rp{buku['harga']} | Stok: {buku['stok']}"
            )


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0: #menggunakan kondisi ini untuk mencegah stok buku menjadi negatif
                print("Gagal update stok! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru

                if jumlah > 0:
                    print(
                        f"Stok '{buku['judul']}' bertambah {jumlah}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
                elif jumlah < 0:
                    print(
                        f"Stok '{buku['judul']}' berkurang {-jumlah}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
                else:
                    print(
                        f"Stok '{buku['judul']}' tetap: {buku['stok']}"
                    )
            return

    print("Error: Buku tidak ditemukan!")


def ringkasan_inventaris(inventaris):
    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")

    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")

    if len(inventaris) > 0:
        buku_termahal = inventaris[0]

        for buku in inventaris:
            if buku["harga"] > buku_termahal["harga"]: #mengambil harga buku yang sedang diperiksa
                buku_termahal = buku #variabel buku_termahal diganti dengan data buku yang memiliki harga lebih tinggi

        print(
            f"Buku termahal     : {buku_termahal['judul']} "
            f"(Rp{buku_termahal['harga']})"
        )
    else:
        print("Buku termahal     : Tidak ada")

    print("========================================")


inventaris = []

print("========================================")
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ").strip()
        penulis = input("Penulis: ").strip()

        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            elif judul == "" or penulis == "":
                print("Judul dan penulis tidak boleh kosong!")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)

        except:
            print("Harga dan stok harus berupa angka!")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(
                input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            )
            update_stok(inventaris, judul, jumlah)

        except:
            print("Jumlah perubahan harus berupa angka!")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid! Masukkan pilihan 1-5.")