def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sblm_ok = (i == 0) or (teks[i-1] not in alfabet)
    ssdh_ok = (i + panjang == len(teks)) or (teks[i+panjang] not in alfabet)
    return sblm_ok and ssdh_ok

def sensor_kata(teks, kata, simbol):
    teks_lower = ""
    for c in teks:
        teks_lower += c.lower()
    kata_lower = ""
    for c in kata:
        kata_lower += c.lower()
        
    hasil = ""
    indeks_awal = []
    jumlah = 0
    i = 0
    while i < len(teks):
        idx = teks_lower.find(kata_lower, i)
        if idx == i and cek_batas_kata(teks, i, len(kata)):
            hasil += simbol * len(kata)
            indeks_awal.append(i)
            jumlah += 1
            i += len(kata)
        else:
            hasil += teks[i]
            i += 1
    return hasil, jumlah, indeks_awal

teks_input = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_input = input("Masukkan simbol: ")

teks_hasil, jml, idx_awal = sensor_kata(teks_input, kata_target, simbol_input)

print(f"Hasil Teks: {teks_hasil}")
print(f"Jumlah: {jml}  Indeks: {idx_awal}")