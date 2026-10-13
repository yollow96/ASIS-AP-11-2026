ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):#ch karakter yg akan dipisah, k jumlah pergeseran huruf
    # Jika huruf kecil
    if ch.lower() in ALFABET:
        posisi = ALFABET.find(ch.lower()) #mencari posisi dlm alfabet
        posisi_baru = (posisi + k) % 26 #menghitung posisi huruf setelah digeser, pergeseran kembali ke aawal
        hasil = ALFABET[posisi_baru]

        # Pertahankan huruf kapital
        if ch.isupper(): #apakah karakter awal merupakan huruf kapital
            return hasil.upper() #hasilnya jadi huruf kapital
        else:
            return hasil

    # Jika bukan huruf, tidak diubah
    return ch


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k): #mengembalikan teks terenkripsi menjadi teks
   
    return mesin_enkripsi(teks, -k) #geser huruf kebelakang


def retas_sandi(sandi, kata_kunci):
    hasil = []

    # Mencoba seluruh 26 kemungkinan kunci
    for k in range(26):
        pesan_asli = mesin_dekripsi(sandi, k)

        # Pencarian tidak membedakan huruf besar/kecil
        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan_asli))

    return hasil


# Program utama
sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi, kata_kunci)

print("Output Deskripsi:", hasil)
            