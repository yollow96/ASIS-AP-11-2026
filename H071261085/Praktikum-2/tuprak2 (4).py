# rekomendasi paket wisata
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").strip().capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").strip().capitalize()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").strip().capitalize()

paket = "Tidak ada paket yang cocok"

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "Paket A"
        elif waktu == "Malam" and tipe == "Dewasa":
            paket = "Paket C"
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            paket = "Paket B"
        elif waktu == "Malam" and tipe == "Dewasa":
            paket = "Paket C"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"

print(f"Paket Rekomendasi: {paket}")