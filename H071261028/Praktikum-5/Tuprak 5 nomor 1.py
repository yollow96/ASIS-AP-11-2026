def bersihkan_teks (teks):
    huruf = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in teks:
        if karakter.lower() in huruf:
            hasil += karakter.lower()
    return hasil

def cek_palinrome (teks):
    palinrome = "".join(reversed(teks)) #menghasilkan karakter secara terbalik, join menggabungkannya menjadi string
    if teks == palinrome:
        return(True, -1) #-1 tidak ada posisi yang salah

    for i in range(len(teks)):
        if teks [i] != palinrome[i]: #membandingkan karakter pada posisi yg sama
            return (False, i)

def inti_palinrome (teks):
    palinrome_terpanjang = ""
    indeks_awal = 0 #menyimpan posisi awal palinrome terpanjang

    for i in range (len(teks)): #menentukan indeks mana substring dimulai
        for j in range (i + 1, len(teks) + 1):#menentukan batas akhir substring 
            substring = teks[i:j] #mengambil sebagian teks berdasarkan indeks i sampai sebelum j

            hasil_cek = cek_palinrome(substring)

            if hasil_cek[0] == True:
                if len(substring) > len(palinrome_terpanjang): #mengecek apakah palindrome baru lbih pnjng dari palindrome yg sdh disimpan di awal
                    palinrome_terpanjang = substring #menyimpan palindrome yg baru ditemukan
                    indeks_awal = i #menyimpan posisi awal palindrome tersebut

    return {
        "teks": palinrome_terpanjang,
        "panjang": len(palinrome_terpanjang),
        "indeks_awal": indeks_awal
    }

teks = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks)

print()
print("Teks Bersih:", teks_bersih)

hasil = inti_palinrome(teks_bersih) #mencari palindrome terpanjang

print("Output Terharap:", hasil)