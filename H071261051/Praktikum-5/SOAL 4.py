def deteksi_anomali_email(email):
    masalah = []

    if email.count("@") != 1:
        masalah.append("Jumlah @ salah.")

    if email.find(" ") != -1:
        masalah.append("Ada spasi.")

    if email.count("@") == 1:
        pos = email.find("@")
        local = email[:pos]
        domain = email[pos + 1:]

        if len(local) == 0 or len(domain) == 0:
            masalah.append("Local/domain kosong.")

        if local.startswith(".") or local.endswith(".") or local.find("..") != -1:
            masalah.append("Titik pada local salah.")

        if domain.count(".") == 0:
            masalah.append("Domain tidak punya titik.")

        if domain.find("..") != -1 or domain.endswith("."):
            masalah.append("Titik pada domain salah.")

        email_kecil = email.lower()

        if not (email_kecil.endswith(".com") or email_kecil.endswith(".id") or email_kecil.endswith(".ac.id")):
            masalah.append("Domain tidak sesuai.")

    return masalah


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(karakter_border) == 0:
        karakter_border = "="

    karakter_border = karakter_border[0]

    terpanjang = 0

    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"

    hasil = garis

    for email in daftar_email_valid:
        hasil = hasil + "\n" + "| " + email + " " * (terpanjang - len(email)) + " |"

    hasil = hasil + "\n" + garis

    return hasil


print("--- Sistem Pencatatan email valid ---")

border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    masalah = deteksi_anomali_email(email)

    duplikat = False

    for tersimpan in daftar_valid:
        if tersimpan.lower() == email.lower():
            duplikat = True

    if duplikat:
        masalah.append("Email duplikat.")

    if len(masalah) == 0:
        daftar_valid.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")

        for m in masalah:
            print(f"   - {m}")

print()
print("--- HASIL EMAIL VALID ---")

if len(daftar_valid) == 0:
    print("Tidak ada email valid.")
else:
    print(cetak_daftar(daftar_valid, border))


    