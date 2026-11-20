import re

def validasi_nim(nim):
    pola_nim = r"^H071\d{6}$"
    return re.match(pola_nim, nim)


def validasi_email(email):
    pola_email = r"^[\w]+@[a-z]+\.[a-z]{2,}$"
    return re.match(pola_email, email)


def validasi_telepon(telepon):
    pola_telepon = r"^\d{10,13}$"
    return re.match(pola_telepon, telepon)


print("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

hasil_nim = validasi_nim(nim)
hasil_email = validasi_email(email)
hasil_telepon = validasi_telepon(telepon)

print("\n--- Hasil Validasi ---")

print("NIM         :", "Valid" if hasil_nim else "Format NIM tidak valid!")
print("Email       :", "Valid" if hasil_email else "Format email tidak valid!")
print("No. Telepon :", "Valid" if hasil_telepon else "Nomor telepon tidak valid!")

if hasil_nim and hasil_email and hasil_telepon:
    print("\nData mahasiswa berhasil diverifikasi!")
