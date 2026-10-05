karakter = input("karakter = ")
if karakter >= "A" and karakter <= "Z":
    print(f"Huruf kapital? {True}")
else:
    print(f"Huruf kapital? {False}")

if karakter >= "a" and karakter <= "z":
    print(f"Huruf kecil? {True}")
else:
    print(f"Huruf kecil? {False}")

if karakter >= "0" and karakter <= "9":
    print(f"Angka? {True}")
else:
    print(f"Angka? {False}")