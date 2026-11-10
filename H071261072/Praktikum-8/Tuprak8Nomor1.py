import re

print("=== PROGRAM VALIDASI DATA MAHASISWA ===")

def validasi_nim(nim):
    pola_nim = r"^H071[0-9]{6}$"

    if re.match(pola_nim, nim):
        return True
    else:
        return False


def validasi_email(email):
    pola_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pola_email, email):
        return True
    else:
        return False


def validasi_telepon(telepon):
    pola_telepon = r"^[0-9]{10,13}$"

    if re.match(pola_telepon, telepon):
        return True
    else:
        return False


nim = input("Masukkan NIM mahasiswa: ")
email = input("Masukkan email mahasiswa: ")
telepon = input("Masukkan nomor telepon: ")

print("\n=== HASIL VALIDASI ===")

hasil_nim = validasi_nim(nim)
hasil_email = validasi_email(email)
hasil_telepon = validasi_telepon(telepon)

if hasil_nim:
    print("NIM valid.")
else:
    print("Format NIM tidak valid!")

if hasil_email:
    print("Email valid.")
else:
    print("Format email tidak valid!")

if hasil_telepon:
    print("Nomor telepon valid.")
else:
    print("Nomor telepon tidak valid!")

if hasil_nim and hasil_email and hasil_telepon:
    print("\nData mahasiswa berhasil diverifikasi!")
else:
    print("\nData mahasiswa gagal diverifikasi!")