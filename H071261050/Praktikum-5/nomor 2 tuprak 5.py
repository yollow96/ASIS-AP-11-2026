alfabet = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    hasil = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        posisi = teks_kecil.find(kata_kecil, start)
        if posisi == -1:
            break
        hasil.append(posisi)
        start = posisi + 1
    return hasil

def cek_batas_kata(teks, posisi, panjang):
    posisi_kanan = posisi + panjang

    if posisi > 0:
        if teks[posisi - 1].lower() in alfabet:
            return False

    if posisi_kanan < len(teks):
        if teks [posisi_kanan].lower() in alfabet:
            return False
    return True

def sensor_kata(teks, kata, simbol):
    hasil = ""
    indeks = []
    terakhir_disalin = 0
    for posisi in cek_kata(teks, kata):
        if cek_batas_kata(teks, posisi, len(kata)):
            hasil = hasil + teks[terakhir_disalin:posisi] + simbol * len(kata)
            terakhir_disalin = posisi + len(kata)
            indeks.append(posisi)
    hasil = hasil + teks[terakhir_disalin:]
    return hasil, len(indeks), indeks


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil teks: ", hasil)
print("Jumlah", jumlah, "| indeks: ", indeks)


