import os  
import datetime
import random

def buat_id_transaksi(nama_kasir):
    inisial = nama_kasir.replace(" ", "")[:3].upper().ljust(3, 'X')
    
    # Mengambil waktu saat ini
    sekarang = datetime.datetime.now()
    tahun = sekarang.strftime("%y")
    bulan = sekarang.strftime("%m")
    tanggal = sekarang.strftime("%d")
    waktu = sekarang.strftime("%H%M")
    
    angka_acak = str(random.randint(100, 999))
    
    id_transaksi = f"{inisial}{tahun}{bulan}{tanggal}{waktu}{angka_acak}"
    return id_transaksi

def catat_riwayat(waktu, id_transaksi, total_nominal):
    nama_file = "trx_history.txt"
    file_baru = not os.path.exists(nama_file)  
    
    with open(nama_file, "a") as file:
        if file_baru:
            file.write("=" * 66 + "\n")
            file.write(f"| {'Waktu':^19} | {'ID Transaksi':^16} | {'Nominal Transaksi':^19} |\n")
            file.write("=" * 66 + "\n")
        
        file.write(f"| {waktu:<19} | {id_transaksi:<16} | Rp. {total_nominal:<15} |\n")
        file.write("=" * 66 + "\n")

def menu_tambah_transaksi():
    print("\n--- TAMBAH TRANSAKSI ---")
    nama_kasir = input("Masukkan nama kasir: ")
    
    keranjang = []
    total_nominal = 0
    
    while True:
        nama_produk = input("Nama produk: ")
        harga_produk = int(input("Harga produk: "))
        jumlah_produk = int(input("Jumlah produk: "))
        
        total_harga_produk = harga_produk * jumlah_produk
        keranjang.append({
            "nama": nama_produk,
            "harga": harga_produk,
            "jumlah": jumlah_produk,
            "total": total_harga_produk
        })
        
        total_nominal += total_harga_produk
        
        lanjut = input("Tambah produk lain? (y/n): ")
        if lanjut.lower() != 'y':
            break

    if not os.path.exists("invoices"):  
        os.makedirs("invoices") 
        
    id_transaksi = buat_id_transaksi(nama_kasir)
    waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    path_invoice = os.path.join("invoices", f"{id_transaksi}.txt")
    with open(path_invoice, "w") as file:
        file.write("=" * 40 + "\n")
        file.write("INVOICE TRANSAKSI\n")
        file.write("=" * 40 + "\n")
        file.write(f"Waktu        : {waktu_sekarang}\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(f"Kasir        : {nama_kasir}\n")
        file.write("-" * 40 + "\n")
        for item in keranjang:
            file.write(f"{item['nama']} (x{item['jumlah']})\n")
            file.write(f"Rp{item['harga']} -> Rp{item['total']}\n")
        file.write("-" * 40 + "\n")
        file.write(f"TOTAL        : Rp{total_nominal}\n")
        file.write("=" * 40 + "\n")
        
    print(f"\n✅ Transaksi berhasil! Invoice disimpan sebagai {id_transaksi}.txt")
    
    catat_riwayat(waktu_sekarang, id_transaksi, total_nominal)

def menu_cari_invoice():
    print("\n--- CARI INVOICE ---")
    id_pencarian = input("Masukkan ID Transaksi: ")
    
    path_invoice = os.path.join("invoices", f"{id_pencarian}.txt") 
    
    if os.path.exists(path_invoice):  
        print(f"\n[ Menampilkan isi file {id_pencarian}.txt ]\n")
        with open(path_invoice, "r") as file:
            print(file.read())
    else:
        print(f"\n❌ Gagal: Invoice dengan ID '{id_pencarian}' tidak ditemukan di folder 'invoices'.")

def main():
    while True:
        print("\n" + "=" * 30)
        print("   APLIKASI KASIR SEDERHANA")
        print("=" * 30)
        print("1. Tambah Transaksi")
        print("2. Cari Invoice")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            menu_tambah_transaksi()
        elif pilihan == '2':
            menu_cari_invoice()
        elif pilihan == '3':
            print("Menutup aplikasi kasir. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()