def countdown(detik):
    print (detik)
    if detik == 0:
        print("Luncurkan!")
    else:
        countdown(detik-1)

def minta_angka():
    angka = int(input("Masukan angka awal hitung mundur: "))
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
        return minta_angka()
    return angka

angka = minta_angka()
countdown(angka)
#countdown(minta_angka())
