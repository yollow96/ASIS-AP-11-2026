import os
import random
from datetime import datetime


# MEMBUAT ID TRANSAKSI
def buat_id_transaksi(nama_kasir):
    inisial = "".join(#menggabungkan tanpa spasi
        kata[0].upper() for kata in nama_kasir.split()
    )

    waktu = datetime.now()

    tahun = waktu.strftime("%y")
    bulan = waktu.strftime("%m")
    tanggal = waktu.strftime("%d")
    jam_menit = waktu.strftime("%H%M")

    angka_acak = random.randint(100, 999)

    id_transaksi = (
        inisial + tahun + bulan + tanggal
        + jam_menit + str(angka_acak)
    )

    return id_transaksi


# MEMBUAT INVOICE
def buat_invoice(nama_kasir, daftar_produk, id_transaksi):
    total = sum(
        produk["harga"] * produk["jumlah"]
        for produk in daftar_produk
    )

    os.makedirs("invoices", exist_ok=True)

    nama_file = id_transaksi + ".txt"
    lokasi_file = os.path.join("invoices", nama_file)#menggabungkan nama folder dan nama file menjadi satu lokasi.

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write("========== INVOICE BELANJA ==========\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(f"Nama Kasir   : {nama_kasir}\n")
        file.write(
            f"Waktu        : {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
        )
        file.write("=====================================\n")

        for nomor, produk in enumerate(daftar_produk, start=1):
            subtotal = produk["harga"] * produk["jumlah"]

            file.write(f"\nProduk {nomor}\n")
            file.write(f"Nama Produk : {produk['nama']}\n")
            file.write(f"Harga       : Rp{produk['harga']:,}\n")
            file.write(f"Jumlah      : {produk['jumlah']}\n")
            file.write(f"Subtotal    : Rp{subtotal:,}\n")

        file.write("\n=====================================\n")
        file.write(f"TOTAL BELANJA : Rp{total:,}\n")
        file.write("=====================================\n")

    print("\nTransaksi berhasil!")
    print(f"ID Transaksi  : {id_transaksi}")
    print(f"Total Belanja : Rp{total:,}")
    print(f"Invoice tersimpan di: {lokasi_file}")

    return total


# MENCATAT RIWAYAT TRANSAKSI
def simpan_riwayat(id_transaksi, total):
    nama_file = "trx_history.txt"
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    file_baru = not os.path.exists(nama_file)#mengambil alamat file

    with open(nama_file, "a", encoding="utf-8") as file:
        if file_baru:
            file.write(
                f"{'Waktu':<22} | {'ID Transaksi':<25} | {'Nominal Transaksi':>18}\n"
            )
            file.write("-" * 75 + "\n")

        file.write(
            f"{waktu:<22} | {id_transaksi:<25} | Rp{total:>15,}\n"
        )


# MENCARI DAN MENAMPILKAN INVOICE
def cari_invoice():
    id_transaksi = input("\nMasukkan ID transaksi: ").strip()

    nama_file = id_transaksi + ".txt"
    lokasi_file = os.path.join("invoices", nama_file)

    if os.path.exists(lokasi_file):
        print("\n========== HASIL PENCARIAN ==========\n")

        with open(lokasi_file, "r", encoding="utf-8") as file:
            isi_invoice = file.read()
            print(isi_invoice)

    else:
        print("\nInvoice tidak ditemukan!")


# MEMBUAT TRANSAKSI BARU
def transaksi_baru():
    print("\n========== TRANSAKSI BARU ==========")

    nama_kasir = input("Nama kasir: ").strip()

    if not nama_kasir:
        print("Nama kasir tidak boleh kosong!")
        return

    try:
        jumlah_produk = int(
            input("Jumlah jenis produk yang dibeli: ")
        )

        if jumlah_produk <= 0:
            print("Jumlah produk harus lebih dari 0!")
            return

        daftar_produk = []

        for i in range(jumlah_produk):
            print(f"\nProduk ke-{i + 1}")

            nama = input("Nama produk: ").strip()

            harga = int(input("Harga produk: "))
            jumlah = int(input("Jumlah produk yang dibeli: "))

            if not nama or harga < 0 or jumlah <= 0:
                print("Data produk tidak valid!")
                return

            produk = {
                "nama": nama,
                "harga": harga,
                "jumlah": jumlah
            }

            daftar_produk.append(produk)

        id_transaksi = buat_id_transaksi(nama_kasir)

        total = buat_invoice(
            nama_kasir, daftar_produk, id_transaksi
        )

        simpan_riwayat(id_transaksi, total)

    except ValueError:
        print("Input harus berupa angka yang valid!")


# MELIHAT RIWAYAT TRANSAKSI
def tampilkan_riwayat():
    nama_file = "trx_history.txt"

    if os.path.exists(nama_file):
        print("\n========== RIWAYAT TRANSAKSI ==========\n")

        with open(nama_file, "r", encoding="utf-8") as file:
            print(file.read())

    else:
        print("\nBelum ada riwayat transaksi.")


# MENU UTAMA
def main():
    while True:
        print("\n========== PROGRAM KASIR ==========")
        print("1. Transaksi Baru")
        print("2. Cari Invoice")
        print("3. Riwayat Transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            transaksi_baru()

        elif pilihan == "2":
            cari_invoice()

        elif pilihan == "3":
            tampilkan_riwayat()

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program kasir!")
            break

        else:
            print("\nPilihan tidak valid! Silakan pilih 1-4.")


if __name__ == "__main__":
    main()
