import re

def validasi_username(username: str) -> bool:
    # Diawali huruf, diikuti huruf/angka/underscore, panjang 5-12 karakter
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}\$"
    return bool(re.match(pattern, username))

def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")
    
    valid_usernames = []
    
    while True:
        user_input = input("Masukkan username: ").strip()
        
        if user_input == "SELESAI":
            break
            
        if validasi_username(user_input):
            print("Username tersedia.")
            valid_usernames.append(user_input)
        else:
            print("Username tidak valid!")
            
    print("\n=== Rekapitulasi ===")
    print("Username valid:")
    for idx, uname in enumerate(valid_usernames, start=1):
        print(f"{idx}. {uname}")
        
    print(f"Jumlah username valid: {len(valid_usernames)}")

if __name__ == "__main__":
    main()