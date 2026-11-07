
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor_akhir = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor_akhir

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        print(f"| {nomor:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<10} | {self.hitung_skor_akhir():<10.2f} | {self.status_performa():<15} |")


daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))

for i in range(jumlah_pemain):
    print(f"\n-- Data Pemain ke-{i + 1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)


print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 78)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
print("=" * 78)

for i in range(len(daftar_pemain)):
    daftar_pemain[i].tampilkan_data(i + 1)

print("=" * 78)