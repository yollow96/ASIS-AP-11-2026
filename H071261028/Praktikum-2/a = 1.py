# a = 1
# b = "Zero"
# x = a + 3
# print(x)

# a = 5 + 5 * 2
# print(a)

# nama_barang = input("nama barang :")
# harga_barang = int(input("Masukkan harga barang :"))
# jumlah_barang = int(input("Masukkan jumlah barang :"))

# subtotal = harga_barang * jumlah_barang
# if subtotal >= 100000:
#     diskon = subtotal * 10 // 100
# else:
#     diskon = 0
# total = subtotal - diskon

# print("Nama barang :", nama_barang)
# print("subtotal :", subtotal)
# print("Total  pembayaran :", total)

# def luas_tabung (jari_jari, tinggi):
#     PHI = 3.14
#     return 2 * PHI * jari_jari * (jari_jari + tinggi)


# def luas_segitiga(alas, tinggi):
#     # Tulis kodemu di sini
#     return 1 / 2 * alas * tinggi

# def bilangan_genap(angka):
#     # Tulis kodemu di sini
#     return angka >= 0

# def harga_diskon(harga):
#     # Tulis kodemu di sini
#     harga_akhir = harga - (harga * 20 / 100)
#     return harga_akhir

# def bilangan_terbesar(a, b):
#     # Tulis kodemu di sini
#     if a >= b:
#         return a
#     else:
#         return b

# def jumlah_bilangan(n):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for i in range (1, n + 1):
#         jumlah = jumlah + 1
#         return jumlah

# def jumlah_genap(n):
#     # Tulis kodemu di sini
#     jumlah = 0
    
#     for i in range (2, n+1, 2):
#         jumlah = jumlah + i
#     return jumlah

# def hitung_positif(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for i in daftar:
#         if i > 0:
#             jumlah = jumlah + 1
#     return jumlah

# def hitung_negatif(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for i in daftar:
#         if i < 0:
#             jumlah = jumlah + 1
#     return jumlah

# def jumlah_list(daftar):
#     # Tulis kodemu sini
#     jumlah = 0
#     for i in daftar:
#         jumlah = jumlah + i
#     return jumlah

# def jumlah_ganjil(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for i in daftar:
#         if i % 2 != 0:
#             jumlah = jumlah + i
#     return jumlah

# def hitung_vokal(teks):
#     # Tulis kodemu di sini
#     huruf_vocal = "aiueo"
#     jumlah = 0
#     for karakter in teks.lower():
#         if karakter in huruf_vocal:
#             jumlah += 1
#     return jumlah
# def hitung_konsonan(teks):
#     # Tulis kodemu di sini
#     huruf_konsonan = "bcdfghjklmnpqrstvwxyz"
#     jumlah = 0
#     for karakter in teks.lower():
#         if karakter in huruf_konsonan:
#             jumlah += 1
#     return jumlah

# def hitung_huruf(teks, target):
#     # Tulis kodemu di sini
    
#     jumlah = 0
#     for karakter in teks.lower():
#         if karakter == target.lower():
#             jumlah += 1
#     return jumlah 

# def hitung_positif(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for angka in daftar:
#         if angka > 0:
#             jumlah += 1
#     return jumlah

# def jumlah_di_atas_10(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for angka in daftar:
#         if angka > 10:
#             jumlah += 1
#     return jumlah

# def jumlah_positif(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for angka in daftar:
#         if angka > 0:
#             jumlah = jumlah + angka 
#     return jumlah

# def hitung_kapital(teks):
#     # Tulis kodemu di sini
#     huruf_kapital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     jumlah = 0
#     for karakter in teks:
#         if karakter in huruf_kapital:
#             jumlah += 1
#     return jumlah

# def jumlah_genap(n):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for angka in range (1, n + 1):
#         if angka % 2 == 0:
#             jumlah = jumlah + angka
#     return jumlah

# def hitung_vokal(teks):
#     # Tulis kodemu di sini
#     huruf_vocal= "aiueo"
#     jumlah = 0
#     for karakter in teks.lower():
#         if karakter in huruf_vocal:
#             jumlah += 1
#     return jumlah

# def jumlah_positif(daftar):
#     # Tulis kodemu di sini
#     jumlah = 0
#     for angka in daftar:
#         if angka > 0:
#             jumlah = jumlah + angka
#     return jumlah

# def kilometer_ke_meter(kilometer):
#     # Tulis kodemu di sini
#     meter = kilometer * 1000
#     return meter

# def konversi_suhu(celsius):
#     # Tulis kodemu di sini
    
#     farenheit = (celsius * 9 / 5) + 32
    
#     if farenheit < 0 :
#         kategori = "Dingin"
#     elif 0 <= farenheit <= 30:
#         kategori = "Normal"
#     else:
#         kategori = "Panas"
#     return farenheit, kategori

# def konversi_berat(gram):
#     # Tulis kodemu di sini
#     kilogram = gram / 1000
#     if gram < 1000:
#         kategori = "Ringan"
#     elif 1000 <= gram <= 5000:
#         kategori = "Sedang"
#     else:
#         kategori = "Berat"
#     return kilogram, kategori

# def konversi_waktu(jam):
#     # Tulis kodemu di sini
#     detik = jam * 3600
#     if jam < 1 :
#         kategori = "singkat"
#     elif 1 <= jam <= 5 :
#         kategori = "Sedang"
#     else:
#         kategori = "Lama"
#     return detik, kategori

# def hitung_rerata_suhu(suhu1, suhu2, suhu3, suhu4):
#     # Tulis kodemu di sini
    
#     suhu =(suhu1 + suhu2 + suhu3 + suhu4) / 4
#     return suhu

