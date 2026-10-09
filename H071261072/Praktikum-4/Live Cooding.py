x = input("Masukkan 1 karakter: ")

kapital = x >= 'A' and x <= 'Z'
kecil = x >= 'a' and x <= 'z'
angka = x >= '0' and x <= '9'

print("Huruf Kapital?", kapital)
print("Huruf Kecil?", kecil)
print("Angka?", angka)