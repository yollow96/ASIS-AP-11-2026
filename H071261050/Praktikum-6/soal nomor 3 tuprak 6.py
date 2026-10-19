playlist = []
genre_set = set()

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    data_lagu = (judul, artis, genre, durasi)
    playlist.append(data_lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    print("=" * 55)
    print(f"{'No':<4}{'Judul':<20}{'Artis':<14}{'Genre':<9}{'Durasi'}")
    print("=" * 55)

    nomor = 0
    total_detik = 0
    for judul, artis, genre, durasi in playlist:
        nomor += 1
        menit = durasi // 60 #floor division, pembagian bulat kebawah
        sisa = durasi % 60 #sisa bagi
        print(f"{nomor:<4}{judul:<20}{artis:<18}{genre:<9}{menit}:{sisa:02d}")
        total_detik += durasi

    print("=" * 55)
    total_menit = total_detik // 60
    total_sisa = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {total_sisa} detik")

def filter_genre(playlist, genre_target):
    return[lagu for lagu in playlist if lagu [2] == genre_target]

def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' oleh {lagu[1]} berhasil dihapus.")

def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    terpanjang = playlist[0] #ambil lagu pertama dari playlsit
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    menit_panjang = terpanjang[3] // 60
    sisa_panjang = terpanjang[3] % 60
    menit_pendek = terpendek[3] // 60
    sisa_pendek = terpendek[3] % 60

    print("=" * 40)
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"  {'Total lagu':<14}: {len(playlist)}")
    print(f"  {'Jumlah genre':<14}: {len(genre_set)}")
    print(f"  {'Daftar genre':<14}: {genre_set}")
    print()
    print("  Distribusi genre:")
    for genre in distribusi:
        print(f"    {genre:<10}: {'#' * distribusi[genre]} ({distribusi[genre]})")
    print()
    print(f"  {'Lagu terpanjang':<16}: {terpanjang[0]} ({menit_panjang}:{sisa_panjang:02d})")
    print(f"  {'Lagu terpendek':<16}: {terpendek[0]} ({menit_pendek}:{sisa_pendek:02d})")
    print("=" * 40)


print("=" * 40)
print("      PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)
print()
print("Menu: ")
print("1. Tambah Lagu")
print("2. Tampilkan Playlist")
print("3. Filter Genre")
print("4. Hapus Lagu")
print("5. Statistik Playlist")
print("6. Keluar")

while True:
    pilihan = int(input("Pilih menu (1-6): "))

    if pilihan == 1:
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
                print()
        except ValueError:
            print("Durasi harus berupa angka!")

    if pilihan == 2:
        tampilkan_playlist(playlist)
        print()

    if pilihan == 3:
        print(f"Genre tersedia: {genre_set}")
        genre_dicari = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, genre_dicari)
        if len(hasil) == 0:
            print("Tidak ada lagu dengan genre tersebut.")
        else:
            print(f"Lagu bergenre '{genre_dicari}':")
            nomor = 0
            for judul, artis, genre, durasi in hasil:
                nomor += 1
                print(f"  {nomor}. {judul} - {artis} ({durasi // 60}:{durasi % 60:02d})")
                print()

    if pilihan == 4:
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("Nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)
        except ValueError:
            print("Nomor harus berupa angka!")

    if pilihan == 5:
        statistik_playlist(playlist, genre_set)

    if pilihan == 6:
        print("Terimakasih telah menggunakan PlayTune!")
        break