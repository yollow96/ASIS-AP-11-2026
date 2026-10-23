def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = genre.capitalize()

    lagu = (judul, artis, genre, durasi)#informasi lagu
    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def format_durasi(durasi):
    menit = durasi // 60
    detik = durasi % 60 #menghitung sisa detik

    return f"{menit}:{detik:02d}"


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("\nPlaylist masih kosong!")
        return

    print("\n======================================================")
    print(" No  Judul                 Artis          Genre    Durasi")
    print("======================================================")

    total_durasi = 0

    for i, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu

        print(
            f"{i:<4} {judul:<22} {artis:<14} "
            f"{genre:<9} {format_durasi(durasi)}"
        )

        total_durasi += durasi

    print("======================================================")

    menit = total_durasi // 60
    detik = total_durasi % 60

    print(f"Total durasi playlist: {menit} menit {detik} detik")


def filter_genre(playlist, genre_target):
    hasil_filter = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil_filter


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
    else:
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus dari playlist!")


def statistik_playlist(playlist, genre_set):
    print("\n=======================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("=======================================")

    print(f"Total lagu       : {len(playlist)}")
    print(f"Jumlah genre     : {len(genre_set)}")
    print(f"Daftar genre     : {genre_set}")

    print("\nDistribusi genre:")

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre not in distribusi:
            distribusi[genre] = 0

        distribusi[genre] += 1

    for genre, jumlah in distribusi.items():
        print(f"  {genre:<12}: # ({jumlah})")

    if len(playlist) > 0:
        lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
        lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

        print(
            f"\nLagu terpanjang : {lagu_terpanjang[0]} "
            f"({format_durasi(lagu_terpanjang[3])})"
        )

        print(
            f"Lagu terpendek  : {lagu_terpendek[0]} "
            f"({format_durasi(lagu_terpendek[3])})"
        )
    else:
        print("\nBelum ada lagu dalam playlist.")

    print("=======================================")


# PROGRAM UTAMA

playlist = []
genre_set = set()

print("=======================================")
print("       PLAYLIST MUSIK - PLAYTUNE")
print("=======================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")

        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))

                if durasi <= 0:
                    print("Durasi harus berupa angka positif!")
                    continue

                break

            except ValueError:
                print("Input tidak valid! Masukkan angka positif.")

        tambah_lagu(
            playlist,
            genre_set,
            judul,
            artis,
            genre,
            durasi
        )

    elif menu == "2":
        tampilkan_playlist(playlist)

    elif menu == "3":
        if len(genre_set) == 0:
            print("Belum ada genre tersedia!")
            continue

        print(f"Genre tersedia: {genre_set}")

        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(playlist, genre_target)

        print(f"\nLagu bergenre '{genre_target.capitalize()}':")

        if len(hasil_filter) == 0:
            print("Tidak ada lagu dengan genre tersebut.")
        else:
            for i, lagu in enumerate(hasil_filter, start=1):
                judul, artis, genre, durasi = lagu

                print(
                    f"  {i}. {judul} - {artis} "
                    f"({format_durasi(durasi)})"
                )

    elif menu == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong!")
            continue

        tampilkan_playlist(playlist)

        try:
            nomor = int(input("\nMasukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)

            genre_set.clear()

            for lagu in playlist:
                genre_set.add(lagu[2])

        except ValueError:
            print("Input tidak valid! Masukkan nomor lagu berupa angka.")

    elif menu == "5":
        statistik_playlist(playlist, genre_set)

    elif menu == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid! Silakan pilih 1-6.")
