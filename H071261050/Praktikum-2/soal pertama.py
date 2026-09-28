Tingkat_kepedasan = int(input("Masukkan presentase cabai: "))

if Tingkat_kepedasan >= 0 and Tingkat_kepedasan <= 10:
    print("Level Aman")

elif Tingkat_kepedasan >= 11 and Tingkat_kepedasan <= 40:
    print("Level Sedang")

elif Tingkat_kepedasan > 70:
    print("level Ekstrem")

elif Tingkat_kepedasan >= 41 and Tingkat_kepedasan <= 70:
    print("Level Pedas")

# elif Tingkat_kepedasan >= 70:
#     print("level Ekstrem")

else:
    print("Tidak Valid")

