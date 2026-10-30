def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for char in teks.lower():
        if char in alfabet:
            hasil += char
    return hasil

def cek_palindrome(teks):
    rev = "".join(reversed(teks))
    if teks == rev:
        return True, -1
    for i in range(len(teks)):
        if teks[i] != rev[i]:
            return False, i
    return False, -1

def inti_palindrome(teks):
    bersih = bersihkan_teks(teks)
    terpanjang = ""
    indeks = 0
    for i in range(len(bersih)):
        for j in range(i + 1, len(bersih) + 1):
            sub = bersih[i:j]
            is_palin, _ = cek_palindrome(sub)
            if is_palin and len(sub) > len(terpanjang):
                terpanjang = sub
                indeks = i
    return {"teks": terpanjang, "panjang": len(terpanjang), "indeks_awal": indeks}

teks_input = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(teks_input)
hasil = inti_palindrome(teks_input)

print(f"Teks Bersih: {teks_bersih}")
print(f"Output Terharap: {hasil}")