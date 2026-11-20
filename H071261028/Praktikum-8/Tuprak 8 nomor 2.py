import re

def validasi_username(username):
    pola = r"^[a-zA-Z]\w{4,11}$"
    return re.match(pola, username)


print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

daftar_username = []

while True:
    username = input("\nMasukkan username: ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print("=== Rekapitulasi ===")
print("Username valid:")

for i, username in enumerate(daftar_username, start=1):
    print(f"{i}. {username}")

print(f"\nJumlah username valid: {len(daftar_username)}")
