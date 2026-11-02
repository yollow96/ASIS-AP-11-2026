import re

list_username = []
def validasi_username(username):
    pola_username = r"^[a-zA-Z]\w{4,11}$"

    username_valid = re.match(pola_username, username)
    if username_valid:
        list_username.append(username)
        print("Username tersedia.\n")
        return True
    else:
        print("Username tidak valid!\n")
        return False

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

while True:
    username = input("Masukkan username: ")
    
    if username == "SELESAI":
        break
    validasi_username(username)
    
print("=== Rekapitulasi ===")
print(f"Username valid: ")

for nomor, nama in enumerate (list_username, start=1):
        print(f"{nomor}. {nama}")
    
print(f"\nJumlah username valid: {len(list_username)}")
