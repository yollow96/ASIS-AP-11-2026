jarak = float(input("masukkan jarak pengiriman (km): "))
layanan_express = str(input("layanan express (ya/tidak): "))


if jarak < 5:
    biaya = 10000
elif jarak >= 5 and jarak <= 20:
    biaya = 20000
else:
    biaya = 35000

biaya_express = 15000 if layanan_express == "ya" else 0

total = biaya + biaya_express
# print(f"Total pengiriman: Rp{total}")
print("total pengiriman: " + str(total))