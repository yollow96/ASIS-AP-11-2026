tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").strip().capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").strip().capitalize()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").strip().capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi" :
            print("Paket rekomendasi: Paket A")
        elif waktu == "Malam" and tipe == "Dewasa" :
            print("Paket rekomendasi: Paket C")
        else :
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa" :
            print("Paket rekomendasi: Paket B")
        elif waktu == "Malam" and tipe == "Dewasa" :
            print("Paket rekomendasi: Paket C")
        else :
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam" :
            print("Paket rekomendasi: Paket C")
        elif waktu == "Malam" and tipe == "Dewasa" :
            print("Paket rekomendasi: Paket C")
        else :
            print("Tidak ada paket yang cocok")
    case _:
        print("Tidak ada paket yang cocok")
