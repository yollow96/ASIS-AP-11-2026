def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(n - 1)

while True:
    n = int(input("Masukkan angka awal hitung mundur: "))
    if n >= 0:
        hitung_mundur(n)
        break
    print("Input tidak valid, angka tidak boleh negatif.")