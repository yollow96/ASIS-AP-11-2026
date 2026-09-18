status = input("masukan status = ")
belanja = int(input("masukan belanja = "))

if status == "member":

    if belanja >= 100000 :
        print("Dapat diskon 20%")
    else:
        print("Dapat diskon 10%")

else:
    print("Tidak dapat diskon")