#method overriding
# class Hewan :
#     def bersuara (self):
#         print("hewan mengeliarkan suara")

    #overloading (menggunakan default parameter)
    # def makan(self, makanan, jumlah=1):
    #       print(f"hewan memakan {jumlah} {makanan}")
    #overloading ( mengggunakan *args)
#     def makan(self, *makanan):
#         print(f"hewan memakan :")

#         for i in makanan:
#             print(f" {i}")
    
# class kucing(Hewan):
#     def bersuara (self):
#             print("meow")

# class anjing (Hewan):
#     def bersuara (self):
#             print("gukguk")

# class sapi (Hewan):
#     def bersuara (self):
#             print("moo")

# hewan1 = Hewan()
# hewan2 = Hewan()
# hewan1.makan("Daging")
# hewan2.makan("Ikan", "wortel", "rumput")

# operator overloading

# class Hewan():
#     def __init__(self, nama, jenis):
#         self.nama = nama
#         self.jenis = jenis

#     def __str__(self):
#         return f"{self.nama} adalah {self.jenis}"
#     def __eq__(self, hewan_lain):
#         return self.jenis == hewan_lain

# babi = Hewan("Selo", "babi")
# anjing = Hewan ("Selo", "babi")

# print(babi)
# print(babi == anjing)
from abc import ABC, abstractmethod
class Notifikasi:
    @abstractmethod
    def kirim_pesan(self, pesan):
        pass
class WhatsApp(Notifikasi):
    def kirim_pesan (self, pesan):
        print("mengirim pesan melalui WhatsApp : {pesan}")
        print(f"{pesan}")
class Email:
    def kirim_pesan (self, pesan):
        print("mengirim pesan melalui Email : {pesan}")
        print(f"{pesan}")
class SMS:
     def kirim_pesan (self, pesan):
        print("mengirim pesan melalui SMS: {pesan}")
        print(f"{pesan}")

whatsapp = WhatsApp()
email = Email()
sms = SMS()


# # pesan1 =  

# from abc import ABC, abstractmethod

# class Notifikasi(ABC):
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur

#     def tampilkan_info(self):
#         print(f"Nama : {self.nama}")
#         print(f"Umur : {self.umur}")

#     @abstractmethod
#     def bersuara():
#         pass
# #child class
# class Kucing (Hewan):
#     def bersuara(self):
#         print("Kucing bersuara : meow")

# class Anjing (Hewan):
#     def bersuara(self):
#         print("Anjing bersuara : gukguk")

# class Sapi (Hewan):
#     def bersuara(self):
#         print("Sapi bersuara : mooo")

# kucing = Kucing("Miki", 1)
# anjing = Anjing("Choco", 2)
# sapi = Sapi("Sawo", 3)

# daftar_hewan = [kucing, anjing, sapi]
# for hewan in daftar_hewan:
#     hewan.tampilkan_info()
#     hewan.bersuara()
#     print("-" * 35)

