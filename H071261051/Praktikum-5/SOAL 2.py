ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata): #mencari kata target
    indeks = []
    start = 0 #pencarian kata dimulai dari indeks 0

    if len(kata) == 0:
        return indeks

    teks_kecil = teks.lower()#seluruh teks
    kata_kecil = kata.lower()#kata target

    posisi = teks_kecil.find(kata_kecil, start)#mencari posisi kata target di dlm teks dri titik start

    while posisi != -1:
        indeks.append(posisi)#menambahkan indeks posisi
        start = posisi + 1#pencarian bukan lg dimulai dri 0, tpi setelah indeks posisi
        posisi = teks_kecil.find(kata_kecil, start)

    return indeks


def cek_batas_kata(teks, i, panjang): #mengecek kata utuh
    if i > 0: #mengecek karakter di sebelah kiri kata
        sebelum = teks[i - 1].lower() #ambil satu huruf sebelum kata

        if ALFABET.find(sebelum) != -1: #kalau huruf hasilnya false krn bukan kata utuh
            return False

    setelah = i + panjang #menghitung posisi indeks huruf terakhir kata

    if setelah < len(teks): #mengecek karakter di sebelah kanan kata
        karakter_setelah = teks[setelah].lower() #ambil satu huruf setelah kata

        if ALFABET.find(karakter_setelah) != -1:#kalau huruf hasilnya false krn bukan kata utuh
            return False

    return True #selain itu true (kata utuh)


def sensor_kata(teks, kata, simbol): #menyensor kata
    if len(simbol) == 0:
        simbol = "*"

    simbol = simbol[0] #hanya mengambil karakter pertama dari simbol

    indeks_kemunculan = cek_kata(teks, kata)

    hasil = ""
    posisi_sekarang = 0
    jumlah_tersensor = 0
    indeks_awal = []

    for i in indeks_kemunculan: #melakukan perulangan untuk setiap indeks kemunculan kata
        if i >= posisi_sekarang and cek_batas_kata(teks, i, len(kata)):#menyambung teks asli sebelum kata target ke variabel hasil
            hasil = hasil + teks[posisi_sekarang:i]
            hasil = hasil + simbol * len(kata) 

            posisi_sekarang = i + len(kata)
            jumlah_tersensor = jumlah_tersensor + 1
            indeks_awal.append(i)

    hasil = hasil + teks[posisi_sekarang:]

    return hasil, jumlah_tersensor, indeks_awal


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print(f"Hasil Teks: {hasil}")
print(f"Jumlah: {jumlah} | Indeks: {indeks}")