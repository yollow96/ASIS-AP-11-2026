def tambah_buku(inventaris, judul, penulis, harga, stok):
    inventaris.append({"judul": judul, "penulis": penulis, "harga": harga, "stok": stok})
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    ditemukan = [b for b in inventaris if kata_kunci.lower() in b['judul'].lower()]
    print(f"Ditemukan {len(ditemukan)} buku:")
    for i, b in enumerate(ditemukan, 1):
        print(f"{i}. {b['judul']} | {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")

def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b['judul'].lower() == judul.lower():
            if b['stok'] + jumlah < 0:
                print("Gagal: Stok tidak boleh negatif!")
                return
            b['stok'] += jumlah
            if jumlah < 0:
                print(f"Stok '{b['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {b['stok']}")
            else:
                print(f"Stok '{b['judul']}' bertambah. Stok sekarang: {b['stok']}")
            return
    print("Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong!")
        return
    total_stok = sum(b['stok'] for b in inventaris)
    total_aset = sum(b['harga'] * b['stok'] for b in inventaris)
    termahal = max(inventaris, key=lambda x: x['harga'])
    print("\n=== RINGKASAN INVENTARIS BOOKNEST ===")
    print(f"Jumlah jenis buku: {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset: Rp{total_aset}")
    print(f"Buku termahal: {termahal['judul']} (Rp{termahal['harga']})")
    print("=======================================")

# --- BAGIAN MENU UTAMA (LOOP) ---
print("=======================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")

inventaris_buku = []

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(inventaris_buku, judul, penulis, harga, stok)
        except ValueError:
            print("Input gagal! Harga dan stok harus berupa angka.")
            
    elif pilihan == '2':
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris_buku, kata_kunci)
        
    elif pilihan == '3':
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris_buku, judul, jumlah)
        except ValueError:
            print("Input gagal! Jumlah perubahan harus berupa angka.")
            
    elif pilihan == '4':
        ringkasan_inventaris(inventaris_buku)
        
    elif pilihan == '5':
        print("Terima kasih telah menggunakan BookNest!")
        break
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")