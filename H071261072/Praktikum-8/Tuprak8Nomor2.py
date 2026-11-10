import re

print("=== PROGRAM PENYARINGAN USERNAME ===")

daftar_username = []

def validasi_username(username):
    pola_username = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"

    if re.match(pola_username, username):
        return True
    else:
        return False


while True:
    print("\nMasukkan SELESAI untuk mengakhiri program.")

    username = input("Masukkan username: ")

    if username == "SELESAI":
        print("\nProgram selesai.")
        break

    hasil_validasi = validasi_username(username)

    if hasil_validasi:
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")


print("\n=== DAFTAR USERNAME VALID ===")

if len(daftar_username) > 0:
    for nomor, username in enumerate(daftar_username, start=1):
        print(f"{nomor}. {username}")
else:
    print("Belum ada username yang valid.")

print("\nJumlah username yang valid:", len(daftar_username))