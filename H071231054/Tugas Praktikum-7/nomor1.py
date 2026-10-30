import os
import datetime
import random

# Setup awal: Membuat folder invoices dan file history jika belum ada
if not os.path.exists("invoices"):
    os.makedirs("invoices")

file_history = "trx_history.txt"
if not os.path.exists(file_history):
    with open(file_history, "w") as f:
        f.write("======================================================================\n")
        f.write(f"| {'Waktu'.center(19)} | {'ID Transaksi'.center(18)} | {'Nominal Transaksi'.center(21)} |\n")
        f.write("======================================================================\n")

def generate_id(nama_kasir, waktu_sekarang):
    # 1. Inisial nama kasir (huruf kapital)
    inisial = "".join([kata[0].upper() for kata in nama_kasir.split()])
    # 2-5. Tahun(2), Bulan(2), Tanggal(2), JamMenit(4)
    waktu_str = waktu_sekarang.strftime("%y%m%d%H%M")
    # 6. Angka acak 100-999
    angka_acak = str(random.randint(100, 999))
    
    return inisial + waktu_str + angka_acak

def buat_transaksi():
    print("\n--- BUAT TRANSAKSI BARU ---")
    nama_kasir = input("Nama Kasir: ")
    
    daftar_produk = []
    total_belanja = 0
    
    while True:
        nama_produk = input("Nama Produk (kosongkan untuk selesai): ")
        if not nama_produk:
            break
        
        try:
            harga = int(input(f"Harga {nama_produk}: Rp"))
            jumlah = int(input(f"Jumlah {nama_produk}: "))
            subtotal = harga * jumlah
            total_belanja += subtotal
            daftar_produk.append({"nama": nama_produk, "harga": harga, "jumlah": jumlah, "subtotal": subtotal})
        except ValueError:
            print("Input harga dan jumlah harus berupa angka!")

    if not daftar_produk:
        print("Transaksi dibatalkan (tidak ada produk).")
        return

    # Generate Waktu & ID
    waktu_sekarang = datetime.datetime.now()
    id_trx = generate_id(nama_kasir, waktu_sekarang)
    
    # Simpan Invoice ke file
    nama_file_invoice = f"invoices/{id_trx}.txt"
    with open(nama_file_invoice, "w") as f:
        f.write("="*40 + "\n")
        f.write("TOKO KITA BERSAMA".center(40) + "\n")
        f.write("="*40 + "\n")
        f.write(f"ID Transaksi : {id_trx}\n")
        f.write(f"Waktu        : {waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Kasir        : {nama_kasir}\n")
        f.write("-" * 40 + "\n")
        for p in daftar_produk:
            f.write(f"{p['nama']:<15} {p['jumlah']:>2} x {p['harga']:<8} = Rp{p['subtotal']:>7}\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'TOTAL':<29} Rp{total_belanja:>7}\n")
        f.write("="*40 + "\n")
    
    # Catat ke trx_history.txt
    waktu_format = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_history, "a") as f:
        f.write(f"| {waktu_format:<19} | {id_trx:<18} | Rp. {total_belanja:<17} |\n")
        f.write("----------------------------------------------------------------------\n")
    
    print(f"\nTransaksi Berhasil! Invoice disimpan sebagai: invoices/{id_trx}.txt")


def cari_invoice():
    print("\n--- CARI INVOICE ---")
    id_trx = input("Masukkan ID Transaksi (tanpa .txt): ")
    path_file = f"invoices/{id_trx}.txt"
    
    if os.path.exists(path_file):
        print("\n" + "="*15 + " ISI INVOICE " + "="*15)
        with open(path_file, "r") as f:
            print(f.read())
    else:
        print(f"Error: Invoice dengan ID '{id_trx}' tidak ditemukan di folder invoices.")


## --- MENU UTAMA ---
while True:
    print("\n=== SISTEM KASIR SEDERHANA ===")
    print("1. Buat Transaksi (Cetak Invoice)")
    print("2. Cari & Tampilkan Invoice")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        buat_transaksi()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("Sistem ditutup. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")