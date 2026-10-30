def hitung_mundur(n):
    if n < 0:
        return
    print(n)
    if n == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(n - 1)

angka = int(input("Masukkan angka awal hitung mundur: "))
if angka < 0:
    print("Input tidak valid, angka tidak boleh negatif.")
else:
    hitung_mundur(angka)