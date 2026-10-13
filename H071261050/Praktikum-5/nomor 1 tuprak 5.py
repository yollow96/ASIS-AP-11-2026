def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for karakter in teks:
        if karakter.lower() in alfabet:
            hasil = hasil + karakter.lower()
    return hasil

def cek_palinrome(teks):
    balik_teks = "".join(reversed(teks))
    if teks == balik_teks:
        return (True, -1)
    for beda in range (len(teks)):
        if teks[beda] != balik_teks[beda]:
            return (False, beda)

def inti_palinrome(teks):
    terpanjang = ""
    indeks_awal = 0
    for i in range(len(teks)):
        for j in range (i + 1, len(teks) + 1):
            sub = teks[i:j]
            if cek_palinrome(sub)[0] and len(sub) > len(terpanjang):
                terpanjang = sub
                indeks_awal = i
    return {"teks": terpanjang, "panjang": len(terpanjang), "indeks_awal": indeks_awal}

teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print("\nTeks Bersih: ", bersih)
print("Output Terharap: ", inti_palinrome(bersih))