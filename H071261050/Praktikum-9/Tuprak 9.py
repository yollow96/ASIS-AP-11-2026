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

    def tampilkan_data(self, no):
        print(
            f"| {no:<2} "
            f"| {self.nama:<10} "
            f"| {self.id_pemain:<10} "
            f"| {self.role:<9} "
            f"| {self.hitung_skor_akhir():<10.2f} "
            f"| {self.status_performa():<14} |"
        )


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

daftar_pemain = []

while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        break
    except ValueError:
        print("Jumlah pemain harus berupa angka bulat.")

for x in range(jumlah_pemain):
    print(f"\n-- Data Pemain ke-{x + 1} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")

    while True:
        try:
            nilai_kill = float(input("Nilai Kill: "))
            nilai_assist = float(input("Nilai Assist: "))
            nilai_objective = float(input("Nilai Objective: "))
            break
        except ValueError:
            print("Input harus berupa angka untuk nilai.")

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

garis = "=" * 74
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<14} |")
print(garis)
for nomor, pemain in enumerate(daftar_pemain, start=1):
    pemain.tampilkan_data(nomor)
print(garis)