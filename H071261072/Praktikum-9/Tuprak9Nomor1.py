
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        print(f"{self.nama:<15} {self.id_pemain:<12} {self.role:<15} {self.nilai_kill:<10} {self.nilai_assist:<10} {self.nilai_objective:<12} {self.hitung_skor_akhir():<12.2f} {self.status_performa()}")


daftar_pemain = []

print("=== SISTEM PENGELOLAAN DATA PEMAIN ===")

while True:
    nama = input("\nMasukkan nama pemain: ")
    id_pemain = input("Masukkan ID pemain: ")
    role = input("Masukkan role pemain: ")

    while True:
        try:
            nilai_kill = float(input("Masukkan nilai Kill: "))
            nilai_assist = float(input("Masukkan nilai Assist: "))
            nilai_objective = float(input("Masukkan nilai Objective: "))

            if nilai_kill < 0 or nilai_assist < 0 or nilai_objective < 0:
                print("Nilai tidak boleh negatif!")
                continue

            break
        except ValueError:
            print("Input harus berupa angka!")

    pemain_baru = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)

    daftar_pemain.append(pemain_baru)

    pilihan = input("\nApakah ingin menambahkan pemain lagi? (ya/tidak): ").lower()

    if pilihan != "ya":
        break

print("\n" + "=" * 115)
print("DAFTAR PERFORMA PEMAIN")
print("=" * 115)

print(f"{'Nama':<15} {'ID Pemain':<12} {'Role':<15} {'Kill':<10} {'Assist':<10} {'Objective':<12} {'Skor Akhir':<12} {'Status'}")
print("-" * 115)

for pemain in daftar_pemain:
    pemain.tampilkan_data()

print("=" * 115)
print(f"Total pemain: {len(daftar_pemain)}")
