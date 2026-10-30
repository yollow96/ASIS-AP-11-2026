kandidat_set = set()
print("=== FASE PENDAFTARAN KANDIDAT ===")
while True:
    nama = input("Masukkan nama kandidat: ").capitalize()
    if not nama:
        if len(kandidat_set) >= 2: break
        else: print("Minimal 2 kandidat!"); continue
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan!")

print("=== FASE PEMUNGUTAN SUARA ===")
rekap_suara = {}
while True:
    pemilih = input("Nama pemilih (kosongkan untuk selesai): ").lower()
    if not pemilih: break
    if pemilih in rekap_suara:
        print(f"'{pemilih.capitalize()}' sudah memberikan suara!")
        continue
    
    pilihan = input("Pilih kandidat: ").capitalize()
    if pilihan not in kandidat_set:
        print("Kandidat tidak valid!")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara untuk '{pilihan}' dicatat!")

print("=== HASIL PEMILIHAN ===")
hasil = {k: 0 for k in kandidat_set}
for v in rekap_suara.values(): hasil[v] += 1
for k, v in hasil.items(): print(f"{k}: {v} suara")

max_suara = max(hasil.values())
pemenang = [k for k, v in hasil.items() if v == max_suara]
if len(pemenang) > 1:
    print(f"Hasil SERI antara: {', '.join(pemenang)}\nPerlu pemilihan ulang!")
else:
    print(f"PEMENANG: {pemenang[0]} dengan {max_suara} suara!")