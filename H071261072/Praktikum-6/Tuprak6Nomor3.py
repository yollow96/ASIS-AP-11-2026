
print("Khaerul")

judul_nya = list()
artis_nya = list()
genre_nya = set()
durasi_nya = list()
lagu_dan_genre = {}
genre_dan_total = {}

genre = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    if judul in playlist:
        print("Judul lagu sudah terdaftar!")
        return False

    playlist[judul] = genre_set
    judul_nya.append(judul)
    artis_nya.append(artis)
    genre_nya.add(genre)
    durasi_nya.append(durasi)

    genre_dan_total[genre_set] = (
        genre_dan_total.get(genre_set, 0) + 1
    )

    return True


def tampilkan_playlist(playlist):
    if not judul_nya:
        print("Playlist masih kosong!")
        return

    total_durasi = sum(durasi_nya)
    total_durasi_menit = total_durasi // 60
    total_durasi_detik = total_durasi % 60

    judul_terpanjang = max(
        len("Judul"),
        max(len(i) for i in judul_nya)
    )

    artis_terpanjang = max(
        len("Artis"),
        max(len(i) for i in artis_nya)
    )

    genre_terpanjang = max(
        len("Genre"),
        max(len(i) for i in genre_nya)
    )

    durasi_terpanjang = max(
        len("Durasi"),
        max(len(f"{i // 60}:{i % 60:02d}") for i in durasi_nya)
    )

    garis = (
        f"====={judul_terpanjang * '='}=="
        f"{artis_terpanjang * '='}=="
        f"{genre_terpanjang * '='}==="
        f"{durasi_terpanjang * '='}="
    )

    print(garis)

    print(
        f" No  Judul{' ' * (judul_terpanjang - 5)}  "
        f"Artis{' ' * (artis_terpanjang - 5)}  "
        f"Genre{' ' * (genre_terpanjang - 5)}   Durasi"
    )

    print(garis)

    for i in range(len(judul_nya)):
        menit = durasi_nya[i] // 60
        detik = durasi_nya[i] % 60

        print(
            f" {i + 1:<3} "
            f"{judul_nya[i].ljust(judul_terpanjang)}  "
            f"{artis_nya[i].ljust(artis_terpanjang)}  "
            f"{playlist[judul_nya[i]].ljust(genre_terpanjang)}   "
            f"{menit}:{detik:02d}"
        )

    print(garis)

    print(
        f"Total durasi playlist: "
        f"{total_durasi_menit} menit {total_durasi_detik} detik"
    )

    print()


def filter_genre(playlist, genre_target):
    if not playlist:
        print("Playlist masih kosong!")
        return

    print(f"Lagu bergenre '{genre_target}':")

    urutan = 1

    for i in range(len(judul_nya)):
        if playlist[judul_nya[i]] == genre_target:
            menit = durasi_nya[i] // 60
            detik = durasi_nya[i] % 60

            print(
                f"  {urutan}. {judul_nya[i]} - "
                f"{artis_nya[i]} ({menit}:{detik:02d})"
            )

            urutan += 1

    if urutan == 1:
        print("Tidak ada lagu dengan genre tersebut.")


def hapus_lagu(playlist, nomor):
    if not judul_nya:
        print("Playlist masih kosong!")
        return False

    if nomor < 1 or nomor > len(judul_nya):
        print("Nomor lagu tidak valid!")
        return False

    indeks = nomor - 1

    judul = judul_nya[indeks]

    playlist.pop(judul)
    judul_nya.pop(indeks)
    artis_nya.pop(indeks)
    durasi_nya.pop(indeks)

    genre_nya.clear()
    genre_nya.update(playlist.values())

    genre_dan_total.clear()

    for nilai_genre in playlist.values():
        genre_dan_total[nilai_genre] = (
            genre_dan_total.get(nilai_genre, 0) + 1
        )

    print(f"Lagu '{judul}' berhasil dihapus!")

    tampilkan_playlist(playlist)

    return True


