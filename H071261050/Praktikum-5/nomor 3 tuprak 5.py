alfabet = "abcdefghijklmnopqrstuvwxyz"
def cek_sandi(ch, k):
    if ch.lower() not in alfabet:
        return ch
    posisi = alfabet.find(ch.lower())
    huruf_baru = alfabet[(posisi + k) % 26]
    if ch == ch.upper():
        return huruf_baru.upper()
    return huruf_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

print("\nOutput Deskripsi: ", retas_sandi(sandi, kata_kunci))