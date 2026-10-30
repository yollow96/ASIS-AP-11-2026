# while True:
#     karakter = input("Karakter :")

#     if karakter >= "A" and karakter <= "Z":
#         print("Huruf kapital?", True)
        
#     else:
#         print("Huruf kapital?", False)
        
#     if karakter >= "a" and karakter <= "z":
#         print("Huruf kecil?", True)
#     else:
#         print("Huruf kecil?", False)

#     if karakter >= "0" and karakter <= "9":
#         print("Angka ?:", True)
#     else:
#         print("Angka ?:", False)
#     continue

# class Mahasiswa:
#     def __init__(self,nama,nilai):
#         self.nama = nama
#         self.nilai = nilai

#     def hitung_rata_rata(self):
#         return sum(self.nilai) / len(self.nilai)
# andi = Mahasiswa("andi", [80, 90, 70])
# mathahir = Mahasiswa ("nama=mathahir", [100, 100, 100])

# print(andi.hitung_rata_rata())
# print(mathahir.hitung_rata_rata())

# # define a class
# class Bike:
#     name = ""
#     gear = 0

# # create object of class
# bike1 = Bike()

# # access attributes and assign new values
# bike1.gear = 11
# bike1.name = "Mountain Bike"

# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

# define a class
# class Employee:
#     # define a property
#     employee_id = 0

# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()

# # access property using employee1
# employee1.employeeID = 1001
# print(f"Employee ID: {employee1.employeeID}")

# # access properties using employee2
# employee2.employeeID = 1002
# print(f"Employee ID: {employee2.employeeID}")

# class PersegiPanjang:
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar = lebar
#     def luas(self):
#         return self.panjang * self.lebar
# luas_a = PersegiPanjang(4, 3)
# print(luas_a.luas())

# class Mahasiswa:
#     def __init__(self, nim, nama, uts, uas) :
#         self.nim = nim
#         self.nama = nama
#         self.daftar_tugas = []
#         self.uts = self.validasi(uts)
#         self.uas = uas
#     def rata_rata(self):
#         return 

# class Mahasiswa:
#     def _init_(self, nim, nama, uts, uas):
#         self.nim = nim
#         self.nama = nama
#         self.daftar_tugas = []
#         self.uts = self.validasi_nilai(uts)
#         self.uas = self.validasi_nilai(uas)

#     def validasi_nilai(self, nilai):
#         if not 0 <= nilai <= 100:
#             raise ValueError("Nilai harus antara 0 sampai 100")
#         return nilai

#     def tambah_tugas(self, nilai):
#         nilai = self.validasi_nilai(nilai)
#         self.daftar_tugas.append(nilai)

#     def rata_rata_tugas(self):
#         if len(self.daftar_tugas) == 0:
#             return 0

#         return sum(self.daftar_tugas) / len(self.daftar_tugas)

#     def nilai_akhir(self):
#         rata_tugas = self.rata_rata_tugas()

#         akhir = (
#             0.30 * rata_tugas
#             + 0.30 * self.uts
#             + 0.40 * self.uas
#         )

#         return akhir

#     def status(self):
#         if self.nilai_akhir() >= 60:
#             return "Lulus"
#         else:
#             return "Tidak Lulus"


# # Program utama
# nim = input("Masukkan NIM: ")
# nama = input("Masukkan Nama: ")

# jumlah_tugas = int(input("Jumlah tugas: "))

# mahasiswa = Mahasiswa(
#     nim, nama,
#     float(input("Nilai UTS: ")),
#     float(input("Nilai UAS: "))
# )

# for i in range(jumlah_tugas):
#     nilai = float(input(f"Nilai tugas ke-{i+1}: "))
#     mahasiswa.tambah_tugas(nilai)

# print("\n===== HASIL NILAI MAHASISWA =====")
# print("NIM:", mahasiswa.nim)
# print("Nama:", mahasiswa.nama)
# print("Daftar Tugas:", mahasiswa.daftar_tugas)
# print("Rata-rata Tugas:", mahasiswa.rata_rata_tugas())
# print("Nilai UTS:", mahasiswa.uts)
# print("Nilai UAS:", mahasiswa.uas)
# print("Nilai Akhir:", mahasiswa.nilai_akhir())
# print("Status:", mahasiswa.status())

# class Rekening:
#     def __init__(self, nomor, pemilik, saldo):
#         self.nomor = nomor
#         self.pemilik = pemilik
#         self.saldo = saldo

#     def transfer(self, tujuan, jumlah):
#         if jumlah <= 0:
#             return False

#         if tujuan is self:
#             return False

#         if jumlah > self.saldo:
#             return False

#         self.saldo -= jumlah
#         tujuan.saldo += jumlah
#         return True


# r1 = Rekening("001", "Ayu", 500_000)
# r2 = Rekening("002", "Bima", 100_000)

# r1.transfer(r1, 600_000)

# print(r1.saldo)  
# print(r2.saldo)  

# import re
# pattern = "[a-e]"
# test = "abdjgde"

# result = re.match(pattern, test)
# if result:
#     print("sukses")
# else:
#     print("tidak sukses")

# import re
# string = "hello 1234 adel 19"
# pattern = "\s"
# replace = "19"
# result = re.sub(pattern, replace, string)
# print(result)

import re 
string = ' Hello 1234 \ Welcome 4523 \n Kaito 1412' 
pattern = '\A' 
replace = "19"  
result = re.sub(pattern, replace, string) 
print(result) 