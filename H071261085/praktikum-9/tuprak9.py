# Class Pemain untuk merepresentasikan entitas pemain
class Pemain:
    # Konstruktor __init__ untuk menginisialisasi atribut pemain
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    # Method untuk menghitung skor akhir berdasarkan bobot penilaian
    def hitung_skor_akhir(self):
        skor = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor

    # Method untuk menentukan status performa pemain
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    # Method untuk menampilkan baris data pemain dalam format tabel ber-f-string
    def tampilkan_data(self, no):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"{no:<4} | {self.nama:<12} | {self.id_pemain:<12} | {self.role:<10} | {skor_akhir:<10.2f} | {status}")


# Fungsi utama program
def main():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    
    # Meminta input jumlah pemain yang akan dimasukkan
    jumlah_pemain = int(input("Masukkan jumlah pemain: "))
    print()

    # List untuk menyimpan seluruh objek Pemain
    daftar_pemain = []

    # Perulangan untuk menginputkan data setiap pemain
    for i in range(jumlah_pemain):
        print(f"Data Pemain ke-{i + 1}")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        kill = float(input("Kill: "))
        assist = float(input("Assist: "))
        objective = float(input("Objective: "))
        print()

        # Membuat objek baru dari class Pemain
        pemain_baru = Pemain(nama, id_pemain, role, kill, assist, objective)
        
        # Menambahkan objek ke dalam list
        daftar_pemain.append(pemain_baru)

    # Menampilkan rekapitulasi data pemain dalam bentuk tabel
    print("=" * 75)
    print(f"{'REKAPITULASI PERFORMA PEMAIN':^75}")
    print("=" * 75)
    print(f"{'No':<4} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | {'Status'}")
    print("-" * 75)

    # Memanggil method tampilkan_data() untuk setiap objek dalam list
    for index, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(index)

    print("-" * 75)

# Menjalankan program utama
if __name__ == "__main__":
    main()