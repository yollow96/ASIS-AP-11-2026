# 1. Input data
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe_pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

paket = 0

match tujuan:
    case "pantai":
        if waktu == "pagi":
            paket = "Paket A"
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"

    case "pegunungan":
        if waktu == "pagi" and tipe_pengunjung == "dewasa":
            paket = "Paket B"
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"

    case "kota":
        if waktu == "malam":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"

    case _:
        paket = "Tidak ada paket yang cocok"


if paket == "Tidak ada paket yang cocok":
    print(paket)
else:
    print("Paket Rekomendasi:" + str (paket))