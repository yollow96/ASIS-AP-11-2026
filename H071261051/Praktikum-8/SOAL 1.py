import re #import modul regex 

def validasi_nim(nim):
    if re.match(r"^H071[0-9]{6}$", nim):
        print("NIM valid.")
        return True
    else:
        print("Format NIM tidak valid!")
        return False


def validasi_email(email):
    if re.match(r"^\w+@[a-zA-Z]+(\.[a-zA-Z]{2,})+$", email): #raw string, yaitu membuat Python membaca tanda \ (backslash) sebagai karakter biasa
        print("Email valid.")
        return True
    else:
        print("Format email tidak valid!")
        return False


def validasi_telepon(telepon):
    if re.match(r"^[0-9]{10,13}$", telepon):
        print("Nomor telepon valid.")
        return True
    else:
        print("Nomor telepon tidak valid!")
        return False


print("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print("\n--- Hasil Validasi ---")

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")