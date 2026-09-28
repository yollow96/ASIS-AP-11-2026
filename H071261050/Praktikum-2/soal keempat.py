Tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").strip().capitalize()
Waktu = input("Masukkan waktu pengiriman (pagi/malam): ").strip().capitalize()
Pengunjung = input("Masukkan tipe pengunjung (Anak/dewasa): ").strip().capitalize()

match Tujuan:
    case "Pantai":
        if Waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif Waktu == "Malam" and Pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if Waktu == "Pagi" and Pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif Waktu == "Malam" and Pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if Waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tujuan ada paket yang cocok")
