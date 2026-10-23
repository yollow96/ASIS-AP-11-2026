inventaris = []

def tambah_buku (inventaris, judul, penulis, harga, stok):
    data_seluruh_buku = {
        "judul": judul,
        "penulis": penulis, 
        "harga": harga, 
        "stok": stok}
    inventaris.append(data_seluruh_buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
            len(hasil)

    print(f"Ditemukan {len(hasil)} buku: ")
    nomor = 0

    for buku in hasil:
        nomor += 1
        print(f"{nomor}. {buku["judul"]} - {buku["penulis"]} | Rp{buku["harga"]} | Stok: {buku["stok"]}")

def update_stok(inventaris, judul, jumlah):
    stok_baru = 0
    for buku in inventaris:
        if judul == buku["judul"]:
            stok_baru = buku["stok"] + jumlah
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
        else:
            buku["stok"] = stok_baru
        if jumlah < 0:
            print(f"Stok '{judul}' berkurang {jumlah}. Stok sekarang: {stok_baru}")
        elif jumlah >= 0:
            print(f"Stok '{judul}' bertambah {jumlah}. Stok sekarang: {stok_baru}")

def ringkasan_inventaris(inventaris):
    total_stok = 0
    total_aset = 0
    termahal = inventaris[0]
    for buku in inventaris:
        total_stok = total_stok + buku["stok"]
        total_aset = total_aset + buku["harga"]
    if buku["harga"] > termahal["harga"]:
        termahal = buku
    print(f"Jumlah jenis buku: {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset: {total_aset}")
    print(f"Buku termahal: {termahal['judul']} (Rp{termahal['harga']})")

while True:
    print("Menu: ")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    pilihan = int(input("Pilih menu (1-5): "))

    if pilihan == 1:   
        input_judul = input("Judul buku: ")
        nama_penulis = input("Penulis: ")
        while True:
                try:
                    harga_per_buku = int(input("Harga: "))
                    stok_buku = int(input("Stok awal: "))
                    if harga_per_buku < 0 or stok_buku < 0:
                        print("Harga dan stok tidak boleh negatif!") 
                    else:
                        tambah_buku(inventaris, input_judul, 
                                    nama_penulis, harga_per_buku, stok_buku)
                        break
                except ValueError:
                    print("Harga dan stok harus berupa angka!")

    if pilihan == 2:
        kata_kunci = input("Masukkan kata kunci: ")
        cari_buku(inventaris, kata_kunci)

    if pilihan == 3:
        judul_update = input("Judul buku yang ingin diupdate: ")
        perubahan_stok = int(input("Jumlah perubahan (positif = tambah, negatif = kurang): "))
        update_stok(inventaris, judul_update, perubahan_stok)

    if pilihan == 4:
        print("========================================")
        print("RINGKASAN INVENTARIS BOOKNEST")
        print("========================================")
        ringkasan_inventaris(inventaris)
        print("========================================")

    if pilihan == 5:
        print("Terimakasih telah menggunakan BookNest!")
        break



        

    
