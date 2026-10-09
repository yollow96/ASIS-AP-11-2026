
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# nomor 1
sub_kopi = harga[0] * jumlah[0] 
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah [2]

# nomor 2
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# nomor 3
BIAYA_OPERASIONAL = 15000
total_seluruh = subtotal_pendapatan[0] + subtotal_pendapatan[1] + subtotal_pendapatan[2]
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# nomor 4
total_barang = jumlah [0] + jumlah[1] + jumlah[2]
target_tercapai = 0
total_pendapatan = total_seluruh
jumlah_barang = total_barang

if total_pendapatan > 200000 and jumlah_barang > 10:
    target_tercapai = True
else:
    target_tercapai = False
    

print(subtotal_pendapatan)
print(pendapatan_bersih)
print(target_tercapai)   