def statistik_playlist(playlist, genre_dan_total):
    print("===============================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("===============================================")

    if not playlist:
        print("Playlist masih kosong!")
        print("Total lagu        : 0")
        print("Jumlah genre      : 0")
        print("Daftar genre      : Tidak ada")
        print("===============================================")
        return

    lagu_terpanjang = durasi_nya.index(max(durasi_nya))
    lagu_terpendek = durasi_nya.index(min(durasi_nya))

    menit_panjang = durasi_nya[lagu_terpanjang] // 60
    detik_panjang = durasi_nya[lagu_terpanjang] % 60

    menit_pendek = durasi_nya[lagu_terpendek] // 60
    detik_pendek = durasi_nya[lagu_terpendek] % 60

    print(f"Total lagu        : {len(judul_nya)}")
    print(f"Jumlah genre      : {len(genre_nya)}")
    print(f"Daftar genre      : {sorted(genre_nya)}")

    print()
    print("Distribusi genre:")

    for key, value in sorted(genre_dan_total.items()):
        print(f"  {key} : {value} lagu")

    print()

    print(
        f"Lagu terpanjang  : {judul_nya[lagu_terpanjang]} "
        f"({menit_panjang}:{detik_panjang:02d})"
    )

    print(
        f"Lagu terpendek   : {judul_nya[lagu_terpendek]} "
        f"({menit_pendek}:{detik_pendek:02d})"
    )

    print("===============================================")


print("===============================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("===============================")


while True:
    print()
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    try:
        menu = int(input("Pilih menu (1-6): ").strip())

    except ValueError:
        print("Input yang Anda masukkan tidak valid!")
        continue

    if menu == 1:
        judul_lagu = input("Judul lagu: ").strip().title()
        artis_lagu = input("Artis: ").strip().title()

        genre_lagu = input(
            "(Pop/Rock/Jazz/RnB/Dangdut): "
        ).strip()

        if genre_lagu.lower() == "rnb":
            genre_lagu = "RnB"
        else:
            genre_lagu = genre_lagu.title()

        if not judul_lagu or not artis_lagu:
            print("Judul lagu dan artis tidak boleh kosong!")
            continue

        if genre_lagu not in genre:
            print("Genre yang Anda masukkan tidak valid!")
            continue

        try:
            durasi_lagu = int(
                input("Durasi (dalam detik): ").strip()
            )

        except ValueError:
            print("Durasi harus berupa angka!")
            continue

        if durasi_lagu <= 0:
            print("Durasi harus lebih dari nol!")
            continue

        berhasil = tambah_lagu(
            lagu_dan_genre,
            genre_lagu,
            judul_lagu,
            artis_lagu,
            genre_lagu,
            durasi_lagu
        )

        if berhasil:
            print(
                f"Lagu '{judul_lagu}' oleh {artis_lagu} "
                "berhasil ditambahkan!"
            )

    elif menu == 2:
        tampilkan_playlist(lagu_dan_genre)

    elif menu == 3:
        if not lagu_dan_genre:
            print("Playlist masih kosong!")
            continue

        print(f"Genre tersedia: {sorted(genre_nya)}")

        filter_genrenya = input(
            "Masukkan genre yang ingin difilter: "
        ).strip()

        if filter_genrenya.lower() == "rnb":
            filter_genrenya = "RnB"
        else:
            filter_genrenya = filter_genrenya.title()

        if filter_genrenya not in genre:
            print("Genre yang Anda masukkan tidak valid!")
            continue

        filter_genre(lagu_dan_genre, filter_genrenya)

    elif menu == 4:
        if not judul_nya:
            print("Playlist masih kosong!")
            continue

        tampilkan_playlist(lagu_dan_genre)

        try:
            nomor = int(
                input("Masukkan nomor lagu yang ingin dihapus: ")
            )

        except ValueError:
            print("Nomor lagu harus berupa angka!")
            continue

        hapus_lagu(lagu_dan_genre, nomor)

    elif menu == 5:
        statistik_playlist(
            lagu_dan_genre,
            genre_dan_total
        )

    elif menu == 6:
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid!")
