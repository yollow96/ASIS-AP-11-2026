kandidat_set = set()

def daftar_kandidat(kandidat_set, nama):
    kandidat_set.add(nama)

rekap_suara = {}
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"'{pilihan}' bukan kandidat!")
    else:
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    rekap_suara[nama_pemilih] = pilihan

def hitung_suara(rekap_suara, kandidat_set):
    hasil = {}
    for kandidat in kandidat_set:
        hasil[kandidat] = 0

    for pemilih in rekap_suara:
        pilihan = rekap_suara[pemilih]
        hasil[pilihan] = hasil[pilihan] + 1

    for kandidat in hasil:
        print(f"{kandidat}: {hasil[kandidat]} suara")

    print()    
    print(f"Total suara masuk: {len(rekap_suara)}")

    suara_tertinggi = max(hasil.values())
    pemenang = []
    for kandidat in hasil:
        if hasil[kandidat] == suara_tertinggi:
            pemenang.append(kandidat)

    if len(pemenang) == 1:
        print(f"PEMENANG: {pemenang[0]}")
    else:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")


while True:
    kandidat = input("Masukkan nama kandidat (kosongkan untuk  selesai): ").capitalize()
    print(f"'{kandidat}' berhasil didaftarkan sebagai kandidat!")
    if kandidat == "":
        if len(kandidat_set) < 2:
            print("Kandidat pilihan minimal 2 orang.")
            continue
        else:
            break
    daftar_kandidat(kandidat_set, kandidat)
print()
print(f"Kandidat terdaftar: {kandidat_set}")

print()
print("---FASE PEMUNGUTAN SUARA---")
print()
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
    if nama_pemilih == "":
        break
    print(f"kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").capitalize()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
    print()

print("========================================")
print("     HASIL PEMILIHAN KETUA KELAS")
print("========================================")
hitung_suara(rekap_suara, kandidat_set)
print("========================================")
