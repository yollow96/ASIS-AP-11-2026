import re

def validasi_username(username):
    if re.match(r"^[a-zA-Z]\w{4,11}$", username):
        print("Username tersedia.")
        return True
    else:
        print("Username tidak valid!")
        return False


daftar_username = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

while True:
    username = input("\nMasukkan username: ")

    if username.upper() == "SELESAI":
        break

    if validasi_username(username):
        daftar_username.append(username)

print("\n=== Rekapitulasi ===")
print("Username valid:")

for i in range(len(daftar_username)):
    print(f"{i + 1}. {daftar_username[i]}")

print(f"\nJumlah username valid: {len(daftar_username)}")