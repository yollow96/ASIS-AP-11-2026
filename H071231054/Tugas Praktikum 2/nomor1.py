pedas = int(input("masukkan persentase cabai: "))

if pedas >= 0 and pedas <= 10:
    print("level aman")
elif pedas >= 11 and pedas <= 40:
    print("level sedang")
elif pedas >= 41 and pedas <= 70:
    print("level pedas")
elif pedas >70:
    print("Level ekstrem")
else:
    print("input tidak valid")
