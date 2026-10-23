#SISTEM MANAJEMEN PLAYLIST MUSIK "PLAYTUNE"
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    print("\n=======================================================")
    print(" No  Judul                Artis          Genre     Durasi")
    print("=======================================================")

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu

        menit = durasi // 60 # Menghitung jumlah menit penuh dengan membagi total durasi (dalam detik) dengan 60, lalu dibulatkan ke bawah menggunakan operator floor division (//).
        detik = durasi % 60 # Menghitung sisa detik setelah dikurangi menit penuh menggunakan operator modulo (%), yang menghasilkan sisa dari pembagian total durasi dengan 60.
        format_durasi = f"{menit}:{detik:02d}" #minimal 2 digit, dengan nol di depan jika angkanya hanya 1 digit.

        print(
            f" {nomor:<3} {judul:<20} {artis:<14} " #membuat teks rata kiri selebar ... karakter
            f"{genre:<9} {format_durasi}"
        )

        total_durasi += durasi

    print("=======================================================")

    total_menit = total_durasi // 60
    sisa_detik = total_durasi % 60

    print(
        f" Total durasi playlist: {total_menit} menit "
        f"{sisa_detik} detik"
    )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
    else:
        lagu = playlist.pop(nomor - 1) # Menghapus lagu dari playlist berdasarkan nomor yang dipilih
# Nomor dikurangi 1 karena indeks list dimulai dari 0
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("========================================")
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")

    print(f"  Total lagu      : {len(playlist)}")
    print(f"  Jumlah genre    : {len(genre_set)}")
    print(f"  Daftar genre    : {genre_set}")

    print("\n  Distribusi genre:")

    distribusi = {}

# Mengisi jumlah lagu setiap genre dengan nilai awal 0
    for genre in genre_set:
        distribusi[genre] = 0

    for lagu in playlist:
        distribusi[lagu[2]] += 1 # Menambah jumlah lagu pada genre yang sesuai sebanyak 1

    for genre in sorted(distribusi):
        print(
            f"    {genre:<12}: "
            f"{'#' * distribusi[genre]} ({distribusi[genre]})"
        )

    if len(playlist) > 0:
        lagu_terpanjang = playlist[0] #program mengambil lagu pertama dari playlist sebagai lagu terpanjang sementara.
        lagu_terpendek = playlist[0]

        for lagu in playlist:
            if lagu[3] > lagu_terpanjang[3]: #lagu [3] adalah lagu yang sedang di cek
                lagu_terpanjang = lagu

            if lagu[3] < lagu_terpendek[3]:
                lagu_terpendek = lagu

        menit_panjang = lagu_terpanjang[3] // 60
        detik_panjang = lagu_terpanjang[3] % 60

        menit_pendek = lagu_terpendek[3] // 60
        detik_pendek = lagu_terpendek[3] % 60

        print(
            f"\n  Lagu terpanjang : {lagu_terpanjang[0]} "
            f"({menit_panjang}:{detik_panjang:02d})"
        )
        print(
            f"  Lagu terpendek : {lagu_terpendek[0]} "
            f"({menit_pendek}:{detik_pendek:02d})"
        )
    else:
        print("\n  Lagu terpanjang : Tidak ada")
        print("  Lagu terpendek : Tidak ada")

    print("========================================")


playlist = []
genre_set = set() #supaya tidak ada yang duplikat, maka digunakan set untuk menyimpan genre

print("========================================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif!")
            elif judul == "" or artis == "" or genre == "":
                print("Judul, artis, dan genre tidak boleh kosong!")
            else:
                tambah_lagu(
                    playlist, genre_set, judul, artis, genre, durasi
                )

        except:
            print("Durasi harus berupa angka positif!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre yang ingin difilter: ")

        hasil = filter_genre(playlist, genre_target)

        if len(hasil) == 0:
            print(f"Tidak ada lagu bergenre '{genre_target}'.")
        else:
            print(f"\nLagu bergenre '{genre_target}':")

            for nomor, lagu in enumerate(hasil, start=1):
                menit = lagu[3] // 60
                detik = lagu[3] % 60

                print(
                    f"  {nomor}. {lagu[0]} - {lagu[1]} "
                    f"({menit}:{detik:02d})"
                )

    elif pilihan == "4":
        tampilkan_playlist(playlist)

        try:
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)

            genre_set = set()

            for lagu in playlist:
                genre_set.add(lagu[2])

        except:
            print("Nomor lagu harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid! Masukkan pilihan 1-6.")