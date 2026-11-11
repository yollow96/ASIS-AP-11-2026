import re

def validasi_nim(nim: str) -> bool:
    # Diawali H071 dan diikuti tepat 6 digit angka (total 10 karakter)
    pattern = r"^H071\d{6}\$"
    return bool(re.match(pattern, nim))

def validasi_email(email: str) -> bool:
    # Username, @, domain, titik, dan ekstensi
    pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}\$"
    return bool(re.match(pattern, email))

def validasi_telp(telp: str) -> bool:
    # Tepat 10 - 13 digit angka
    pattern = r"^\d{10,13}\$"
    return bool(re.match(pattern, telp))

def main():
    print("=== Validasi Data Mahasiswa ===")
    print()
    
    nim = input("Masukkan NIM        : ").strip()
    email = input("Masukkan Email      : ").strip()
    telp = input("Masukkan No. Telp   : ").strip()
    
    is_nim_valid = validasi_nim(nim)
    is_email_valid = validasi_email(email)
    is_telp_valid = validasi_telp(telp)
    
    print("\n--- Hasil Validasi ---")
    print(f"NIM        : {'Valid' if is_nim_valid else 'Format NIM tidak valid!'}")
    print(f"Email      : {'Valid' if is_email_valid else 'Format email tidak valid!'}")
    print(f"No. Telepon: {'Valid' if is_telp_valid else 'Nomor telepon tidak valid!'}")
    print()
    
    if is_nim_valid and is_email_valid and is_telp_valid:
        print("Data mahasiswa berhasil diverifikasi!")

if __name__ == "__main__":
    main()