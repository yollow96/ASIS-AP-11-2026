from datetime import datetime
import random
import os

FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "trx_history.txt" 
LEBAR_TERMINAL = 60 
LEBAR_STRUK = 70 

def buat_folder():
    os.makedirs(FOLDER_INVOICE, exist_ok=True) #membuat folder invoces

def tanya(label):
    return input(label.ljust(25) + ": ") #ljust artinya left justify (rata kiri) barudisambung dengan ": "
 

def buat_id_transaksi(nama_kasir, waktu_sekarang):
    waktu_sekarang = datetime.now()
    inisial = "".join(kata[0] for kata in nama_kasir.split()).upper()
    tanggal_jam = waktu_sekarang.strftime("%y%m%d%H%M") #dua digit terakhir
    angka_acak = random.randint(100, 999)
    id_transaksi = f"{inisial}{tanggal_jam}{angka_acak}"
    return id_transaksi

def inputan_produk():
    daftar_produk = []
    while True:    
        nama_produk = tanya("Masukkan nama produk: ")
        if nama_produk.strip() == "": 
            print("Nama produk tidak boleh kosong.")
            continue
        try:
            harga_produk = int(tanya("Masukkan harga produk: "))  
            jumlah_produk = int(tanya("Masukkan jumlah produk: ")) 
            if harga_produk < 0 or jumlah_produk <= 0:
                print("Harga dan Jumlah produk harus positif.") 
                continue                  
        except ValueError:
            print("Harga dan Jumlah harus berupa angka.")
            continue
        daftar_produk.append([nama_produk, harga_produk, jumlah_produk])
        print("=" * LEBAR_TERMINAL)
        tambah = tanya("Tambah produk? (y/t): ").lower()
        print("=" * LEBAR_TERMINAL)
        if tambah == "t":
            print("TRANSAKSI BERHASIL".center(LEBAR_TERMINAL))
            print("=" * LEBAR_TERMINAL)
            break
            
    return daftar_produk

def total_harga(daftar_produk):
    total_akhir = 0
    for nama, harga, jumlah in daftar_produk:
        total_akhir = total_akhir + (harga * jumlah)
    return total_akhir

def simpan_struk(nama_kasir, daftar_produk, total, id_tranksaksi, waktu):
    nama_file = os.path.join(FOLDER_INVOICE, f"{id_tranksaksi}.txt") #menyusun alamat file ke folder invoices
    garis = "=" * LEBAR_STRUK
    garis_tabel = " " * 5 + "=" * LEBAR_TERMINAL
    nama_toko = nama_kasir.upper()

    with open(nama_file, "w") as file:
        file.write("\n")
        file.write(f"TOKO {nama_toko}".center(LEBAR_STRUK) + "\n")
        file.write("\n")
        file.write(garis + "\n")
        file.write(f"{'Nama kasir':<20}: {nama_kasir}\n")
        file.write(f"{'Waktu transaksi':<20}: {waktu.strftime('%d/%m/%y %H:%M')}\n")
        file.write(garis + "\n")
        file.write("\n")
        file.write("Daftar Produk".center(LEBAR_STRUK) + "\n")
        file.write("\n")

        file.write(garis_tabel + "\n")
        file.write(" " * 5 + "|" + "Nama".center(20) + "|" + "Harga".center(12)
                   + "|" + "Jumlah".center(8) + "|" + "Total".center(15) + "|\n") # angka = lebarnya
        file.write(garis_tabel + "\n")
 
        for nama, harga, jumlah in daftar_produk:
            subtotal = harga * jumlah
 
            if len(nama) > 18:
                nama = nama[:15] + "..." #ambil sampe karakter ke 15
 
            file.write(" " * 5 + "|" + f" {nama:<18} " + "|" + f" {'Rp' + str(harga):>10} "
                       + "|" + f" {jumlah:<6} " + "|" + f" {'Rp' + str(subtotal):>13} " + "|\n")
 
        file.write(garis_tabel + "\n")
        file.write(" " * 5 + "|" + "TOTAL".center(20) + " " * 22 + "|"
                   + f" {'Rp' + str(total):>13} " + "|\n") #str biar bisa di +
        file.write(garis_tabel + "\n")
        file.write("\n")
        file.write(garis + "\n")
        file.write("TERIMA KASIH TELAH BERBELANJA".center(LEBAR_STRUK) + "\n")
        file.write(garis + "\n")

        file.write(f"TOTAL: Rp{total}\n")

def cari_transaksi():
    id_transaksi = tanya("Masukkan ID transaksi: ").strip().upper()

    nama_file = os.path.join(FOLDER_INVOICE, f"{id_transaksi}.txt")

    try:
        with open(nama_file, "r") as file:
            isi_struk = file.read()
            print("_" * LEBAR_STRUK)
            print(isi_struk)
            print("_" * LEBAR_STRUK)

    except FileNotFoundError:
        print("Transaksi tidak ditemukan!")
        print("_" * LEBAR_TERMINAL)

def simpan_riwayat(waktu, id_transaksi, total):
    garis = "_" * LEBAR_STRUK

    if not os.path.exists(FILE_RIWAYAT): #membuat header, kalo udah ada, skip
        with open(FILE_RIWAYAT, "w") as file:
            file.write(garis + "\n")
            file.write("|" + "RIWAYAT TRANSAKSI".center(68) + "|\n")
            file.write(garis + "\n")
            file.write("|" + "Waktu".center(17) + "|" + "ID Transaksi".center(24)
                    + "|" + "Nominal Transaksi".center(25) + "|\n")
            file.write(garis + "\n")
 
    with open(FILE_RIWAYAT, "a") as file:
        file.write("|" + f" {waktu.strftime('%d/%m/%y %H:%M'):<15} " + "|"
                   + f" {id_transaksi:<22} " + "|" + f" {'Rp' + str(total):>23} " + "|\n")
        file.write(garis + "\n")
 
 
buat_folder()


print("=" * LEBAR_TERMINAL)
print("SELAMAT DATANG".center(LEBAR_TERMINAL))
print("=" * LEBAR_TERMINAL)
nama_kasir = tanya("Masukkan nama kasir: ")
print("=" * LEBAR_TERMINAL)

while True:
    print("pilih opsi: ")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * LEBAR_TERMINAL)
    try:
        opsi = int(input("Masukkan opsi pilihan: ")) 
    except ValueError:
        print("Opsi harus berupa angka.")
        continue
    print("=" * LEBAR_TERMINAL)  


    if opsi == 1:
        daftar_produk = inputan_produk()
        total = total_harga(daftar_produk)
        waktu = datetime.now()
        id_transaksi = buat_id_transaksi(nama_kasir, waktu)
        simpan_struk(nama_kasir, daftar_produk, total, id_transaksi, waktu)
        simpan_riwayat(waktu, id_transaksi, total)

    if opsi == 2:
        cari_transaksi()

    if opsi == 3:
        print("SAMPAI JUMPA".center(LEBAR_TERMINAL))
        print("=" * LEBAR_TERMINAL)
        break
 
