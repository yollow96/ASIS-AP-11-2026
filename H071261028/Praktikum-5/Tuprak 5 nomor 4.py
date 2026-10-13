def deteksi_anomali_email(email):
    error = []

    # 1. Harus memiliki tepat satu karakter @
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    # Pisahkan local dan domain
    local, domain = email.split("@")#memisahkan string berdasarkan karakter

    # 2. Local dan domain tidak boleh kosong
    if local == "" or domain == "":
        error.append(
            "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
        )

    # 3. Tidak boleh mengandung spasi
    if " " in email:
        error.append("Tidak boleh mengandung spasi di posisi manapun.")

    # 4. Aturan local
    if local != "":#hanya memeriksa aturan local jika bagian memiliki isi
        if local.startswith(".") or local.endswith(".") or ".." in local:
            error.append(
                "Bagian local tidak boleh diawali atau diakhiri titik (.), "
                "serta tidak boleh mengandung titik berurutan (..)."
            )

    # 5. Aturan domain
    if domain != "":
        if "." not in domain:
            error.append(
                "Bagian domain wajib memiliki minimal satu titik."
            )

        if ".." in domain or domain.endswith("."):
            error.append(
                "Bagian domain tidak boleh mengandung titik berurutan "
                "atau diakhiri titik."
            )

    # 6. Tidak boleh duplikat
    # Dicek di program utama karena membutuhkan daftar email yang sudah valid.

    # 7. Harus berakhir dengan domain resmi
    if not (
        email.endswith(".com")
        or email.endswith(".id")
        or email.endswith(".ac.id")
    ):
        error.append(
            "Wajib berakhiran dengan .com, .id, atau .ac.id"
        )

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return

    # Mencari email terpanjang
    email_terpanjang = daftar_email_valid[0]

    for email in daftar_email_valid:
        if len(email) > len(email_terpanjang):
            email_terpanjang = email

    # Padding satu spasi di kiri dan kanan
    lebar = len(email_terpanjang) + 2

    border = karakter_border * (lebar + 2)

    print()
    print("--- HASIL EMAIL VALID ---")
    print("+" + border + "+")

    for email in daftar_email_valid:
        jumlah_spasi = lebar - len(email)

        print("| " + email + (" " * jumlah_spasi) + " |")

    print("+" + border + "+")


# Program utama
daftar_email_valid = []

print("--- Sistem Pencatatan email valid ---")

karakter_border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email: ")

    # Mengakhiri program
    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    # Cek duplikat
    if len(error) == 0:
        if email in daftar_email_valid:
            error.append("Email sudah terdaftar (Duplikat).")

    # Jika tidak ada error
    if len(error) == 0:
        daftar_email_valid.append(email)

        print(">> Email VALID!")

    # Jika ada error
    else:
        print(">> Email DITOLAK karena:")

        for pesan in error:
            print("   - " + pesan)

cetak_daftar(daftar_email_valid, karakter_border)