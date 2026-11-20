
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def performa_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def kategori_performa(self):
        if self.performa_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_status(self, no):
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<10} | {self.performa_akhir():<10.2f} | {self.kategori_performa():<14} |")


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))

daftar_pemain = []

for i in range(jumlah_pemain):
    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)

    daftar_pemain.append(pemain)


print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 74)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<14} |")
print("=" * 74)

for i, pemain in enumerate(daftar_pemain, start=1):
    pemain.tampilkan_status(i)

print("=" * 74)
