import re

# Function untuk memvalidasi NIM mahasiswa
# Aturan: Diawali 'H071' dan diikuti oleh tepat 6 digit angka
def validasi_nim(nim):
    pattern = r'^H071\d{6}$' # ^H071 = diawali H071, \d{6} = 6 digit angka, $ = akhir string
    return bool(re.match(pattern, nim))

# Function untuk memvalidasi Email mahasiswa
# Aturan: username@domain.ekstensi 
def validasi_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Function untuk memvalidasi Nomor Telepon
# Aturan: Terdiri dari 10-13 digit angka
def validasi_phone(phone):
    pattern = r'^\d{10,13}$' # \d{10,13} = 10 sampai 13 digit angka
    return bool(re.match(pattern, phone))

def main():
    print("=== Validasi Data Mahasiswa ===")
    print()
    
    # Meminta input data dari mahasiswa
    nim_input = input("Masukkan NIM       : ")
    email_input = input("Masukkan Email     : ")
    phone_input = input("Masukkan No. Telp  : ")
    print()

    # Memanggil masing-masing fungsi validasi
    is_nim_valid = validasi_nim(nim_input)
    is_email_valid = validasi_email(email_input)
    is_phone_valid = validasi_phone(phone_input)

    print("--- Hasil Validasi ---")
    
    # Cek dan tampilkan status NIM
    if is_nim_valid:
        print("NIM        : Valid")
    else:
        print("NIM        : Format NIM tidak valid!")

    # Cek dan tampilkan status Email
    if is_email_valid:
        print("Email      : Valid")
    else:
        print("Email      : Format email tidak valid!")

    # Cek dan tampilkan status Nomor Telepon
    if is_phone_valid:
        print("No. Telepon : Valid")
    else:
        print("No. Telepon : Nomor telepon tidak valid!")

    print()
    # Jika seluruh data valid, tampilkan pesan sukses
    if is_nim_valid and is_email_valid and is_phone_valid:
        print("Data mahasiswa berhasil diverifikasi!")

if __name__ == "__main__":
    main()