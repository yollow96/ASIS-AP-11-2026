# Data
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# Subtotal masing-masing menu
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# Masukkan ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# Total seluruh dan pendapatan bersih
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# Jumlah barang terjual & target tercapai
jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

# Tampilkan hasil
print("=== Laporan Penjualan Kopi Senja ===")
print(f"Subtotal Kopi Susu    : Rp{sub_kopi}")
print(f"Subtotal Matcha Latte : Rp{sub_matcha}")
print(f"Subtotal Americano    : Rp{sub_americano}")
print(f"Total Pendapatan      : Rp{total_seluruh}")
print(f"Biaya Operasional     : Rp{BIAYA_OPERASIONAL}")
print(f"Pendapatan Bersih     : Rp{pendapatan_bersih}")
print(f"Jumlah Barang Terjual : {jumlah_barang}")
print(f"Target Tercapai       : {target_tercapai}")