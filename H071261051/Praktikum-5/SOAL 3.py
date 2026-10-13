ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):#Menggeser satu karakter sesuai kunci Caesar
    huruf_kecil = ch.lower()
    posisi = ALFABET.find(huruf_kecil)

    if posisi == -1:
        return ch

    posisi_baru = (posisi + k) % 26 # Menghitung posisi baru huruf dan kembali ke awal alfabet jika melewati z
    hasil = ALFABET[posisi_baru] # Mengambil huruf sesuai posisi baru

    if ch == ch.upper():
        return hasil.upper()
    else:
        return hasil.lower()


def mesin_enkripsi(teks, k):# Mengenkripsi (mengubah ke pesan asli) seluruh teks dengan menggeser setiap karakter

    hasil = ""

    for karakter in teks:
        hasil = hasil + cek_sandi(karakter, k)  # Menggeser setiap karakter sesuai kunci, lalu menggabungkan hasilnya ke variabel hasil

    return hasil


def mesin_dekripsi(teks, k): # Mengembalikan teks tersandi menjadi teks asli
    return mesin_enkripsi(teks, -k)  # Menggeser huruf ke arah berlawanan menggunakan kunci negatif


def retas_sandi(sandi, kata_kunci):  #Mencoba berbagai kunci untuk mencari pesan asli berdasarkan kata kunci
    hasil = []

    if len(kata_kunci) == 0:
        return hasil

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci) # Mendekripsi pesan dengan kunci yang sedang dicoba

        if pesan_asli.lower().find(kata_kunci.lower()) != -1: # Memeriksa apakah pesan mengandung kata kunci
            hasil.append((kunci, pesan_asli))

    return hasil


sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi, kata_kunci)

print()
print(f"Output Deskripsi: {hasil}")