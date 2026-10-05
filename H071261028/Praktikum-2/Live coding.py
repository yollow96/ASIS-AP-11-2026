while True:
    karakter = input("Karakter :")

    if karakter >= "A" and karakter <= "Z":
        print("Huruf kapital?", True)
        
    else:
        print("Huruf kapital?", False)
        
    if karakter >= "a" and karakter <= "z":
        print("Huruf kecil?", True)
    else:
        print("Huruf kecil?", False)

    if karakter >= "0" and karakter <= "9":
        print("Angka ?:", True)
    else:
        print("Angka ?:", False)
    continue
    
    

    
