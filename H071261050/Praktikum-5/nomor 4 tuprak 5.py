def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
    else:
        local, domain = email.split("@")

        if local == "" or domain == "":
            error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

        if local.startswith(".") or local.endswith(".") or ".." in local:
            error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

        if "." not in domain:
            error.append("Bagian domain wajib memiliki minimal satu titik.")
        if ".." in domain or domain.endswith("."):
            error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

        if " " in email:
            error.append("Tidak boleh mengandung spasi.")

        if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
            error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    # cari email terpanjang
    lebar = 0
    for email in daftar_email_valid:
        if len(email) > lebar:
            lebar = len(email)

    garis = "+" + karakter_border * (lebar + 2) + "+"

    hasil = garis + "\n"
    for email in daftar_email_valid:
        hasil = hasil + "| " + email + " " * (lebar - len(email)) + " |\n"
    hasil = hasil + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")
print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break

    anomali = deteksi_anomali_email(email)

    if email in daftar_valid:
        anomali.append("Email sudah terdaftar (Duplikat).")

    if len(anomali) == 0:
        daftar_valid.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for pesan in anomali:
            print("   - " + pesan)


print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid, karakter_border))