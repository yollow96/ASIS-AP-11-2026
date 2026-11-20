
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.__judul = ""
        self.__penulis = ""
        self.__tahun_terbit = 1450

        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun

    # Getter dan setter judul
    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, nilai):
        if not nilai or not nilai.strip():
            print("Judul tidak boleh kosong!")
            return
        self.__judul = nilai

    # Getter dan setter penulis
    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, nilai):
        if not nilai or not nilai.strip():
            print("Penulis tidak boleh kosong!")
            return
        self.__penulis = nilai

    # Getter dan setter tahun terbit
    @property
    def tahun_terbit(self):
        return self.__tahun_terbit

    @tahun_terbit.setter
    def tahun_terbit(self, nilai):
        if not isinstance(nilai, int) or nilai < 1450 or nilai > 2026:
            print("Tahun terbit harus 1450-2026!")
            return
        self.__tahun_terbit = nilai

    def tampilkan_data(self):
        print(f"Judul  : {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun  : {self.tahun_terbit}")


# Membuat dua objek Buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = Buku("Bumi", "Tere Liye", 2014)

# Mencoba mengubah tahun terbit
print("=== UJI VALIDASI BUKU ===")
buku1.tahun_terbit = 3000

# Menampilkan data
print("\n=== DATA BUKU 1 ===")
buku1.tampilkan_data()

print("\n=== DATA BUKU 2 ===")
buku2.tampilkan_data()
