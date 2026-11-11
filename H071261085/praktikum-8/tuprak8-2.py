import re

# Function untuk validasi username menggunakan Regular Expression
def validasi_username(username):
    # Aturan username:
    # 1. Diawali huruf: ^[a-zA-Z]
    # 2. Diikuti huruf, angka, atau underscore: [a-zA-Z0-9_]
    # 3. Panjang 5-12 karakter (1 karakter pertama + 4-11 karakter berikutnya): {4,11}$
    # 4. Tidak boleh mengandung spasi                                       
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    return bool(re.match(pattern, username))

def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.\n")
    
    list_username_valid = [] # List tempat menyimpan username yang valid
    
    # While loop terus berjalan sampai pengguna memasukkan 'SELESAI'
    while True:
        username = input("Masukkan username: ")
        
        # Kondisi berhenti ketika menginput 'SELESAI'
        if username == "SELESAI":
            break
            
        # Proses validasi username
        if validasi_username(username):
            print("Username tersedia.")
            list_username_valid.append(username) # Tambahkan ke list jika valid
        else:
            print("Username tidak valid!")

    print("\n=== Rekapitulasi ===")
    print("Username valid:")
    
    # Menampilkan seluruh username valid dalam bentuk bernomor
    for idx, u in enumerate(list_username_valid, start=1):
        print(f"{idx}. {u}")
        
    # Menampilkan total jumlah username valid
    print(f"Jumlah username valid: {len(list_username_valid)}")

if __name__ == "__main__":
    main()