# def hitung_nilai(nilai1, nilai2, nilai3):
#     # Tulis kodemu di sini
#     rata_rata = (nilai1 + nilai2 + nilai3)/3
#     if rata_rata >= 75 :
#         status = "Lulus"
#     elif rata_rata < 75 :
#         status = "Tidak Lulus"
#     return rata_rata, status

# def hitung_predikat(nilai1, nilai2, nilai3, nilai4):
#     # Tulis kodemu di sini
#     rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4
#     if rata_rata >= 90 :
#         predikat = "A"
#     elif 80 <= rata_rata < 90:
#         predikat = "B"
#     elif 70<= rata_rata < 80 :
#         predikat = "C"
#     elif 60 <= rata_rata < 70 :
#         predikat = "D"
#     else:
#         predikat = "E"
#     return rata_rata, predikat
      
# def analisis_nilai(nilai1, nilai2, nilai3, nilai4):
#     # Tulis kodemu di sini
#     rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4
#     tertinggi = max(nilai1, nilai2, nilai3, nilai4)
#     if rata_rata >= 75:
#         status = "Lulus"
#     elif rata_rata <= 75:
#         status = "Tidak Lulus"
#     return rata_rata, tertinggi, status

# def hitung_biaya_parkir(jam, adalah_member):
#     # Tulis kodemu di sini
#     biaya_jam_pertama = 5000
    
#     if jam + 1:
#         tambahan_biaya = biaya_jam_pertama + 3000
#     else:
#         tambahan_biaya = 0 

#     if adalah_member == True:
#         total_biaya = tambahan_biaya * 20 / 100
#     else:
#         total_biaya == tambahan_biaya 

# def hitung_biaya_parkir(jam, adalah_member):
#     if jam <= 0:
#         return 0

#     biaya_jam_pertama = 5000
#     tambahan_biaya = (jam - 1) * 3000
#     total_biaya = biaya_jam_pertama + tambahan_biaya

#     if adalah_member == True:
#         diskon = total_biaya * 20 / 100
#         total_biaya = total_biaya - diskon

#     return round(total_biaya)

# def hitung_belanja(harga, jumlah, member):
#     # Tulis kodemu di sini
#     if jumlah<=0:
#         return 0
#     subtotal = harga * jumlah
#     if subtotal >= 100000:
#         diskon = subtotal * 10 / 100
#     else:
#         diskon = 0
#     if member == True:
#         diskon_2 = subtotal * 5 / 100
#     else:
#         diskon_2 = 0
#     subtotal_akhir = subtotal - (diskon + diskon_2)
#     return subtotal_akhir

# def hitung_gaji(jam_kerja, tarif_per_jam):
#     # Tulis kodemu di sini
#     batas_jam = 40
#     if jam_kerja <= 0:
#         return 0
    
#     if jam_kerja <= 40:
#         total = jam_kerja * tarif_per_jam
#     else:
#         gaji_biasa = jam_kerja * tarif_per_jam
#         jam_tambahan =jam_kerja - batas_jam
#         gaji_lembur = jam_tambahan * tarif_per_jam * 1.5
#         total = gaji_biasa + gaji_lembur
#     return total


# def jumlah_ganjil(n):
#     # Write your code here
#     total = 0
#     for angka in range (1, n +1, 2):
#         total = total + angka
#     return total


# def hitung_akumulasi(n):
#     # Write your code here
    
#     total = 0
#     for angka in range (3, n + 1, 3):
#         if angka % 2 != 0:
#          total = total + angka
#     return total


# def hitung_pasangan(n):
#     # Write your code here
#     total = 0
    
#     for i in range (1, n + 1):
       
#        for j in range (1, n + 1):
         
#           if i + j == n:
#              total = total + 1
#     return total

# def hitung_kelipatan(n):
#     # Tulis kodemu di sini
#     total = 0
#     for angka in range(1, n + 1):
#        if angka % 3 == 0 or angka % 5 == 0:
#           total = total + 1
#     return total

# def hitung_digit_genap(n):
#     # Tulis kodemu di sini
#     total = 0
#     for angka in range (1, n + 1):
#        if angka % 2 == 0:
#           total = total + 1
#     return total

# antrean_awal = [10, 20, 30, 40, 50, 60]
# antrean_awal.append(70)

# antrean_awal.insert(2, 25)
# antrean_awal.remove(10)
# for i in range (1, 6, 2):
#     print (antrean_awal.append(70).insert(2, 25).remove(10))

# kata_kunci_kata = ["python", "java", "go", "kotlin"]
# hasil = []
# for x in kata_kunci_kata:
#     if len(x.upper) > 4 :
#         hasil += x
#     hasil="".join(reversed(hasil))
#     print(hasil)

# t = (1, 2, 3)
# l = list(t)
# l[0] = 10
# l.append(4)
# t = tuple(l)
# print(t)

# t = [("Mahasiswa A", 85), ("Mahasiswa B", 40), ("Mahasiswa C", 95)]
# for x in t:
#     if x in [0, 2] >= 80:
#         grade = "A"
#     elif x in [0, 2] >= 60:
#         grade = "B"
#     else:
#         grade = "C"
#         print(x)


    
teks_a = "ID: 1, 2, 2, 3, 4"
teks_b = "ID: 3, 4, 4, 5"
teks_a= teks_a.replace("ID:", "").split(",")
teks_b= teks_b.replace("ID:", "").split(",")

a = set()
b = set()

for item in teks_a:
    a.add(int(item))
for item in teks_b:
    b.add(int(item))

hasil = ((len(a)), len(a|b), len( a & b), len(a^b))
print(hasil)





    


    
   

