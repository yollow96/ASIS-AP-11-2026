def cek_kata(teks, kata):
    indeks = []
    start = 0

    teks_kecil = teks.lower() #tdk dibedakan dgn huruf kapital
    kata_kecil = kata.lower()

    while True:
        posisi = teks_kecil.find(kata_kecil, start) #mencari posisi dalam teks

        if posisi == -1: # tdk ditemukan
            break 

        indeks.append(posisi)
        start = posisi + 1 #pencarian berikutnya dimulai dari

    return indeks


def cek_batas_kata(teks, i, panjang): #cek apkah kata utuh
    # Cek karakter sebelum kata
    if i == 0:
        batas_kiri = True
    else:
        karakter_kiri = teks[i - 1].lower() #jika tdk ada d awal teks, program mengambil karakter sblum kata tersebut, indeks sebelumnya

        if 'a' <= karakter_kiri <= 'z':
            batas_kiri = False
        else:
            batas_kiri = True #kata yg merupakan bagian dari kata lain tdk dianggap kata utuh

    # Cek karakter sesudah kata
    posisi_akhir = i + panjang #menghitung posisi tepat setelah kata target

    if posisi_akhir == len(teks):
        batas_kanan = True
    else:
        karakter_kanan = teks[posisi_akhir].lower()#jika tdk berakhir di ujung teks, program mengambil karakter setelah kata trsbut

        if 'a' <= karakter_kanan <= 'z':
            batas_kanan = False
        else:
            batas_kanan = True

    return batas_kiri and batas_kanan


def sensor_kata(teks, kata, simbol):
    panjang = len(kata) #menghitung panjang kata
    semua_indeks = cek_kata(teks, kata) #mencari semua posisi kata target

    hasil = "" #menampung teks akhir setelah disensor
    indeks_awal = [] #posisi awal kata yang di sensor
    posisi_sekarang = 0
    jumlah = 0 #jumlah kata yg berhasil disensor, awalnnya nol

    for i in semua_indeks: #mengambil setiap indeks dalam variabael satu per satu
        if i >= posisi_sekarang and cek_batas_kata(teks, i, panjang): #posisi kata blm dilewati, kata merupakan kata utuh, jika keduanya bnr kata disensor
            # Ambil bagian teks sebelum kata target
            hasil += teks[posisi_sekarang:i] #meanmbahkan teks sebelum kata target dlmm hasil

            # Membuat simbol sebanyak panjang kata
            sensor = "" #menampung simbol pengganti

            for j in range(panjang): #mengulang penambahan simbol sebanyak panjang kata target
                sensor += simbol

            hasil += sensor

            # Catat indeks asli
            indeks_awal.append(i) #mencatat indeks awal kata yg berhasil disensor dlm list
            jumlah += 1

            # Pindah melewati kata yang sudah disensor
            posisi_sekarang = i + panjang #memindahkan posisi pemrosesan ke karakter setelah kata yang disensor

    # Tambahkan sisa teks setelah proses penyensoran
    hasil += teks[posisi_sekarang:] #menambahkan sisa teks yg blm diproses kedalam list

    return hasil, jumlah, indeks_awal


# Program utama
teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)