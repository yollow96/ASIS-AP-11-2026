#mengimpor modul bawaan python untuk kebutuhan program
import os #mengelola file dan folder
import random #mengambil angka random dri 100-999
from datetime import datetime #mengambil waktu saat transaksi dilakukan


def buat_invoice(nama_kasir):
    inisial = ""

    for nama in nama_kasir.split():
        inisial += nama[0].upper()

    waktu = datetime.now()
    id_transaksi = (
        inisial
        + waktu.strftime("%y%m%d%H%M")
        + str(random.randint(100, 999))
    )

    daftar_produk = []
    total = 0

    while True:
        print("=" * 69)
        nama_produk = input("Masukkan nama produk    : ")

        if nama_produk == "":
            break

        try:
            harga = int(input("Masukkan harga produk   : "))
            jumlah = int(input("Masukkan jumlah produk  : "))
            if harga < 0 or jumlah < 0:
                print ("Harga dan jumlah harus positif")
                continue
        except ValueError:
            print ("Harga dan jumlah harus angka")

        subtotal = harga * jumlah
        total += subtotal

        daftar_produk.append(
            (nama_produk, harga, jumlah, subtotal)
        )

        print("=" * 69)
        tambah = input("Tambah produk? (y/t)    : ").lower()

        if tambah != "y":
            break

    if len(daftar_produk) == 0:
        print("Transaksi dibatalkan karena tidak ada produk.")
        return

    folder_program = os.path.dirname(os.path.abspath(__file__))
    folder_invoice = os.path.join(folder_program, "invoices")

    if not os.path.exists(folder_invoice):
        os.makedirs(folder_invoice)

    nama_file = os.path.join(
        folder_invoice, id_transaksi + ".txt"
    )

    garis = "=" * 69
    garis_produk = "-" * 69

    isi_invoice = ""
    isi_invoice += garis + "\n"
    isi_invoice += f"TOKO {nama_kasir.upper()}".center(69) + "\n"
    isi_invoice += garis + "\n"
    isi_invoice += f"Nama kasir      : {nama_kasir}\n"
    isi_invoice += (
        f"Waktu transaksi : {waktu.strftime('%d/%m/%y %H:%M')}\n"
    )
    isi_invoice += f"ID transaksi    : {id_transaksi}\n"
    isi_invoice += garis + "\n"
    isi_invoice += "Daftar Produk".center(69) + "\n\n"

    isi_invoice += garis_produk + "\n"
    isi_invoice += (
        f"| {'Nama':<22} | {'Harga':>12} | "
        f"{'Jumlah':>8} | {'Total':>14} |\n"
    )
    isi_invoice += garis_produk + "\n"

    for produk in daftar_produk:
        nama = produk[0][:22]

        isi_invoice += (
            f"| {nama:<22} | "
            f"Rp{produk[1]:>10} | "
            f"{produk[2]:>8} | "
            f"Rp{produk[3]:>12} |\n"
        )

    isi_invoice += garis_produk + "\n"
    isi_invoice += (
        f"| {'TOTAL':<48} | {'Rp' + str(total):>14} |\n"
    )
    isi_invoice += garis + "\n"
    isi_invoice += "TERIMA KASIH TELAH BERBELANJA".center(69) + "\n"
    isi_invoice += garis + "\n"

    with open(nama_file, "w") as file:
        file.write(isi_invoice)

    nama_history = os.path.join(
        folder_program, "trx_history.txt"
    )

    if not os.path.exists(nama_history):
        with open(nama_history, "w") as file:
            file.write("=" * 64 + "\n")
            file.write("RIWAYAT TRANSAKSI".center(64) + "\n")
            file.write("=" * 64 + "\n")
            file.write(
                f"| {'Waktu':<16} | {'ID Transaksi':<18} "
                f"| {'Nominal Transaksi':>20} |\n"
            )
            file.write("=" * 64 + "\n")

    with open(nama_history, "a") as file:
        file.write(
            f"| {waktu.strftime('%d/%m/%y %H:%M'):<16} "
            f"| {id_transaksi:<18} "
            f"| {'Rp' + str(total):>20} |\n"
        )
        file.write("=" * 64 + "\n")

    print("\n" + "=" * 40)
    print("TRANSAKSI BERHASIL".center(40))
    print("=" * 40)
    print("ID transaksi:", id_transaksi)
    print("Total belanja: Rp", total)


def cari_invoice():
    folder_program = os.path.dirname(os.path.abspath(__file__))
    folder_invoice = os.path.join(folder_program, "invoices")

    id_transaksi = input("Masukkan ID transaksi : ")
    nama_file = os.path.join(
        folder_invoice, id_transaksi + ".txt"
    )

    if os.path.exists(nama_file):
        with open(nama_file, "r") as file:
            isi_invoice = file.read()

        print(isi_invoice)
    else:
        print("Transaksi tidak ditemukan.")


def tampilkan_menu():
    print("=" * 40)
    print("SELAMAT DATANG".center(40))
    print("=" * 40)

    nama_kasir = input("Masukkan nama kasir : ")

    while True:
        print("=" * 40)
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * 40)

        pilihan = input("Masukkan opsi pilihan : ")

        if pilihan == "1":
            buat_invoice(nama_kasir)
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            print("Program kasir selesai.")
            break
        else:
            print("Pilihan tidak valid.")


tampilkan_menu()