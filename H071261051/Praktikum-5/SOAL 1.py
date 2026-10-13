ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    teks_bersih = ""

    for karakter in teks:
        karakter_kecil = karakter.lower()

        if ALFABET.find(karakter_kecil) != -1:#apakah data variabel k_k termasuk huruf alfabet.
            teks_bersih = teks_bersih + karakter_kecil

    return teks_bersih


def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks)) 

    if teks == teks_balik:
        return (True, -1) #penanda tdk ada karakter yg berbeda

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i) #indeks awal ditemukan perbedaan huruf


def inti_palinrome(teks_bersih):
    panjang_teks = len(teks_bersih)

    panjang_maksimal = 0
    substring_terbaik = ""
    indeks_terbaik = 0

    for i in range(panjang_teks):
        for j in range(i + 1, panjang_teks + 1):
            bagian = teks_bersih[i:j]

            hasil_cek = cek_palinrome(bagian) #potongan kata yg sdg diuji dimasukkan ke fungsi c_p dan disimpan ke variabel h_c

            if hasil_cek[0]:
                if len(bagian) > panjang_maksimal:
                    panjang_maksimal = len(bagian)
                    substring_terbaik = bagian
                    indeks_terbaik = i

    return {"teks": substring_terbaik, "panjang": panjang_maksimal, "indeks_awal": indeks_terbaik}


masukan = input("Masukkan teks prasasti: ")
print()

teks_bersih = bersihkan_teks(masukan)
hasil = inti_palinrome(teks_bersih)

print(f"Teks Bersih: {teks_bersih}")
print(f"Output Terharap: {hasil}")