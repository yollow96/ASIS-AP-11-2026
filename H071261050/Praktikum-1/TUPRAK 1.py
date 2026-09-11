#data penjualan
Menu = ["Kopi Susu", "Macha Latte", "Americano"]
Harga = [10000, 22000, 15000]
Jumlah = [4, 3, 5]

#Sub total
Sub_Kopi_Susu = Harga[0] * Jumlah[0]
Sub_Macha_Latte = Harga[1] * Jumlah[1]
Sub_Americano = Harga[2] * Jumlah[2]

Subtotal_pendapatan = [Sub_Kopi_Susu, Sub_Macha_Latte, Sub_Americano]

Biaya_Operasional = 15000
Total_Seluruh = sum(Subtotal_pendapatan) 
Pendapatan_Bersih = Total_Seluruh - Biaya_Operasional

Total_Penjualan = sum(Jumlah) #4 + 3 + 5 = 12
Target_tercapai = Total_Seluruh > 200000 and Total_Penjualan > 10

print("Laporan Penjualan")
print("Subtotal Pendapatan per menu: ", Subtotal_pendapatan)
print("Pendapatan Bersih: Rp", Pendapatan_Bersih)
print("Total Penjualan: ", Total_Penjualan)
print("Target tercapai: ", Target_tercapai)