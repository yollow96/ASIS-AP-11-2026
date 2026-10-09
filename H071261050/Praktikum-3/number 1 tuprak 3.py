print("---Rekapitulasi Transaksi Dins Store---")

jumlah = 1

while jumlah != 0:
    try:
        jumlah = int(input("Masukkan jumlah item: "))
        if jumlah == 0:
            print("Toko ditutup.")
        elif jumlah < 0:
            print("Jumlah tidak boleh negatif!")
        elif jumlah > 100:
            print("Maksimal 100 item per transaksi!")
        else:
            print(f"Transaksi {jumlah} item telah berhasil!!")
    except:
        print("Input harus berupa angka!")