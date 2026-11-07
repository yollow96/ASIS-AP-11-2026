import re

def validasi_NIM(NIM):
    pola_NIM = r"^H071\d{6}$"

    NIM_valid = re.match(pola_NIM, NIM)
    if NIM_valid:
        print(f"{'NIM':<12}: NIM valid")
        return True
    else:
        print(f"{'NIM':<12}: Format NIM tidak valid!")
        return False

def validasi_email(email):
    pola_email = r"\w+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

    email_valid = re.match(pola_email, email)
    if email_valid:
        print(f"{'Email':<12}: Email valid")
        return True
    else:
        print(f"{'Email':<12}: Format email tidak valid!")
        return False

def validasi_no_telepon(nomor_telepon):
    pola_no_telepon = r"^\d{10,13}$"

    no_telepon_valid = re.match(pola_no_telepon, nomor_telepon)
    if no_telepon_valid:
        print(f"{'No. telp':<12}: Nomor telepon valid")
        return True
    else:
        print(f"{'No. telp':<12}: Nomor telepon  tidak valid!")
        return False

print("=== Validasi Data Mahasiswa ===" + "\n")
NIM = input(f"{'Masukkan nim':<19}: ")
email = input(f"{'Masukkan Email' :<19}: ")
nomor_telepon = input(f"{'Masukkan No. Telp' :<19}: ")

print("\n--- Hasil Validasi ---\n")
nim_ok = validasi_NIM(NIM)
email_ok = validasi_email(email)
telp_ok = validasi_no_telepon(nomor_telepon)

if nim_ok and email_ok and telp_ok:
    print("\nData Mahasiswa berhasil diverifikasi!")