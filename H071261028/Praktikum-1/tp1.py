menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [10000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi_susu, sub_matcha_latte, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print("===== Laporan Penjualan Kopi Senja =====")
print("subtotal kopi susu:", sub_kopi_susu)
print("subtotal matcha latte:", sub_matcha_latte)
print("subtotal americano:", sub_americano)
print("subtotal pendapatan:", total_seluruh)
print("jumlah barang:", jumlah_barang)
print("pendapatan bersih:", pendapatan_bersih)
print("target tercapai:", target_tercapai) 

