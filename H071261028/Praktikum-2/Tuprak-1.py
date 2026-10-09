persentase_cabai = int(input("Masukkan persentase cabai:"))
if 0 <= persentase_cabai <=10 :
    print("level aman")
elif 11 <= persentase_cabai <= 40 :
    print("level sedang")
elif 41 <= persentase_cabai <= 70 :
    print("level pedas")
elif 70 < persentase_cabai <= 100 :
    print("level ekstrem")
else :
    print("tidak valid")