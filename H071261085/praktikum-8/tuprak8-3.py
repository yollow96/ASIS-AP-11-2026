import re

# Function untuk menghapus spasi dan tanda '-' dari input nomor telepon
def bersihkan_nomor(nomor):
    # re.sub(pattern, replacement, string) menghapus spasi (\s) dan tanda minus (-)
    return re.sub(r'[\s-]', '', nomor)

# Function untuk mengecek apakah nomor hasil pembersihan bernilai valid
# Hanya boleh berisi angka dengan panjang 10-13 digit
def validasi_nomor(nomor_bersih):
    pattern = r'^\d{10,13}$'
    return bool(re.match(pattern, nomor_bersih))

def main():
    print("=== Pembersihan Data Nomor Telepon ===")
    jumlah = int(input("Masukkan jumlah data: ")) # Input jumlah data
    
    data_list = [] # List menampung riwayat data sebelum, sesudah, dan status
    jumlah_valid = 0 # Counter penghitung jumlah nomor valid
    
    # Looping menerima input sesuai jumlah data
    for i in range(1, jumlah + 1):
        nomor_awal = input(f"Nomor ke-{i}: ")
        
        # Langkah 1: Bersihkan nomor menggunakan re.sub()
        nomor_sesudah = bersihkan_nomor(nomor_awal)
        
        # Langkah 2: Cek validasi nomor setelah dibersihkan
        if validasi_nomor(nomor_sesudah):
            status = "Valid"
            jumlah_valid += 1 # Tambah counter jika valid
        else:
            status = "Tidak valid"
            
        # Simpan ke list data
        data_list.append({
            "sebelum": nomor_awal,
            "sesudah": nomor_sesudah,
            "status": status
        })

    print("\n--- Hasil Pembersihan ---")
    
    # Menampilkan rekapitulasi data sebelum dan sesudah dibersihkan
    for idx, item in enumerate(data_list, start=1):
        print(f"Data {idx}:")
        print(f"Sebelum: {item['sebelum']}")
        print(f"Sesudah: {item['sesudah']}")
        print(f"Status : {item['status']}")
        print()

    # Menampilkan total jumlah nomor valid
    print(f"Jumlah nomor valid: {jumlah_valid}")

if __name__ == "__main__":
    main()