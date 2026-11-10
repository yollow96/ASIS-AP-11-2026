import re

def bersihkan_nomor(nomor: str) -> str:
    # Mengabaikan/menghapus spasi dan tanda '-' menggunakan re.sub()
    pattern = r"[\s-]"
    return re.sub(pattern, "", nomor)

def validasi_nomor_bersih(nomor_bersih: str) -> bool:
    # Memastikan hasil akhir berupa 10 - 13 digit angka
    pattern = r"^\d{10,13}\$"
    return bool(re.match(pattern, nomor_bersih))

def main():
    print("=== Pembersihan Data Nomor Telepon ===")
    jumlah = int(input("Masukkan jumlah data: "))
    
    raw_list = []
    for i in range(1, jumlah + 1):
        raw = input(f"Nomor ke-{i}: ").strip()
        raw_list.append(raw)
        
    print("\n--- Hasil Pembersihan")
    valid_count = 0
    valid_numbers = []
    
    for idx, raw in enumerate(raw_list, start=1):
        cleaned = bersihkan_nomor(raw)
        is_valid = validasi_nomor_bersih(cleaned)
        
        status = "Valid" if is_valid else "Tidak valid"
        if is_valid:
            valid_count += 1
            valid_numbers.append(cleaned)
            
        print(f"Data {idx}:")
        print(f"Sebelum: {raw}")
        print(f"Sesudah: {cleaned}")
        print(f"Status : {status}")
        if idx < jumlah:
            print()
            
    print(f"\nJumlah nomor valid: {valid_count}")

if __name__ == "__main__":
    main()
    